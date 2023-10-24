

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('Models/diabetes.pkl', 'rb'))

heart_disease_model = pickle.load(open('Models/heart.pkl', 'rb'))

BreastCancer_model = pickle.load(open('Models/Breastcancer.pkl', 'rb'))

liver_model = pickle.load(open('Models/liver.pkl', 'rb'))

parkinsons_model = pickle.load(open('Models/parkinsons_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Prediction',
                           'Liver Disease Prediction',
                           'Parkinsons Prediction'],
                          default_index=0)
    
 # Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
   
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    






# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        radius_mean = st.text_input('Radius Mean')
        
    with col2:
        texture_mean = st.text_input('Texture Mean')
        
    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')
        
    with col1:
        area_mean = st.text_input('Area Mean')
        
    with col2:
        smoothness_mean = st.text_input('Smoothness Mean')
        
    with col3:
        compactness_mean = st.text_input('Compactness Mean')
        
    with col1:
        concavity_mean = st.text_input('Concavity Mean')
        
    with col2:
        concave_points_mean = st.text_input('Concave Points Mean')
        
    with col3:
        symmetry_mean = st.text_input('Symmetry Mean')
        
    with col1:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')
        
    with col2:
        radius_se = st.text_input('Radius SE')
        
    with col3:
        texture_se = st.text_input('Texture SE')
        
    with col1:
        perimeter_se = st.text_input('Perimeter SE')
        
    with col2:
        area_se = st.text_input('Area SE')
        
    with col3:
        smoothness_se = st.text_input('Smoothness SE')
        
    with col1:
        compactness_se = st.text_input('Compactness SE')
        
    with col2:
        concavity_se = st.text_input('Concavity SE')
        
    with col3:
        concave_points_se = st.text_input('Concave Points SE')
        
    with col1:
        symmetry_se = st.text_input('Symmetry SE')
        
    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')
        
    with col3:
        radius_worst = st.text_input('Radius Worst')
        
    with col1:
        texture_worst = st.text_input('Texture Worst')
        
    with col2:
        perimeter_worst = st.text_input('Perimeter Worst')
        
    with col3:
        area_worst = st.text_input('Area Worst')
        
    with col1:
        smoothness_worst = st.text_input('Smoothness Worst')
        
    with col2:
        compactness_worst = st.text_input('Compactness Worst')
        
    with col3:
        concavity_worst = st.text_input('Concavity Worst')
        
    with col1:
        concave_points_worst = st.text_input('Concave Points Worst')
        
    with col2:
        symmetry_worst = st.text_input('Symmetry Worst')
        
    with col3:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')
        
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = BreastCancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])  
        
        if (breast_cancer_prediction[0] == 1):
            breast_cancer_diagnosis = 'The person has breast cancer'
        else:
            breast_cancer_diagnosis = 'The person does not have breast cancer'
        
    st.success(breast_cancer_diagnosis)



# Liver Disease Prediction Page
if (selected == 'Liver Disease Prediction'):
    
    # page title
    st.title('Liver Disease Prediction using ML')
    
   

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        gender = st.text_input('Gender')
        
    with col3:
        total_bilirubin = st.text_input('Total Bilirubin')
        
    with col1:
        direct_bilirubin = st.text_input('Direct Bilirubin')
        
    with col2:
        alkaline_phosphotase = st.text_input('Alkaline Phosphotase')
        
    with col3:
        alamine_aminotransferase = st.text_input('Alamine Aminotransferase')
        
    with col1:
        aspartate_aminotransferase = st.text_input('Aspartate Aminotransferase')
        
    with col2:
        total_protiens = st.text_input('Total Protiens')
        
    with col3:
        albumin = st.text_input('Albumin')
        
    with col1:
        albumin_globulin_ratio = st.text_input('Albumin and Globulin Ratio')
        
    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button('Liver Disease Test Result'):
        liver_prediction = liver_model.predict([[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase, aspartate_aminotransferase, total_protiens, albumin, albumin_globulin_ratio]])  
        
        if (liver_prediction[0] == 1):
            liver_diagnosis = 'The person has liver disease'
        else:
            liver_diagnosis = 'The person does not have liver disease'
        
    st.success(liver_diagnosis)














