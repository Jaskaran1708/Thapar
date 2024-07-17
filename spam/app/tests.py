import requests
import json
import uuid

BASE_URL = "http://127.0.0.1:8000" 

def register_user(username, password, phone_number, email):
    url = f"{BASE_URL}/users/"
    payload = {
        "username": username,
        "password": password,
        "phone_number": phone_number,
        "email": email
    }
    print(f"Registering user {username}")
    response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    print(f"Response: {response.status_code} - {response.text}")
    if response.status_code == 201:
        print("User registered successfully")
        return response.json()['id']
    else:
        print(f"Failed to register user: {response.status_code} - {response.text}")
        return None

def create_contact(name, phone_number, username_id):
    url = f"{BASE_URL}/contacts/"
    payload = {
        "name": name,
        "phone_number": phone_number,
        "username": username_id
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

def mark_spam(reporter, phone_number):
    url = f"{BASE_URL}/spamreports/"
    payload = {
        "reporter": reporter,
        "phone_number": phone_number,
        "message": "This number is spam"
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
    url = f"{BASE_URL}/search/name/{query}/"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        print("Search by name results:")
        for result in results:
            print(result)
    else:
        print(f"Failed to search by name: {response.status_code} - {response.text}")

def search_by_phone(phone_number):
    url = f"{BASE_URL}/search/number/{phone_number}/"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        print("Search by phone results:")
        for result in results:
            print(result)
    else:
        print(f"Failed to search by phone: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Generate unique credentials
    unique_id = uuid.uuid4()
    username = f"testuser_{unique_id}"
    password = "password123"
    email = f"testuser_{unique_id}@example.com"
    phone_number = f"{unique_id.int % 10000000000}"  # Ensure phone number is 10 digits
    contact_name = "John Doe"

    # Register a user
    user_id = register_user(username, password, phone_number, email)
    if user_id:
        # Create a contact for the user
        create_contact(contact_name, phone_number, user_id)
        
        # List all contacts
        list_contacts()
        
        # Mark a phone number as spam
        mark_spam(user_id, phone_number)  # Assuming the reporter user_id is the same user
        
        # Search by name
        search_by_name("John")
        
        # Search by phone number
        search_by_phone(phone_number)
