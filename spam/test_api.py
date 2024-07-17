import requests
import json

BASE_URL = "http://127.0.0.1:8000/app"

def register_user(username, password, email):
    url = f"{BASE_URL}/users/"
    payload = {
        "username": username,
        "password": password,
        "email": email
    }
    response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    if response.status_code == 201:
        print("User registered successfully")
    else:
        print(f"Failed to register user: {response.status_code} - {response.text}")

def create_contact(name, phone_number):
    url = f"{BASE_URL}/contacts/"
    payload = {
        "name": name,
        "phone_number": phone_number
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 201:
        print("Contact created successfully")
    else:
        print(f"Failed to create contact: {response.status_code} - {response.text}")

def list_contacts():
    url = f"{BASE_URL}/contacts/"
    response = requests.get(url)
    if response.status_code == 200:
        contacts = response.json()
        print("Contacts retrieved successfully")
        for contact in contacts:
            print(contact)
    else:
        print(f"Failed to retrieve contacts: {response.status_code} - {response.text}")

def mark_spam(phone_number):
    url = f"{BASE_URL}/spamreports/"
    payload = {
        "phone_number": phone_number
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 201:
        print("Spam report created successfully")
    else:
        print(f"Failed to create spam report: {response.status_code} - {response.text}")

def search_by_name(query):
    url = f"{BASE_URL}/search/name/"
    params = {"q": query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        print("Search by name results:")
        for result in results:
            print(result)
    else:
        print(f"Failed to search by name: {response.status_code} - {response.text}")

def search_by_phone(phone_number):
    url = f"{BASE_URL}/search/phone/"
    params = {"q": phone_number}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        print("Search by phone results:")
        for result in results:
            print(result)
    else:
        print(f"Failed to search by phone: {response.status_code} - {response.text}")

if __name__ == "__main__":
    username = "testuser"
    password = "password123"
    email = "testuser@example.com"
    phone_number = "1234567890"
    contact_name = "John Doe"

    register_user(username, password, email)
    create_contact(contact_name, phone_number)
    list_contacts()
    mark_spam(phone_number)
    search_by_name("John")
    search_by_phone(phone_number)
