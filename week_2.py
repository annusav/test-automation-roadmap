#Python Automation Testing Roadmap 
#Week 2 Mini-Project: Script to read a CSV file of usernames & passwords, log attempts to a file.

import csv
import logging

logging.basicConfig(
    filename="login_attempts.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

valid_credentials = {
    "alice": "12345",
    "bob": "pass123"
}

def login(username, password):
    if username in valid_credentials and valid_credentials[username] == password:
        return True
    return False

def process_login(file):
    with open(file, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = row["username"]
            pwd = row["password"]
            success = login(user, pwd)

            if success:
                logging.info(f"Logged in as user: {user}")
            else:
                logging.warning(f"Wrong username or password")




process_login("./files/users.csv")
print("Login attempts processed. Check 'login_attempts.log'")