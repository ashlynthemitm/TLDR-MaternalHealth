from flask import Flask
import datetime

x = datetime.datetime.now()

app = Flask(__name__)


@app.route('/data')
def sendData():
    return {
        'Name': 'Ashlyn Campbell'
    }
    
if __name__ == '__main__':  
    app.run(debug=True)