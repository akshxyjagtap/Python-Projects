from pprint import pprint
from flask import Flask, request
import json
import requests
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import pyperclip
import re
import pandas as pd
from Google import Create_Service
with open('links.txt') as f:
    for line in f:
        print(line)
        url=line
        pattern = r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})'
        result = re.findall(pattern, url, re.MULTILINE | re.IGNORECASE)
        # print(result[0])

        CLIENT_SECRET_FILE = 'client-secret.json'
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/youtube']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

        part_string = 'contentDetails,snippet'
        # part_string = 'contentDetails',snippet"
        video_ids = result[0]

        response = service.videos().list(
            part=part_string,
            id=video_ids
        ).execute()

        pprint(response)

        with open('data.json', 'w', encoding='utf-8') as f: json.dump(response, f, ensure_ascii=False, indent=4)


        category = ["emotions","nature","language_and_literary","creativity_and_arts",
                    "physical_and_motor_development","mathematical_and_logical_thinking","cartoon"]


        title = response["items"][0]["snippet"]["title"]
        thumbnail = response["items"][0]["snippet"]["thumbnails"]["maxres"]["url"]
        time = pd.Timedelta(response["items"][0]["contentDetails"]["duration"])
        # ["items"][0]["snippet"]["title"]
        time = str(time.to_pytimedelta())
        time = time[2:]

        # extracting inp info

        final = {
            "videoUrl": url[0:-1],
            "category": "creativity_and_arts",
            "title": title,
            "imageUrl":thumbnail,
            "language": "English",
            "duration": time
        }
        json_formatted_str = json.dumps(final, indent=4)
        print(json_formatted_str)
