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

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "name" not in st.session_state:
    st.session_state.name = None
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

# Sidebar for navigation
with st.sidebar:
    if not st.session_state.logged_in:
        selected = option_menu(
            "Predictive Disease Detection App",
            ["Login", "Signup"],
            icons=["key", "person-plus"],
            default_index=0,
        )
    else:
        selected = option_menu(
            "Predictive Disease Detection App",
            [
                "Home",
                "Diabetes Prediction",
                "Heart Disease Prediction",
                "Parkinsons Prediction",
                "Logout",
            ],
            icons=["house", "activity", "heart", "person", "box-arrow-right"],
            default_index=0,
        )

# Handle Logout separately
if selected == "Logout":
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.name = None
    st.session_state.selected_page = "Home"
    st.success("You have been logged out.")
    st.stop()

# Signup Page
if selected == "Signup":
    st.title("Signup Page")

    # Signup form fields
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):
        # Validate email and password
        if not validate_email(email):
            st.error("Please enter a valid Gmail address (e.g., example@gmail.com).")
        elif password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif signup(name, email, password):
            st.success(f"Account created successfully for {name}!")
            st.session_state.logged_in = True
            st.session_state.user = email
            st.session_state.name = name
            st.session_state.selected_page = "Home"
        else:
            st.error("This email is already registered. Please login.")

# Login Page
elif selected == "Login":
    st.title("Login Page")

    # Login form fields
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Validate email and password
        if not validate_email(email):
            st.error("Please enter a valid Gmail address (e.g., example@gmail.com).")
        elif authenticate(email, password):
            st.session_state.logged_in = True
            st.session_state.user = email
            st.session_state.name = users_db[email]["name"]
            st.session_state.selected_page = "Home"
            st.success("Login successful!")
        else:
            st.error("Invalid email or password. Please try again.")

# Disease Prediction Pages (visible after successful login)
if st.session_state.logged_in:
    if selected == "Home":
        st.title("Welcome to Predictive Disease Detection App")
        st.write(
            """
            This application uses machine learning to predict the likelihood of the following diseases:
            - *Diabetes*
            - *Heart Disease*
            - *Parkinson's Disease*
            
            Select a disease prediction option from the sidebar to get started.
            """
        )

    elif selected == "Diabetes Prediction":
        st.title("Diabetes Prediction using ML")

        # Input fields
        patient_name = st.text_input("Patient Name")
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
        Glucose = st.number_input("Glucose Level", min_value=0)
        BloodPressure = st.number_input("Blood Pressure value", min_value=0)
        SkinThickness = st.number_input("Skin Thickness value", min_value=0)
        Insulin = st.number_input("Insulin Level", min_value=0)
        BMI = st.number_input("BMI value", min_value=0.0, format="%.2f")
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value", min_value=0.0, format="%.2f")
        Age = st.number_input("Age of the Person", min_value=0)

        if st.button("Diabetes Test Result"):
            diab_prediction = diabetes_model.predict(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            )
            result = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
            st.success(result)

# Add similar sections for "Heart Disease Prediction" and "Parkinsons Prediction"
"""
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

