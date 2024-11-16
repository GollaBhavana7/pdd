
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('mdpd/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('mdpd/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('mdpd/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Predictive Disease Detection App',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
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
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

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
    """

"""import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import re

# Load saved models (adjust the paths based on your environment)
diabetes_model = pickle.load(open('mdpd/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('mdpd/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('mdpd/parkinsons_model.sav', 'rb'))

# Dictionary to store user data temporarily (for simplicity)
users_db = {}

# Function to validate email format (checks for basic email structure and @gmail.com)
def validate_email(email):
    email = email.strip().lower()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    if not email.endswith("@gmail.com"):
        return False
    return True

# Function to authenticate login
def authenticate(email, password):
    email = email.strip().lower()
    if email in users_db and users_db[email]["password"] == password:
        return True
    else:
        return False

# Function to register a new user (Signup)
def signup(name, email, password):
    email = email.strip().lower()
    if email in users_db:
        return False  # Email already exists
    # Save user details in the "database"
    users_db[email] = {"name": name, "password": password}
    return True

# Sidebar for navigation
with st.sidebar:
    if 'logged_in' not in st.session_state or not st.session_state.logged_in:
        selected = option_menu("Predictive Disease Detection App", ["Login", "Signup"], icons=["key", "person-plus"], default_index=0)
    else:
        selected = option_menu('Predictive Disease Detection App',
                               ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Prediction'],
                               icons=['activity', 'heart', 'person'],
                               default_index=0)

# Signup Page
if selected == "Signup":
    st.title("Signup Page")

    # Signup form fields
    name = st.text_input('Full Name')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')

    if st.button('Create Account'):
        # Validate email and password
        if not validate_email(email):
            st.error("Please enter a valid Gmail address (e.g., example@gmail.com).")
        elif password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif signup(name, email, password):
            st.success(f"Account created successfully for {name}!")
            # Set login state
            st.session_state.logged_in = True
            st.session_state.user = email
            st.session_state.name = name
            st.session_state.selected_page = "Diabetes Prediction"  # Default page after signup
        else:
            st.error("This email is already registered. Please login.")

# Login Page
elif selected == "Login":
    st.title("Login Page")

    # Login form fields
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        # Validate email and password
        if not validate_email(email):
            st.error("Please enter a valid Gmail address (e.g., example@gmail.com).")
        elif authenticate(email, password):
            st.session_state.logged_in = True
            st.session_state.user = email
            st.session_state.name = users_db[email]["name"]
            st.session_state.selected_page = "Diabetes Prediction"  # Default page after login
            st.success('Login successful!')
        else:
            st.error('Invalid email or password. Please try again.')

# Disease Prediction Pages (visible after successful login)
if 'logged_in' in st.session_state and st.session_state.logged_in:
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Diabetes Prediction'  # Default page when logged in

    selected_page = st.session_state.selected_page

    # Sidebar to select prediction type
    with st.sidebar:
        selected_page = option_menu('Disease Prediction',
                                    ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                                    icons=['activity', 'heart', 'person'],
                                    default_index=0)
        st.session_state.selected_page = selected_page

    if selected_page == 'Diabetes Prediction':
        st.title('Diabetes Prediction using ML')

        # Get patient details
        patient_name = st.text_input('Patient Name')
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

        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            # Display patient details and prediction result
            st.subheader('Patient Information:')
            st.write(f"Name: {patient_name}")
            st.write(f"Age: {Age}")
            st.write(f"Prediction: {diab_diagnosis}")
    
    elif selected_page == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction using ML')
        
        # Get patient details
        patient_name = st.text_input('Patient Name')
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age')
        with col2:
            sex = st.number_input('Sex')
        with col3:
            cp = st.number_input('Chest Pain types')
        with col1:
            trestbps = st.number_input('Resting Blood Pressure')
        with col2:
            chol = st.number_input('Serum Cholestoral in mg/dl')
        with col3:
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.number_input('Resting Electrocardiographic results')
        with col2:
            thalach = st.number_input('Maximum Heart Rate achieved')
        with col3:
            exang = st.number_input('Exercise Induced Angina')
        with col1:
            oldpeak = st.number_input('ST depression induced by exercise')
        with col2:
            slope = st.number_input('Slope of the peak exercise ST segment')
        with col3:
            ca = st.number_input('Major vessels colored by flourosopy')
        with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            # Display patient details and prediction result
            st.subheader('Patient Information:')
            st.write(f"Name: {patient_name}")
            st.write(f"Age: {age}")
            st.write(f"Sex: {sex}")
            st.write(f"Prediction: {heart_diagnosis}")
    
    elif selected_page == "Parkinson's Prediction":
        st.title("Parkinson's Disease Prediction using ML")

        # Get patient details
        patient_name = st.text_input('Patient Name')
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

        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB]])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            # Display patient details and prediction result
            st.subheader('Patient Information:')
            st.write(f"Name: {patient_name}")
            st.write(f"Prediction: {parkinsons_diagnosis}")

# Logout button to end session
if st.button('Logout'):
    st.session_state.logged_in = False
    st.session_state.clear()
    st.experimental_rerun()
 
"""
import streamlit as st
import numpy as np
import pickle

# Load pre-trained models
diabetes_model = pickle.load(open('mdpd/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('mdpd/heart_disease_model.sav', 'rb'))

# App title
st.title("Multiple Disease Prediction System")

# Sidebar navigation
st.sidebar.title("Navigation")
selected = st.sidebar.selectbox("Choose Disease Prediction:", ["Home", "Diabetes Prediction", "Heart Disease Prediction"])

# Home page
if selected == "Home":
    st.write("""
        ## Welcome to the Multiple Disease Prediction System
        Choose a disease prediction option from the sidebar.
    """)

# Diabetes Prediction Page
elif selected == "Diabetes Prediction":
    st.header("Diabetes Prediction")

    # Input fields for diabetes prediction
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0.0)
    blood_pressure = st.number_input("Blood Pressure Level", min_value=0.0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
    insulin = st.number_input("Insulin Level", min_value=0.0)
    bmi = st.number_input("BMI", min_value=0.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0, step=1)

    # Predict diabetes
    if st.button("Predict Diabetes"):
        features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        result = diabetes_model.predict(features)
        st.success(f"Diabetes Prediction: {'Positive' if result[0] == 1 else 'Negative'}")

# Heart Disease Prediction Page
elif selected == "Heart Disease Prediction":
    st.header("Heart Disease Prediction")

    # Input fields for heart disease prediction
    age = st.number_input("Age", min_value=0, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain = st.number_input("Chest Pain Type (1-4)", min_value=1, max_value=4, step=1)
    resting_bp = st.number_input("Resting Blood Pressure", min_value=0.0)
    cholesterol = st.number_input("Cholesterol Level", min_value=0.0)
    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    resting_ecg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2, step=1)
    max_heart_rate = st.number_input("Maximum Heart Rate Achieved", min_value=0.0)
    exercise_angina = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak (ST Depression Induced by Exercise)", min_value=0.0)
    slope = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", min_value=0, max_value=2, step=1)
    major_vessels = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", min_value=0, max_value=3, step=1)
    thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", [1, 2, 3])

    # Map categorical inputs
    sex = 1 if sex == "Male" else 0
    fasting_blood_sugar = 1 if fasting_blood_sugar == "Yes" else 0
    exercise_angina = 1 if exercise_angina == "Yes" else 0

    # Predict heart disease
    if st.button("Predict Heart Disease"):
        features = np.array([[age, sex, chest_pain, resting_bp, cholesterol, fasting_blood_sugar, resting_ecg,
                              max_heart_rate, exercise_angina, oldpeak, slope, major_vessels, thal]])
        result = heart_disease_model.predict(features)
        st.success(f"Heart Disease Prediction: {'Positive' if result[0] == 1 else 'Negative'}")
