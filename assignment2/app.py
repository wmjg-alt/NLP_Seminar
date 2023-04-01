''' Michael Gardner Assignment2, flask app with database storing entities '''
from flask import Flask, Markup, request, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from ner import get_entities_with_markup, get_entities

with open('input.txt', 'r', encoding='utf8') as fx:
    EXAMPLEX = str(fx.read())

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AV3ryS3cr3TK3y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Entity(db.Model):
    ''' Entity; a database class of id, term, label, occurrence '''
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(256), unique=True, nullable=False)
    label = db.Column(db.String(128), unique=False, nullable=False)
    occurrence = db.Column(db.Integer)

    def __repr__(self):
        ''' representation of Entity class as: Entity term occurrence'''
        return '<Entity %r %r>' % (self.term, self.occurrence)


def create_all():
    ''' create all db contexts '''
    with app.app_context():
        db.create_all()


def update_entity(user_text: str):
    ''' Take text, get entities,
        fill database with those entities,
        return all entities
    '''
    ents = get_entities(user_text)
    for ent in ents:
        # The ents are going to war
        e_text = ent[3].upper()
        ent_query = Entity.query.filter_by(term=e_text).first()

        if ent_query:
            ent_query.occurrence = ent_query.occurrence + 1
        else:
            dbentity = Entity(term=e_text, label=ent[2], occurrence=1)
            db.session.add(dbentity)

        db.session.commit()

    return Entity.query.all()


# #######################################FLASK##############################################
@app.route("/", methods=['GET', 'POST'])
def go_home():
    ''' flask app route for HOME, handling POST and GET separately'''
    if request.method == 'POST':
        text = request.form.get('userbox')
        target_str = str(text)
        ents = update_entity(target_str)
        mkup = get_entities_with_markup(target_str)
        return render_template('index.html',
                               result=Markup(mkup),
                               entities=ents)

    elif request.method == 'GET':
        return render_template('index.html',
                               result=EXAMPLEX,
                               entities=None)

    else:
        # USEFUL FOR BUGFIXING WHILE BUILDING
        user_input = request.get_json()
        return render_template('fail.html',
                               result=user_input)


# ###########################################RESTFUL#####################################
api = Api(app)


class JASON(Resource):
    ''' restful api text ner markup retrieval '''
    def get(self):
        ''' restful get, returning example markup'''
        mkup = get_entities_with_markup(EXAMPLEX)
        return {"text": EXAMPLEX, "markup": mkup}

    def post(self):
        ''' restful post, returning userinput markup'''
        user_text = request.data.decode()
        mkup = get_entities_with_markup(user_text)
        return {"text": user_text, "markup": mkup}


api.add_resource(JASON, '/api')


if __name__ == '__main__':
    create_all()
    app.run(debug=True, host="0.0.0.0")
