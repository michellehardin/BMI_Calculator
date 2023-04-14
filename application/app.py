from flask import Flask, render_template, request
from functions import determine_category, determine_bmi

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def calculate(): 
    bmi = 0
    category = ''
    if request.method=='POST' and 'weight' in request.form and 'height_ft'in request.form and 'height_inch' in request.form:
        w = float(request.form.get('weight'))
        h_ft = float(request.form.get('height_ft'))
        h_in = float(request.form.get('height_inch'))
        bmi = determine_bmi(w, h_ft, h_in)
        category = determine_category(bmi)
    else: 
        bmi = 0
        category = ''
    return render_template('index.html', bmi=bmi, category=category)
