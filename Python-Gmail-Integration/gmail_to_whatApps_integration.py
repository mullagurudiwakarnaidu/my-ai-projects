import os
import json
import base64
import re
import requests
import main

from dotenv import load_dotenv
from google import genai
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# -------------------------------------------------------------
# 1. Load environment variables
# -------------------------------------------------------------

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_ID = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


# --------------------------------------------------------------
# 2. Initialize Gemini AI
# --------------------------------------------------------------

#gemini_client = genai.Client(api_key=GEMINI_API_KEY)

finalHeaders = main.read_email();
print(finalHeaders)
for headers in finalHeaders:
    sender = ""
    subject = ""
    date = ""
    body = ""
    for header in headers:
        if header['name'].lower() == 'from':
            sender = header['value']
        elif header['name'].lower() == 'subject':
            subject = header['value']
        elif header['name'].lower() == 'date':
            date = header['value']
        #elif header['message'].lower() == 'message':
            #body = header['value']
    print("-----------------------------------")
    print("From: " + sender)
    print("Subject: " + subject)
    print("Date: " + date)
    #print("Body: " + body)


