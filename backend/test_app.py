import pytest
from app import app as api
from app import Users  # Assuming Users is defined in app.py
from flask import json
from unittest.mock import patch

@pytest.fixture
def app():
    app = api
    app.config.update({
        "TESTING": True,
        "JWT_SECRET_KEY": "test-key",  # Set a test secret key
        # Configure your test database or other settings
    })
    print("ROUTES :::: ", app.url_map)
    # Setup test database, if necessary

    yield app

    # Teardown test database, if necessary

@pytest.fixture
def client(app):
    return app.test_client()

# @pytest.fixture
# def auth_token(app):
#     # Create a test user or mock user authentication
#     test_user = Users(email='test@example.com', password='testpassword')
    
#     # Add test_user to the database or mock the database interaction

#     # Generate a test token
#     with app.app_context():
#         from flask_jwt_extended import create_access_token
#         test_token = create_access_token(identity='test@example.com')
    
#     return test_token

# Test cases...

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Server up and running"}   

def test_register(client):
    response = client.post('/register', json={
        "email": "newuser@example.com",
        "password": "password",
        "firstName": "Test",
        "lastName": "User"
    })
    assert response.status_code == 200 or response.status_code == 400   

def test_create_token(client):
    response = client.post('/token', json={
        "email": "newuser@example.com",
        "password": "password"
    })
    # You need to adjust this based on the expected outcome
    assert response.status_code == 200 or response.status_code == 401 


def test_logout(client):
    # Assuming you have a way to authenticate, you need to add that here
    response = client.post('/logout')
    assert response.status_code == 200    


# Example test using the auth_token
@pytest.fixture
def auth_token(client):
    response = client.post('/token', json={
        'email': 'newuser@example.com',
        'password': 'password'
    })
    # Parse the response data to JSON and get the token
    data = json.loads(response.data)
    return data['access_token']

def test_get_data(client, auth_token):
    response = client.get(
        '/applications',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200

def test_add_application(client, auth_token):
    new_application = {
        "jobTitle": "Software Engineer",
        "companyName": "ExampleCorp",
        "date": "2023-01-15",
        "jobLink": "https://example.com/job/1",
        "location": "San Francisco, CA",
        "status": "1"
    }
    response = client.post(
        '/applications',
        headers={'Authorization': f'Bearer {auth_token}'},
        json=new_application
    )
    assert response.status_code == 200

def test_update_application(client, auth_token):
    updated_application = {
        "stage": "2"
    }
    application_id = 1  # Replace with a valid ID
    response = client.put(
        f'/applications/{application_id}',
        headers={'Authorization': f'Bearer {auth_token}'},
        json={'application': updated_application}
    )
    assert response.status_code == 200

def test_delete_application(client, auth_token):
    application_id = 1  # Replace with a valid ID
    response = client.delete(
        f'/applications/{application_id}',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200


def test_add_contact(client, auth_token):
    new_contact = {
        "firstName": "John",
        "lastName": "Doe",
        "jobTitle": "Developer",
        "companyName": "Tech Inc",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "linkedin": "linkedin.com/in/johndoe"
    }
    response = client.post(
        "/users/contacts",
        headers={'Authorization': f'Bearer {auth_token}'},
        json=new_contact
    )
    assert response.status_code == 200
    
    response_data = json.loads(response.data.decode('utf-8'))
    response_data.get("message", "")

def test_get_contacts(client, auth_token):
    response = client.get(
        "/users/contacts",
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200
    contacts = json.loads(response.data)["contacts"]
    assert isinstance(contacts, list)

def test_download_resume(client, auth_token):
    response = client.get(
        "/downloadresume",
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 400
    # The below will be for a case where the resume is actually uploaded
    # assert response.status_code == 200 
    # assert 'Content-Disposition' in response.headers
    # assert response.headers['Content-Disposition'] == 'attachment; filename=resume.pdf'

def test_get_dashboard_data(client,auth_token):
    response = client.get(
        "/dashboard",
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    data = response.get_json()
    # Assert the status code
    assert data["applications_created"] == 0
    assert data["interviews_completed"] == 0
    assert data["contacts_saved"] == 1
    assert isinstance(data["last_four_apps"], list)
    assert len(data["last_four_apps"]) == 0
    assert isinstance(data["job_applications_status"], list)
    assert len(data["job_applications_status"]) == 4
    assert isinstance(data["six_months_jobs_count"], list)
    assert len(data["six_months_jobs_count"]) == 6
    assert response.status_code == 200


def test_fetch_resume(client, auth_token):
    response = client.get(
        "/fetchresume",
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 500
    # assert response.headers['Content-Type'] == 'application/pdf'


if __name__ == '__main__':
    pytest.main()
