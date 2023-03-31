from flask import Flask, Markup, request, render_template
from flask_restful import Resource, Api
from ner import get_entities_with_markup
import jsonify

with open('input.txt','r',encoding='utf8') as fx:
    exampleX = str(fx.read())

app = Flask(__name__)



################################################FLASK##############################################
@app.route("/", methods=['GET', 'POST'])
def go_home():
    if request.method == 'POST':
        text = request.form.get('userbox')
        X = str(text)
    elif request.method == 'GET':
        X = exampleX
    else:
        #USEFUL FOR BUGFIXING WHILE BUILDING
        user_input = request.get_json()
        
        return render_template('fail.html', result=user_input)
    
    mkup = get_entities_with_markup(X)
    return render_template('index.html', result=Markup(mkup))

############################################################RESTFUL########################################
api = Api(app)

class JASON(Resource):
    def get(self):
        mkup = get_entities_with_markup(exampleX)
        return {"text":exampleX, "markup":mkup}

    def post(self):
        X = request.data.decode()
        mkup = get_entities_with_markup(X)
        return {"text":X, "markup":mkup}

api.add_resource(JASON, '/api')


if __name__ == '__main__':
    app.run(debug=True)