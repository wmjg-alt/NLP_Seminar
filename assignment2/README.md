# Assignment 2, NLP Senior Seminar

#### wmjg

## BUILT WITH Python 3.10.6

##  STEPS TO SETUP:
    * download my assignment2 files from https://github.com/wmjg-alt/NLP_Seminar
    * With docker running/accessible simply user the Dockerfile to generate an Image
        * COMMAND: docker build --tag assignment2
        * Let docker run through much pip installing, etc

## STEPS TO RUN:
    * Now run the image in a container with the following command:
        * docker run -d -p 5000:5000 assignment2
    * With a web browser navigate to:
        * 127.0.0.1:5000 

## USE:
    * Use the prefilled text box to NER the example text from input.txt
    * a database will be filled with the entities
    * the labelled entities will be visualized 
    * and the counts of how many times the entities appears in user inputs will be charted in the table below.

* Be sure to kill the container and image when you're done.
