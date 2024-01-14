from wsgiref import simple_server
from flask import Flask, request, app, render_template
from flask import Response
from flask_cors import CORS 
import pickle
import os
import bz2
import numpy as np
import pandas as pd
from joblib import load



app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

scalerobject=bz2.BZ2File("Models\kidney_standardScalar.pkl", "rb")
scaler=pickle.load(scalerobject)
modelforpred=bz2.BZ2File("Models\XGB_ModelForPrediction.pkl", "rb")
model=pickle.load(modelforpred)

#scaler=pickle.load(open("Model\standardScalar.pkl", "rb"))
#model=pickle.load(open("Model\trainedmodelrfc.pkl", "rb"))


#try:
#scaler = load("Models/kidney_standardScalar.pkl")
    # Use the scaler object
    #print("Scaler loaded successfully.")
#except Exception as e:
    #print(f"Error loading scaler: {e}")

#try:
#model=load("Models/RandomFC_ModelForPrediction.pkl")
       #use the model object
    #print("Model loaded succesfully")
#except Exception as e:
    #print(f"Error loading model: {e}")




#Route for homepage

@app.route('/')
def index():
    return render_template('index.html')


#Route for Single data point prediction
@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    result=""
   
    if request.method=='POST':
        
            

            age=request.form.get("age")
            blood_pressure=(request.form.get("blood_pressure"))
            specific_gravity=(request.form.get("specific_gravity"))
            albumin=(request.form.get("albumin"))
            sugar=(request.form.get("sugar"))
            red_blood_cells=(request.form.get("red_blood_cells"))
            pus_cell = (request.form.get("pus_cell"))
            pus_cell_clumps = (request.form.get("pus_cell_clumps"))
            bacteria = (request.form.get("bacteria"))
            blood_glucose_random = (request.form.get("blood_glucose_random"))
            blood_urea = (request.form.get("blood_urea"))
            serum_creatinine = (request.form.get("serum_creatinine"))
            sodium = (request.form.get("sodium"))
            potassium = (request.form.get("potassium"))
            haemoglobin = (request.form.get("haemoglobin"))
            packed_cell_volume = int(request.form.get("packed_cell_volume"))
            white_blood_cell_count = int(request.form.get("white_blood_cell_count"))
            red_blood_cell_count = int(request.form.get("red_blood_cell_count"))
            hypertension = int(request.form.get("hypertension"))
            diabetes_mellitus = int(request.form.get("diabetes_mellitus"))
            coronary_artery_disease = int(request.form.get("coronary_artery_disease"))
            appetite = int(request.form.get("appetite"))
            peda_edema	 = int(request.form.get("peda_edema"))
            aanemia = int(request.form.get("aanemia"))

        
            new_data=scaler.transform([[age,blood_pressure,specific_gravity,albumin,sugar,red_blood_cells,pus_cell,
                                    pus_cell_clumps,bacteria,blood_glucose_random,blood_urea,serum_creatinine,
                                    sodium,potassium,haemoglobin,packed_cell_volume,white_blood_cell_count,red_blood_cell_count,
                                    hypertension,diabetes_mellitus,coronary_artery_disease,appetite,peda_edema,aanemia]])
            predict=model.predict(new_data)

            if predict[0]==1:
                result ='Person is not Healthy as suffering with Kidney Disease'
                
            else:
                result='Person is Healthy, Do not have Kidney Disease'
        
            return render_template('result.html', result=result)
       
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)                  



            