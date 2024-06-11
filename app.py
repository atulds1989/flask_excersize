from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/", methods =['GET', 'POST'])
def index():
    bmi = None
    if request.method=='POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi =  calc_bmi(weight, height)

    return render_template('bmi_calc.html', bmi=bmi)


def calc_bmi(weight, height):
    bmi = weight / (height/1000)**2
    return round(bmi, 2)


if __name__ == '__main__':  
   app.run(debug=True)




###################################
# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     bmi = None
#     if request.method == 'POST':
#         weight = request.form.get('weight')
#         height = request.form.get('height')
#         if weight and height:
#             try:
#                 weight = float(weight)
#                 height = float(height)
#                 bmi = calc_bmi(weight, height)
#             except ValueError:
#                 bmi = "Invalid input"
#     return render_template('bmi_calc.html', bmi=bmi)

# def calc_bmi(weight, height):
#     bmi = weight / (height / 100) ** 2
#     return round(bmi, 2)

# if __name__ == '__main__':
#     app.run(debug=True)
