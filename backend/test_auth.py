#!/usr/bin/env python3
"""
Test script to check the auth functionality
"""
import requests
import json

# Test the registration endpoint
def test_registration():
    url = "http://localhost:8000/api/v1/auth/register"

    payload = {
        "email": "test@example.com",
        "password": "password123"
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code != 200:
            print("Error occurred during registration")
        else:
            print("Registration successful")
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

if __name__ == "__main__":
    test_registration()