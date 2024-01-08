def perform_login(registered_user, login_username, login_password, provided_auth_code):
    if registered_user['username'] == login_username and registered_user['password'] == login_password and registered_user["auth_code"] == provided_auth_code:
        return f"Access granted for {login_username}."
    elif registered_user['password'] != login_password and registered_user['username'] == login_username:
        return f"Incorrect password for {login_username}. Access denied."
    elif registered_user['username'] == login_username and registered_user['password'] == login_password and registered_user["auth_code"] != provided_auth_code:
        return f"Incorrect authentication code for {registered_user['username']}. Access denied."
    return f"User {login_username} not found. Access denied."

def authenticate(username, password, auth_code, login_username, login_password, provided_auth_code):
    registered_user = {"username": username, "password": password, "auth_code": auth_code}
    return perform_login(registered_user, login_username, login_password, provided_auth_code)

def main():
    # User information registration
    username = input()
    password = input()
    
    # Authentication code setup
    auth_code = input()
    
    # Login attempt
    login_username = input()
    login_password = input()
    
    # Provided authentication code input
    provided_auth_code = input()
    
    # Authenticate with provided authentication code
    result = authenticate(username, password, auth_code, login_username, login_password, provided_auth_code)  
    print(result)

if __name__ == "__main__":
    main()