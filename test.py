import datetime
import time
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service

API_NAME="youtube"
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/youtube']
client_file='client_secret.json'
service=create_service(client_file,API_NAME,API_VERSION,SCOPES)

#upload

request_body={
    'snippet':{
    'title':'Test 1',
    'description':'test',
    },
    'status':{
    'privacyStatus':'private',
    }
}

video_file="video.mp4"

media_file=MediaFileUpload(video_file)
print(media_file.to_json())

response=service.videos().insert(
    part="snippet, status",
    bodt=request_body,
    media_body=media_file
).execute()

print(response)