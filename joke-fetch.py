import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        joke = response.json()
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_general_joke():
    general_url = "https://official-joke-api.appspot.com/jokes/general/random"
    try:
        response = requests.get(general_url)
        response.raise_for_status()
        joke = response.json()[0]  # The API returns a list for category jokes
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_dad_joke():
    dad_url = "https://official-joke-api.appspot.com/jokes/dad/random"
    try:
        response = requests.get(dad_url)
        response.raise_for_status()
        joke = response.json()[0]  # The API returns a list for category jokes
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_knock_joke():
    knock_url = "https://official-joke-api.appspot.com/jokes/knock-knock/random"
    try:
        response = requests.get(knock_url)
        response.raise_for_status()
        joke = response.json()[0]  # The API returns a list for category jokes
        print(f"{joke['setup']}")
        print(f"{joke['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Select the type of joke you want:")
    print("1. Random Joke")
    print("2. General Joke")
    print("3. Dad Joke")
    print("4. Knock-Knock Joke")

    choice = input("Enter a number (1-4): ")

    if choice == "1":
        get_random_joke()
    elif choice == "2":
        get_general_joke()
    elif choice == "3":
        get_dad_joke()
    elif choice == "4":
        get_knock_joke()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")