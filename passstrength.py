import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Use a special character (!@#$%^&*).")

    strength_labels = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return strength_labels.get(strength, "Very Weak"), remarks

# Streamlit UI
st.title("Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    st.subheader(f"Password Strength: {strength}")
    
    if feedback:
        st.warning("\n".join(feedback))
    else:
        st.success("Great password!")

