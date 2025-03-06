1. User clicks "Login with Facebook" on the frontend.
2. Redirect to Facebook's OAuth endpoint.
3. User authorizes your app (logs in or approves permissions).
4. Facebook redirects back to app with an authorization code.
5. Backend exchanges the code for an access token.
6. Backend fetches user information using the access token.
7. Frontend receives user data from the backend.