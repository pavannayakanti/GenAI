import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Hyderabad&BudgetMin=60-Lacs&BudgetMax=70-Lacs"

# Send a request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Function to extract property details
def extract_property_details(property_card):
    # Extract details from the property card
    title = property_card.find('span', class_='propTitle').text.strip()
    price = property_card.find('span', class_='price').text.strip()
    location = property_card.find('span', class_='locality').text.strip()
    details = property_card.find('div', class_='srpDataWrap').text.strip()
    
    return {
        'Title': title,
        'Price': price,
        'Location': location,
        'Details': details
    }

# Find all property cards
property_cards = soup.find_all('div', class_='m-srp-card')

# Extract details of each property
properties = [extract_property_details(card) for card in property_cards]

# Create a DataFrame
df = pd.DataFrame(properties)

# Save the DataFrame to an Excel sheet
df.to_excel('properties.xlsx', index=False)

print('Data has been saved to properties.xlsx')
