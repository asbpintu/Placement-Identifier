from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@ app.route('/' , methods = ['GET','POST'])
def home():
    prediction=''
    if request.method == 'POST':
        try:
            cgpa = float(request.form['cgpa'])
            iq = float(request.form['iq'])
            ps = float(request.form['ps'])
            
            result = model.predict([[cgpa,iq,ps]])
            
            if result==1:
                prediction = 'You will be Placed'
            else:
                prediction = 'You may not be Placed'
        except:
            None
    return render_template('index.html',value = prediction)



@ app.route('/about')
def about():
    return 'My Name is Ardhendu Shekhar!!!'



if __name__ == '__main__':
    app.run(debug=True)