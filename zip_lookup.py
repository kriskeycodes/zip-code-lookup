import requests

def lookup_zip(zip_code):
    url = f"http://api.zippopotam.us/us/{zip_code}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data['places'][0]['place name']
            state = data['places'][0]['state']
            print(f"ZIP Code {zip_code} is in {city}, {state}")
        else:
            print(f"No city or state found for ZIP Code: {zip_code}")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to zip code service. Please check your internet connection.")


if __name__ == "__main__":
    print("--- Zip Code Lookup ---")
    print("Type a zip code to find its city, or 'exit' to stop.")
    
    while True:
        zip_code = input("Enter a ZIP code: ").strip()

        if zip_code.lower() == 'exit':
            print("Thank you for using the Zip Code Lookup! Goodbye.")
            break

        if zip_code.isdigit() and len(zip_code) == 5:
            lookup_zip(zip_code)
        else:
            print("Please enter a valid 5-digit ZIP code.")
