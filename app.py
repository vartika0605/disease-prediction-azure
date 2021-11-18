from flask import Flask, render_template, request,jsonify
import pickle
import numpy as np
import pandas as pd





model = pickle.load(open('diseasePrediction.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html',data = '')
   



@app.route('/predict', methods=['POST'])
def home():
    df2 = pd.read_csv('Symptom-severity.csv')
    a = np.array(df2["Symptom"])
    b = np.array(df2["weight"])
    data1 = request.form['e']
    print(data1)
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    if data1=='':
        data1='0'
    if data2=='':
        data2='0'

    if data3=='':
        data3='0'


    if data4=='':
        data4='0'            
    

    if (data1=='0' and data2=='0' and data3=='0' and data4=='0'):
        msg = "OPPS!! , ENTER  SYMPTOMS PLEASE"
        jsonify(msg)
        return render_template('home.html',data =msg)
   
    else :
        arr = np.array([[data1, data2, data3, data4,0,0,0,0,0,0,0,0,0,0,0,0,0]])

        for j in range(4):
            prev= arr[0][j]
            for k in range(len(a)):
                if arr[0][j]==a[k]:
                     arr[0][j]=b[k]
            if arr[0][j]==prev:
                arr[0][j]='0'      
            
        print(arr)
        arr[0] = arr[0].astype(np.float)
        print(arr)
        pred = model.predict(arr)
        
        pred=pred[0]
        jsonify(pred)
        return render_template('after.html', data=pred)
    
       

    

if __name__ == "__main__":
    app.run(debug=True)















