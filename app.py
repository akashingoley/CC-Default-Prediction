from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        LIMIT_BAL = int(request.form['LIMIT_BAL'])
        SEX = int(request.form['SEX'])
        EDUCATION = int(request.form['EDUCATION'])
        MARRIAGE= int(request.form['MARRIAGE'])
        AGE= int(request.form['AGE'])
        PAY_1= int(request.form['PAY_1'])
        PAY_2= int(request.form['PAY_2'])
        PAY_3= int(request.form['PAY_3'])
        PAY_4= int(request.form['PAY_4'])
        PAY_5= int(request.form['PAY_5'])
        PAY_6= int(request.form['PAY_6'])
        BILL_AMT1= int(request.form['BILL_AMT1'])
        BILL_AMT2= int(request.form['BILL_AMT2'])
        BILL_AMT3= int(request.form['BILL_AMT3'])
        BILL_AMT4= int(request.form['BILL_AMT4'])
        BILL_AMT5= int(request.form['BILL_AMT5'])
        BILL_AMT6= int(request.form['BILL_AMT6'])
        PAY_AMT1= int(request.form['PAY_AMT1'])
        PAY_AMT2= int(request.form['PAY_AMT2'])
        PAY_AMT3= int(request.form['PAY_AMT3'])
        PAY_AMT4= int(request.form['PAY_AMT4'])
        PAY_AMT5= int(request.form['PAY_AMT5'])
        PAY_AMT6= int(request.form['PAY_AMT6'])
        
    values = np.array([[ LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_1,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,
                        BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,
                        PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6 ]])

    prediction = model.predict(values)
    if prediction == 0:
        label = 'Not be Defaulted'
    else:
        label = 'Be Defaulted'

    return render_template('result.html', prediction_text=label)


if __name__ == "__main__":
    app.run(debug=True)