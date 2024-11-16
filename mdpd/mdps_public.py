import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import re

# Load saved models (adjust the paths based on your environment)
diabetes_model = pickle.load(open('mdpd/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('mdpd/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('mdpd/parkinsons_model.sav', 'rb'))

# Initialize session state keys
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'name' not in st.session_state:
    st.session_state.name = None
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Home"

# Function to validate email format (basic check for Gmail)
def validate_email(email):
    email = email.strip().lower()
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) and email.endswith("@gmail.com")

# Temporary "database" to store user credentials
users_db = {}

# Authentication functions
def authenticate(email, password):
    email = email.strip().lower()
    return email in users_db and users_db[email]["password"] == password

def signup(name, email, password):
    email = email.strip().lower()
    if email in users_db:
        return False
    users_db[email] = {"name": name, "password": password}
    return True

# Sidebar navigation
with st.sidebar:
    if not st.session_state.logged_in:
        selected = option_menu(
            "Predictive Disease Detection App",
            ["Login", "Signup"],
            icons=["key", "person-plus"],
            default_index=0
        )
    else:
        selected = option_menu(
            "Disease Prediction",
            ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "Logout"],
            icons=["activity", "heart", "person", "box-arrow-right"],
            default_index=0
        )

# Pages
if selected == "Signup":
    st.title("Signup Page")
    name = st.text_input('Full Name')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')

    if st.button('Create Account'):
        if not validate_email(email):
            st.error("Invalid Gmail address. Use an email ending with '@gmail.com'.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif signup(name, email, password):
            st.success(f"Account created for {name}!")
        else:
            st.error("Email already registered. Please log in.")

elif selected == "Login":
    st.title("Login Page")
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if not validate_email(email):
            st.error("Invalid Gmail address.")
        elif authenticate(email, password):
            st.session_state.logged_in = True
            st.session_state.user = email
            st.session_state.name = users_db[email]["name"]
            st.success(f"Welcome back, {st.session_state.name}!")
        else:
            st.error("Invalid email or password.")

elif selected == "Logout":
    st.session_state.clear()
    st.success("You have been logged out.")
    st.stop()

# Prediction Pages (visible after login)
if st.session_state.logged_in:
    st.title(f"Welcome, {st.session_state.name}")

    if selected == "Diabetes Prediction":
        st.header("Diabetes Prediction using ML")
        # Input fields
        patient_name = st.text_input("Patient Name")
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, value=0)
        Glucose = st.number_input("Glucose Level", min_value=0)
        BloodPressure = st.number_input("Blood Pressure", min_value=0)
        SkinThickness = st.number_input("Skin Thickness", min_value=0)
        Insulin = st.number_input("Insulin Level", min_value=0)
        BMI = st.number_input("BMI", min_value=0.0, format="%.2f")
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.2f")
        Age = st.number_input("Age", min_value=0)

        if st.button("Get Diabetes Prediction"):
            prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            result = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
            st.success(result)

    elif selected == "Heart Disease Prediction":
        st.header("Heart Disease Prediction using ML")
        # Input fields
        age = st.number_input("Age", min_value=0)
        sex = st.number_input("Sex (0 = Female, 1 = Male)", min_value=0, max_value=1)
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
        trestbps = st.number_input("Resting Blood Pressure", min_value=0)
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0)
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)", min_value=0, max_value=1)
        restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2)
        thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
        exang = st.number_input("Exercise Induced Angina (1 = Yes, 0 = No)", min_value=0, max_value=1)
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, format="%.2f")
        slope = st.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2)
        ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3)
        thal = st.number_input("Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)", min_value=0, max_value=2)

        if st.button("Get Heart Disease Prediction"):
            prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            result = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
            st.success(result)

    elif selected == "Parkinson's Prediction":
        st.header("Parkinson's Disease Prediction using ML")
        # Input fields
        fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, format="%.2f")
        fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0, format="%.2f")
        flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0, format="%.2f")
        Jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, format="%.2f")
        Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, format="%.6f")
        RAP = st.number_input("MDVP:RAP", min_value=0.0, format="%.6f")
        PPQ = st.number_input("MDVP:PPQ", min_value=0.0, format="%.6f")
        DDP = st.number_input("Jitter:DDP", min_value=0.0, format="%.6f")
        Shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, format="%.6f")
        Shimmer_dB = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, format="%.2f")

        if st.button("Get Parkinson's Prediction"):
            prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB]])
            result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(result)
