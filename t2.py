import requests
import pandas as pd

# Define the correct API endpoint (Replace with actual endpoint)
api_url = "https://www.iedb.org/api/your_correct_endpoint"  # Update this URL
params = {
    "limit": 100,  # Number of samples to retrieve
    "format": "json"
}

# Send a GET request to the IEDB API
try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes

    # Check if the response content is as expected
    if response.status_code == 200:
        data = response.json()
        epitopes = data.get('results', [])  # Adjust based on actual response structure

        # Convert to DataFrame for easier handling
        if epitopes:
            df = pd.DataFrame(epitopes)
            print(df.head())

            # Save to CSV file
            df.to_csv('iedb_epitopes.csv', index=False)
        else:
            print("No data found.")
    else:
        print(f"Received unexpected status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
