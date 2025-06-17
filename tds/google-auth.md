## Google Authentication with FastAPI

Secure your API endpoints using Google ID tokens to restrict access to specific email addresses.

[![🔥 Python FastAPI Google Login Tutorial | OAuth2 Authentication (19 min)](https://i.ytimg.com/vi_webp/4ExQYRCwbzw/sddefault.webp)](https://youtu.be/4ExQYRCwbzw
<youtube_summary>Leah Bonasaki from Master Lab Systems presents a tutorial on integrating OAuth 2.0 with Google login into a FastAPI project. OAuth 2.0 is explained as an authorization framework enabling third-party apps to access user resources securely without sharing passwords, commonly used for social logins like Google, Facebook, and GitHub. Google login is chosen for its simplicity, security, and improved user experience by eliminating the need for new credentials.

FastAPI is recommended due to its modern, asynchronous Python web framework design, ease of integration, and built-in OAuth 2.0 support, making it ideal for secure API authentication and authorization.

Prerequisites include a Google Developer Console project, Python 3.9+, FastAPI, and Uvicorn server. The setup involves creating Google credentials via the Google Developer Console: enabling OAuth 2.0, setting up a consent screen, creating client credentials, and configuring redirect URLs.

The OAuth 2.0 implementation flow includes building a Google OAuth URL, handling the callback to exchange authorization code for tokens, and retrieving the user profile upon successful authentication. The demo shows a user visiting the site, being redirected to Google’s consent screen, and upon success, being redirected back with an access token to fetch and display their user profile.

Leah walks through creating a Google Cloud project and OAuth client, downloading the client credentials JSON (containing client ID and secret), and storing these in a .env file along with the redirect URL for security. She outlines the FastAPI app code structure: importing necessary modules, loading environment variables, defining Google OAuth endpoints (token and user info), and creating routes for the homepage, login redirect, OAuth callback, and profile display.

The homepage presents a welcome message with a login link directing to Google OAuth. The login route initiates the OAuth process, the callback route exchanges the authorization code for an access token and fetches user info (name, email, picture), and the profile route displays the authenticated user’s details.

Testing demonstrates successful login using Google accounts, token generation, and profile retrieval, with HTTP 200 status indicating success. Leah also tests the cancellation scenario, showing proper error handling when authorization is denied.

The tutorial concludes with Leah inviting viewers to request the code via GitHub and encouraging comments and subscriptions.</youtube_summary>
)

Google Auth is the most commonly implemented single sign-on mechanism because:

- It's popular and user-friendly. Users can log in with their existing Google accounts.
- It's secure: Google supports OAuth2 and OpenID Connect to handle authentication.

Here's how you build a FastAPI app that identifies the user.

1. Go to the [Google Cloud Console – Credentials](https://console.developers.google.com/apis/credentials) and click **Create Credentials > OAuth client ID**.
2. Choose **Web application**, set your authorized redirect URIs (e.g., `http://localhost:8000/`).
3. Copy the **Client ID** and **Client Secret** into a `.env` file:

   ```env
   GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=your-client-secret
   ```

4. Create your FastAPI `app.py`:

```python
# /// script
# dependencies = ["python-dotenv", "fastapi", "uvicorn", "itsdangerous", "httpx", "authlib"]
# ///

import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth

load_dotenv()
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="create-a-random-secret-key")

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/")
async def application(request: Request):
    user = request.session.get("user")
    # 3. For authenticated users: say hello
    if user:
        return f"Hello {user['email']}"
    # 2. For users who have just logged in, save their details in the session
    if "code" in request.query_params:
        token = await oauth.google.authorize_access_token(request)
        request.session["user"] = token["userinfo"]
        return RedirectResponse("/")
    # 1. For users who are logging in for the first time, redirect to Google login
    return await oauth.google.authorize_redirect(request, request.url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
```

Now, run `uv run app.py`.

1. When you visit <http://localhost:8000/> you'll be redirected to a Google login page.
2. When you log in, you'll be redirected back to http://localhost:8000/
3. Now you'll see the email ID you logged in with.

Instead of displaying the email, you can show different content based on the user. For example:

- Allow access to specfic users and not others
- Fetch the user's personalized information
- Display different content based on the user
