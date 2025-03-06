from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth

app = FastAPI(title="Facebook OAuth2 with FastAPI")


# WILDCARD for testing purposes
# for Frontend, CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add ROUTERS here
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Facebook OAuth2 with FastAPI"}
