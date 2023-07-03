import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

HTTPS_SCHEME = os.environ.get("HTTPS_SCHEME")
GITLAB_NETLOC = os.environ.get("GITLAB_NETLOC")
PROXY_NETLOC = os.environ.get("PROXY_NETLOC")

GET_ACCESS_TOKEN_URL = os.environ.get("GET_ACCESS_TOKEN_URL")
OAUTH_AUTHORIZE_URL = os.environ.get("OAUTH_AUTHORIZE_URL")

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
STATE = os.environ.get("STATE")
SCOPE = os.environ.get("SCOPE")


@app.get("/gitlab/auth")
async def get_gitlab_auth_url():
    from utils import build_url

    query_params = {
        "client_id": CLIENT_ID,
        "redirect_uri": build_url(HTTPS_SCHEME, PROXY_NETLOC, GET_ACCESS_TOKEN_URL),
        "response_type": "code",
        "state": STATE,
        "scope": SCOPE
    }

    return {'url': build_url(HTTPS_SCHEME, GITLAB_NETLOC, OAUTH_AUTHORIZE_URL, None, query_params, None)}


@app.get("/success")
async def success():
    return {'message': 'successfully generated access token.'}
