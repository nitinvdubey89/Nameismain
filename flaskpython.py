## in  an import files, the code gets executed at indentation lelvel 0
## special built in variable __name__ that gets assigned  a string depending on how we are running the actual script
##  python will do __name__  = '__main__' i.e. __name__ = name of the python script

from flask import Flask

app = Flask(__name__) ## everyfile a unique name



## use  a decorator

@app.route('/')   # 'http://www.google.com/' ### tell whhat type of request we need to handle in flasks  you want to understand
                  # when we access www.google.com , we actually access http://www.google.com/ or google.com/maps or /plus


def home():
    return "BHaag bhosadike world"

app.run(port = 5000)  # mention port as a parameter

## http://localhost:5000/ google chrome hides the trailing / http://localhost:5000 but its always there




