 import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load saved models
diabetes_model = pickle.load(open('mdpd/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('mdpd/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('mdpd/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Predictive Disease Detection App',
                          ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                          icons=['activity', 'heart', 'person'],
                          default_index=0)

# Home Page
if selected == "Home":
    st.title("Welcome to Predictive Disease Detection App")
    st.write("""
    This application uses machine learning to predict the likelihood of the following diseases:
    - Diabetes
    - Heart Disease
    - Parkinson's Disease
    
    Select a disease prediction option from the sidebar to get started.
    """)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields for user data
    patient_name = st.text_input('Patient Name')
    age = st.number_input('Age of the Person', min_value=0)
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    Glucose = st.number_input('Glucose Level', min_value=0)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0)
    SkinThickness = st.number_input('Skin Thickness value', min_value=0)
    Insulin = st.number_input('Insulin Level', min_value=0)
    BMI = st.number_input('BMI value', min_value=0.0, format="%.2f")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.2f")

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
        st.success(f"Patient: {patient_name}, Age: {age}, Result: {diab_diagnosis}")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Input fields for user data
    age = st.number_input('Age')
    sex = st.number_input('Sex')
    cp = st.number_input('Chest Pain types')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Serum Cholestoral in mg/dl')
    fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.number_input('Resting Electrocardiographic results')
    thalach = st.number_input('Maximum Heart Rate achieved')
    exang = st.number_input('Exercise Induced Angina')
    oldpeak = st.number_input('ST depression induced by exercise')
    slope = st.number_input('Slope of the peak exercise ST segment')
    ca = st.number_input('Major vessels colored by flourosopy')
    thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]) 
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(f"Patient: {age}, Result: {heart_diagnosis}")

# Parkinson's Disease Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields for user data
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')

    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]) 
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
        st.success(f"Patient: {fo}, Result: {parkinsons_diagnosis}")

