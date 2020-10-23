import flask
import pandas as pd
import os
from fpdf import FPDF
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/home/<name>', methods=['GET'])
def home(name):
    return "Welcome %s" %name


'''@app.route('/stats/<file>', methods=['GET'])
def stats(file):
    pt = 'c:/users/t621123/PycharmProjects/hack/'
    file_name = os.path.join(pt,file)
    df = pd.read_csv(file_name)
    out= df.describe()
    output = out
    output.to_json(r'c:/users/t621123/PycharmProjects/hack/Stats.json')
    return "File stats Success. Check storage for Json output"
'''

@app.route('/stats/<file>', methods=['GET'])
def stats(file):
    pt = 'c:/users/t621123/PycharmProjects/hack/'
    file_name = os.path.join(pt,file)
    df = pd.read_csv(file_name)
    out= df.describe()
    result = out.to_json()
    parsed = json.loads(result)
    final = json.dumps(parsed, indent=4)
    return final



@app.route('/convert/<file>', methods=['GET'])
def convert(file):
    pt = 'c:/users/t621123/PycharmProjects/hack/'
    file_name = os.path.join(pt, file)

    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    # open the text file in read mode
    f = open(file_name, "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')

        # save the pdf with name .pdf
    pdf.output("output.pdf")
    return "File Conversion Success. Check storage for pdf output"


app.run(host='0.0.0.0')