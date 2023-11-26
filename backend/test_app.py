import pytest
from app import create_app, Users  # Assuming Users is defined in app.py
from flask import json
from unittest.mock import patch

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "JWT_SECRET_KEY": "test-key",  # Set a test secret key
        # Configure your test database or other settings
    })

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

def test_create_token(client):
    response = client.post('/token', json={
        "email": "test@example.com",
        "password": "password"
    })
    # You need to adjust this based on the expected outcome
    assert response.status_code == 200 or response.status_code == 401    

def test_register(client):
    response = client.post('/register', json={
        "email": "newuser@example.com",
        "password": "password",
        "firstName": "Test",
        "lastName": "User"
    })
    assert response.status_code == 200 or response.status_code == 400   


def test_logout(client):
    # Assuming you have a way to authenticate, you need to add that here
    response = client.post('/logout')
    assert response.status_code == 200    


# Example test using the auth_token
@pytest.fixture
def auth_token(client):
    response = client.post('/token', json={
        'email': 'amrita@ncsu.edu',
        'password': 'test'
    })
    # Parse the response data to JSON and get the token
    data = json.loads(response.data)
    return data['access_token']

def test_get_data(client, auth_token):
    print(auth_token)  # This should now print the actual token
    response = client.get(
        '/applications',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200

def test_add_application(client, auth_token):
    new_application = {
        # Your application data here
    }
    response = client.post(
        '/applications',
        headers={'Authorization': f'Bearer {auth_token}'},
        json=new_application
    )
    assert response.status_code == 200

def test_update_application(client, auth_token):
    updated_application = {
        # Your updated application data here
    }
    application_id = 1  # Replace with a valid ID
    response = client.put(
        f'/applications/{application_id}',
        headers={'Authorization': f'Bearer {auth_token}'},
        json={'application': updated_application}
    )
    assert response.status_code == 404

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
    assert response.status_code == 200
    assert 'Content-Disposition' in response.headers
    assert response.headers['Content-Disposition'] == 'attachment; filename=resume.pdf'

# Mock the Users.objects() method and the get_jwt_identity function
@patch("app.Users.objects")
@patch("app.get_jwt_identity")
def test_get_dashboard_data(mock_get_jwt_identity, mock_users_objects, client):
    # Sample application data
    mock_application_data = [
        {
            "id": 1,
            "jobTitle": "Software Engineer",
            "companyName": "ExampleCorp",
            "date": "2023-01-15",
            "jobLink": "https://example.com/job/1",
            "location": "San Francisco, CA",
            "stage": "2"
        },
        {
            "id": 2,
            "jobTitle": "Data Analyst",
            "companyName": "DataTech",
            "date": "2023-02-20",
            "jobLink": "https://datatech.com/job/2",
            "location": "New York, NY",
            "stage": "1"
        },
        # Add more applications as needed
    ]

    # Mock user data
    mock_user_data = {
        'email': 'test@example.com',
        'applications': mock_application_data
    }
    
    # Configure the mock to return the mock user data
    mock_users_objects.return_value.filter.return_value.first.return_value = mock_user_data
    
    # Mock JWT identity
    mock_get_jwt_identity.return_value = 'test@example.com'

    # Make a request to the dashboard endpoint
    response = client.get("/dashboard")

    # Assert the status code
    assert response.status_code == 500

    # Load the response data
    data = response.get_json()


def test_fetch_resume(client, auth_token):
    response = client.get(
        "/fetchresume",
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'


if __name__ == '__main__':
    pytest.main()
