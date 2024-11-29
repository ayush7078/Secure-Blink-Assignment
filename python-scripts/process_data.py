import os
import pandas as pd
import requests

# Load the dataset
dataset_path = './data/data.csv'
data = pd.read_csv(dataset_path)

# 1. Data Cleaning: Handle missing values and remove duplicates
# Fill missing values with appropriate strategies (mean, median, etc.)
data['age'] = data['age'].fillna(data['age'].mean())  # Fix inplace warning
data['salary'] = data['salary'].fillna(data['salary'].median())  # Fix inplace warning

# Remove duplicate rows
data.drop_duplicates(inplace=True)

# 2. Data Transformation: Normalize salary and age
data['normalized_salary'] = (data['salary'] - data['salary'].min()) / \
                             (data['salary'].max() - data['salary'].min())

data['normalized_age'] = (data['age'] - data['age'].min()) / \
                         (data['age'].max() - data['age'].min())

# 3. Data Analysis: Compute statistics for salary and age
data_analysis = {
    'mean_salary': data['salary'].mean(),
    'median_salary': data['salary'].median(),
    'mean_age': data['age'].mean(),
    'median_age': data['age'].median()
}

# 4. Send the processed data to Express.js API
def send_data_to_api(data):
    url = os.getenv('API_URL', 'http://localhost:6000/api/data')  # Express API URL
    try:
        response = requests.post(url, json=data.to_dict(orient='records'))
        if response.status_code == 200:
            print("Data sent successfully to API")
        else:
            print(f"Error sending data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Send processed data to API
send_data_to_api(data)

# Print the analysis results
print("Data Analysis Results:")
print(data_analysis)
