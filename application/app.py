from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])

def calculate(): 
    bmi = 0
    if request.method=='POST' and 'weight' in request.form and 'height_ft'in request.form and 'height_inch' in request.form:
        w = float(request.form.get('weight'))
        h_ft = float(request.form.get('height_ft'))
        h_in = float(request.form.get('height_inch'))
        bmi = round((0.45 * w)/((((h_ft * 12) + h_in) * 0.025) ** 2), 2)
    return render_template('index.html', bmi=bmi)
