import pickle
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
            - Diabetes
            - Heart Disease
            - Parkinson's Disease
            
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
