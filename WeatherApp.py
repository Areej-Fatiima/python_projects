import requests

# Replace with your Weatherbit API key
API_KEY = 'c0b8ddb28bbd425a9d3a6524825185f1'
BASE_URL = 'https://api.weatherbit.io/v2.0/current'

def get_weather(city):
    # Construct the URL
    url = f'{BASE_URL}?city={city}&key={API_KEY}&units=metric'
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON data
            data = response.json()
            
            # Extract relevant information
            city_name = data['data'][0]['city_name']
            temperature = data['data'][0]['temp']
            weather_description = data['data'][0]['weather']['description']
            
            # Display the weather information
            print(f'City: {city_name}')
            print(f'Temperature: {temperature}°C')
            print(f'Weather: {weather_description.capitalize()}')
        except ValueError:
            print('Error decoding JSON response.')
    else:
        print(f'Error: {response.status_code}')
        print(f'Message: {response.json().get("error", "No message available")}')

def main():
    city = input('Enter city name: ')
    get_weather(city)

if __name__ == '__main__':
    main()
