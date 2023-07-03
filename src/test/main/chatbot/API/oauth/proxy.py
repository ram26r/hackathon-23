import os

import requests
from dotenv import load_dotenv
from fastapi import FastAPI

from utils import build_url

load_dotenv()

app = FastAPI()

HTTPS_SCHEME = os.environ.get("HTTPS_SCHEME")
GITLAB_NETLOC = os.environ.get("GITLAB_NETLOC")
PROXY_NETLOC = os.environ.get("PROXY_NETLOC")

OAUTH_TOKEN_URL = os.environ.get("OAUTH_TOKEN_URL")
GET_ACCESS_TOKEN_URL = os.environ.get("GET_ACCESS_TOKEN_URL")

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
STATE = os.environ.get("STATE")
SCOPE = os.environ.get("SCOPE")


@app.get("/get_access_token")
async def get_access_token(code: str, state: str):
    query_params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": build_url(HTTPS_SCHEME, PROXY_NETLOC, GET_ACCESS_TOKEN_URL)
    }
    headers = {"Accept": "application/json"}
    url = build_url(HTTPS_SCHEME, GITLAB_NETLOC, OAUTH_TOKEN_URL)
    data = requests.post(url=url, headers=headers, params=query_params)
    return data.json()


@app.get("/success")
async def success():
    return {'message': 'successfully generated access token.'}
