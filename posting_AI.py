import requests
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

# Load the client secrets file
CLIENT_SECRETS_FILE = 'client_secrets.json'
TOKEN_FILE = 'token.json'

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/blogger']

def call_api(prompt, realtime):
    url = 'https://itzpire.com/ai/gpt-logic'
    params = {
        'q': prompt,
        'logic': 'respon dalam bahasa yang di inputkan. anda adalah sebuah ahli dalam bahasa pemerograman html jadi tulis hanya dalam respon html. hasilkan hanya <h2><h3><p>',
        'realtime': realtime
    }

    try:
        response = requests.get(url, params=params)
        response_data = response.json()  # Jika respons dari API adalah JSON
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def authenticate():
    creds = None
    # Load credentials from file if they exist
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token:
            creds = Credentials.from_authorized_user_info(json.load(token), SCOPES)
    # If there are no valid credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def post_article(title, content, blog_id, creds):
    url = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/'
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }
    data = {
        'kind': 'blogger#post',
        'title': title,
        'content': content
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def main():
    prompt = input("Masukkan prompt Anda: ")
    realtime_option = input("Pilih opsi realtime (1 untuk true, 2 untuk false): ")
    realtime = True if realtime_option == '1' else False

    api_result = call_api(prompt, realtime)

    if api_result:
        print("Response dari API:")
        print(api_result)
        blog_id = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
        title = input("Masukkan judul artikel: ")
        content = api_result['data']['response']  # Mengambil konten dari respons API

        creds = authenticate()
        response = post_article(title, content, blog_id, creds)
        print(response)
    else:
        print("Gagal memanggil API.")

if __name__ == '__main__':
    main()
