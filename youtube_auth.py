from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Create the flow using the client secrets file from the Google API Console.
flow = InstalledAppFlow.from_client_secrets_file( 
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl']) # This grants full access to the YouTube account

""" Essentially, flow will get an authentication code and will use that alongside the client_secrets.json file to retrieve an 
access token that allows our app to get what's defined by the scopes"""


credentials = flow.run_local_server(port=8081) # Store the access and refresh tokens in the credentials object

youtube = build('youtube', 'v3', credentials=credentials) # build the YouTube service object; gives access to YouTube API 