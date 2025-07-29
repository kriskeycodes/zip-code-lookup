import requests

def lookup_zip(zip_code):
    url = f"http://api.zippopotam.us/us/{zip_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data['places'][0]['place name']
        state = data['places'][0]['state']
        print(f"ZIP Code {zip_code} is in {city}, {state}")
    else:
        print(f"No city or state found for ZIP Code: {zip_code}")

if __name__ == "__main__":
    while True:
        zip_code = input("Enter a ZIP code ").strip()
        if zip_code.lower() == 'exit':
            break
        if zip_code.isdigit() and len(zip_code) == 5:
            lookup_zip(zip_code)
        else:
            print("Please enter a valid 5-digit ZIP code.")
