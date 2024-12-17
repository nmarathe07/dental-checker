import streamlit as st
import pandas as pd

# Load the CSV data
file_path = 'dental-data.csv'
data = pd.read_csv(file_path)

# Symptom Checker Function
def symptom_checker(symptom):
    result = data[data['Symptom'].str.lower().str.contains(symptom.lower(), na=False)]
    if not result.empty:
        response = "Here are the matches we found:\n\n"
        for _, row in result.iterrows():
            response += f"**Symptom:** {row['Symptom']}\n**Condition:** {row['Condition']}\n**Urgency:** {row['Urgency']}\n**Prevention:** {row['Prevention']}\n\n"
        return response
    else:
        return "Sorry, we couldn't find a match for that symptom. Please try again."

# Streamlit Interface
st.title("Dental Symptom Checker")
st.write("Enter a symptom to find possible conditions and their urgency levels.")

# Input box
user_symptom = st.text_input("Enter your symptom:")

# Check symptom and display result
if st.button("Check Condition"):
    if user_symptom:
        result = symptom_checker(user_symptom)
        st.markdown(result)
    else:
        st.warning("Please enter a symptom!")

