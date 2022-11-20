from integration import *
from flask import Flask

app = Flask(__name__)

@app.route('/numericalintegralservice/<lower>/<upper>')
def index(lower, upper):
    result = ""
    for i in subintervals:
        j = integral(fn, i, float(lower), float(upper))
        result += "<p> i=" + str(i) + ": " + str(j) + "</p>"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
