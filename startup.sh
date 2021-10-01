#!/bin/sh



helpFunction()
{
   echo ""
   echo "Usage: $0 [start] [test]"
   echo -e "\tstart for running our Flask api"
   echo -e "\ttest for testing our Flask api"
   exit 1 # Exit script after printing help
}


#set project app
export FLASK_APP=app.py


if [ $1 = "start" ]; then
    echo "Starting Flask server \t"
    #run app
    python -m pip install -r requirements.txt
    python -m flask run
elif [ $1 = "test" ]; then
        echo "Running test cases \t"
        #run app
        python -m pip install -r requirements.txt
        python apitest.py
else 
    helpFunction
fi





