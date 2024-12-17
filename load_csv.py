import pandas as pd

# Path to your CSV file (update this if your file is in another folder)
file_path = 'dental-data.csv'

# Load the CSV into a DataFrame
data = pd.read_csv(file_path)

# Preview the data
print("Here is your data:")
print(data.head())

# Symptom Checker Function
def symptom_checker(symptom):
    # Check if the symptom exists in the data
    result = data[data['Symptom'].str.lower().str.contains(symptom.lower(), na=False)]
    if not result.empty:
        # Return all matching conditions and urgency levels
        response = "Here are the matches we found:\n"
        for _, row in result.iterrows():
            response += f"Symptom: {row['Symptom']}\nCondition: {row['Condition']}\nUrgency: {row['Urgency']}\n\n"
        return response
    else:
        return "Sorry, we couldn't find a match for that symptom. Please try again."


# Ask the user for input
user_symptom = input("Enter your symptom: ")
print(symptom_checker(user_symptom))
