import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
def connect_to_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service
def read_email():
    service = connect_to_gmail()
    finalHeaders =[]
    #Get the latest 5 emails
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    for message in messages:
        email_data = service.users().messages().get(userId='me', id=message['id'], format="full").execute()
        headers = email_data['payload']['headers']
        finalHeaders.append(headers)
        sender = ""
        subject = ""
        date = ""
        for header in headers:
            if header['name'].lower() == 'from':
                sender = header['value']
            elif header['name'].lower() == 'subject':
                subject = header['value']
            elif header['name'].lower() == 'date':
                date = header['value']

        #print("-----------------------------------")
        #print("From: " + sender)
        #print("Subject: " + subject)
        #print("Date: " + date)
        #print("Snippet: " + email_data.get("snippet", ""))
    return finalHeaders
if __name__ == '__main__':
    read_email()