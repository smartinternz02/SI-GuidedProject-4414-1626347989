import numpy as np
from flask import Flask,request,render_template
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import pandas as pd
global model, graph, c
import tensorflow as tf
#graph =  tf.get_default_graph()
model = load_model('airline4-copy1.h5')
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ind')
def index2():
    return render_template('index2.html')

@app.route('/login', methods =['POST'])
def login():
    return render_template('index.html')
    year = request.form['year']
    month = request.form['month']
    passengers = request.form['passengers']
   
    total = [year,month,passengers]
    print(total)
    #with graph.as_default():
    from sklearn.preprocessing import RobustScaler
    rs_pas = RobustScaler()
    y_predict = model.predict(np.array([[total]]))
    scaled_training=rs_pas.fit_transform(y_predict)
    print(scaled_training)
    y_pred=rs_pas.inverse_transform(scaled_training.reshape(1,-1))[0][0]*10
    print(y_pred)
    return render_template('index.html' ,display = str(round(y_pred)))

if __name__ == '__main__':
    app.run(debug=True)
    
    