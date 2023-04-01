# Assignment 1, NLP Senior Seminar

#### wmjg

## BUILT WITH Python 3.10.6

##  STEPS TO SETUP:
* in command line setup a new Virtual Environment
* run pip install -r requirements.txt
* get the spacy model with: python -m spacy download en_core_web_sm 

##  For the Flask App:
* simply run python app.py from the directory
* then navigate to http://127.0.0.1:5000/
* you should see an html render of the spacy output for the example text
* you can enter new text for spacy to analyze and display.

##  For the Restful API:
* Leave the python app.py server running
* From ANOTHER CMD LINE try the commands:
    * curl http://127.0.0.1:5000/api 
        * READS THE EXAMPLE input.txt
    * curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api  
        * READS the input data file

##  For the Streamlit App:
* via cmd line we run app2.py with:
    * streamlist run app2.py
    * your browser should open, but you can access it with http://localhost:8501/
* This app vizualizes text with NER and for Dependencies
* in the sidebar you can switch to larger "better" spaCy models 
    * But you'll need to download them with the command:
    * python -m spacy download MODELNAME
