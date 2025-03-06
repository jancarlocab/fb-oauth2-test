from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
import httpx 

load_dotenv()

router = APIRouter(prefix="/facebook/auth", tags=["auth"])

FACEBOOK_CLIENT_ID = os.getenv("FACEBOOK_CLIENT_ID")
FACEBOOK_CLIENT_SECRET = os.getenv("FACEBOOK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Redirect to Facebook OAuth2
@router.get("/login")
async def facebook_login():
    fb_oauth_url = (
        f"https://www.facebook.com/v22.0/dialog/oauth"
        f"?client_id={FACEBOOK_CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email"
    )
    return RedirectResponse(fb_oauth_url)

# Handle the Facebook callback
@router.get("/callback")
async def facebook_callback(code: str = Query(...)):
    try:
        # TO GET ACCESS TOKEN
        token_url = "https://graph.facebook.com/v18.0/oauth/access_token"
        payload = {
            "client_id": FACEBOOK_CLIENT_ID,
            "client_secret": FACEBOOK_CLIENT_SECRET,
            "redirect_uri": REDIRECT_URI,
            "code": code,
        }

        # FETCH USER DETAILS
        async with httpx.AsyncClient() as client:
            token_response = await client.get(token_url, params=payload)
            token_response.raise_for_status()
            access_token = token_response.json().get("access_token")

            # Fetch user profile
            user_url = "https://graph.facebook.com/me"
            user_params = {"fields": "id,name,email", "access_token": access_token}
            user_response = await client.get(user_url, params=user_params)
            user_response.raise_for_status()

        # convert user info to json
        user_info = user_response.json()
        # then return JSON
        return {"user": user_info, "access_token": access_token}

    except httpx.HTTPError as e:
        raise HTTPException(status_code=400, detail=f"OAuth2 flow failed: {e}")
