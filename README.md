# kidneydiseaseprediction

## Problem Statement:
    The healthcare industry is producing massive amounts of data which need to be mine to discover hidden information for effective prediction, exploration, diagnosis and decision making. Machine learning techniques can help and provides medication to handle this circumstances. Moreover, Chronic Kidney Disease prediction is one of the most central problems in medical decision making because it is one of the leading cause of death. So, automated tool for early prediction of this disease will be useful to cure. In this Project, the experiments were conducted for the prediction task of Chronic Kidney Disease using the machine learning algorithm

## Data Description:
I downloaded the dataset from the Kaggle named Chronic Kidney Disease. This dataset has 26 attributes. Total 400 instances of the dataset is used for the training to prediction algorithms, out of which 250 has label chronic kidney disease (CKD) and 150 has label non chronic kidney disease (NCKD)


#### Using the Columns :

       Id= id of the columns
       age= age of the person
       bp=blood_pressure
       sg=specific_gravity
       al=albumin
       su=sugar
       rbc=red_blood_cells
       pc=pus_cell
       pcc=pus_cell_clumps
       ba=bacteria
       bgr=blood_glucose_random
       bu=blood_urea
       sc=serum_creatinine
       sod=sodium
       pot=potassium
       hemo=haemoglobin
       pcv=packed_cell_volume
       wc=white_blood_cell_count
       rc=red_blood_cell_count
       htn=hypertension
       dm=diabetes_mellitus
       cad=coronary_artery_disease
       appet=appetite
       pe=peda_edema
       ane=aanemia


   #### target Variable
        classification    

## Tools / IDE
### IDE
We used Jupyter NoteBook for model training. And Vs Code for model deployment on the local system.

### Tools @ Libraries
      flask     
      matplotlib
      seaborn
      pandas
      numpy
      scikit_learn
      xgboost

## Data Preprocessing:
Before we could start building the model, we had to preprocess the data. This involved checking for missing values, removing any unnecessary features, and normalizing the data. We used pandas libraries to perform these tasks.

## Exploratory Data Analysis:
Next, we performed some exploratory data analysis to gain insights into the relationships between the different features and the target variable, i.e., Kidney disease prediction. We used the matplotlib and Seaborn libraries to visualize the data and understand any patterns or correlations in the dataset. We also computed some summary statistics to understand the central tendency and variability of the data.

## Model Building:
we started building the machine learning models. We trained and test various Machine Learning Models, logistic Regression, naive bayes classifier, Random Forest Classifier and Support vector Classification, XGBOOST. XGBOOST has highest Accuracy rate which is 97.5% ,so We choose to use a XGBOOST Machine Learning model to Predict the Kidney disease.

 
## Application Development
       1. Built a conda Environment
       2. Build the web app using Flask API
       3. Install the necessary dependencies and libraries
       4. Get the customer information from Web app
       5. Display the prediction
       6. Upload the project on GitHub
       7. Create a project image using Docker hub as Containerize the app
       
## Initialize the Git Repositry
         git init
         git add .
         git commit -m "first commit"
         git branch -M main
         git remote add origin <github_url>
         git push -u origin main 

 #### To update the modification or modification on github repositry
          git add .
          git commit -m "proper message"
          git push -u origin main   

## Create a file "Dockerfile" with below content
         FROM python:3.9
         COPY . /app
         WORKDIR /app
         RUN pip install -r requirements.txt
         ENTRYPOINT [ "python" ]
         CMD [ "app.py" ]    

## To Build the Docker Image on DockerHub
      docker build -t "docker_profile_name/app_name": latest .

### To run the container Image
      docker container run -d -p "port number:EX-5000" "docker_profile_name/app_name": latest

### To Upload the Docker Image on DockerHub
      docker push "docker_profile_name/app_name": latest

### Create a "Procfile" with following content
     web:gunicorn main:app

      

                     
        



