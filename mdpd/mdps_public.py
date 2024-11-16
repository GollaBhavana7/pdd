import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Load pre-trained models
diabetes_model = pickle.load(open('mdpd/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('mdpd/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('mdpd/parkinsons_model.sav', 'rb'))

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Multiple Disease Prediction System",
        options=["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["house", "activity", "heart", "person"],
        default_index=0
    )

# Home Page
if selected == "Home":
    st.title("Welcome to the Multiple Disease Prediction System")
    st.write("""
    This application uses machine learning to predict the likelihood of the following diseases:
    - **Diabetes**
    - **Heart Disease**
    - **Parkinson's Disease**
    
    Select a disease prediction option from the sidebar to get started.
    """)

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")

    # Input fields for user data
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness (mm)', min_value=0.0)
        Age = st.number_input('Age', min_value=0, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0.0)
        Insulin = st.number_input('Insulin Level (µU/mL)', min_value=0.0)
        BMI = st.number_input('Body Mass Index (BMI)', min_value=0.0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure (mmHg)', min_value=0.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0)

    # Predict and display results
    if st.button("Get Diabetes Prediction"):
        features = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = diabetes_model.predict(features)
        result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
        st.success(f"The prediction is: **{result}**")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    # Input fields for user data
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=0, step=1)
        trestbps = st.number_input('Resting Blood Pressure (mmHg)', min_value=0.0)
        thalach = st.number_input('Max Heart Rate Achieved', min_value=0.0)
    with col2:
        sex = st.selectbox('Sex', options=["Male", "Female"], index=0)
        chol = st.number_input('Serum Cholesterol (mg/dL)', min_value=0.0)
        oldpeak = st.number_input('ST Depression (Oldpeak)', min_value=0.0)
    with col3:
        cp = st.selectbox('Chest Pain Type', options=["Type 0", "Type 1", "Type 2", "Type 3"], index=0)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', options=["No", "Yes"], index=0)
        exang = st.selectbox('Exercise Induced Angina', options=["No", "Yes"], index=0)

    # Mapping inputs to numeric
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0

    # Predict and display results
    if st.button("Get Heart Disease Prediction"):
        features = np.array([[age, sex, cp, trestbps, chol, fbs, thalach, exang, oldpeak]])
        prediction = heart_disease_model.predict(features)
        result = "Heart Disease Present" if prediction[0] == 1 else "No Heart Disease"
        st.success(f"The prediction is: **{result}**")

# Parkinson's Disease Prediction Page
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction")

    # Input fields for user data
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
        Jitter_percent = st.number_input('Jitter(%)', min_value=0.0)
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
        Jitter_Abs = st.number_input('Jitter(Abs)', min_value=0.0)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
        Shimmer = st.number_input('Shimmer', min_value=0.0)
    with col4:
        RAP = st.number_input('MDVP:RAP', min_value=0.0)
        Shimmer_dB = st.number_input('Shimmer(dB)', min_value=0.0)

    # Predict and display results
    if st.button("Get Parkinson's Prediction"):
        features = np.array([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, Shimmer, Shimmer_dB]])
        prediction = parkinsons_model.predict(features)
        result = "Parkinson's Disease Detected" if prediction[0] == 1 else "No Parkinson's Disease"
        st.success(f"The prediction is: **{result}**")
