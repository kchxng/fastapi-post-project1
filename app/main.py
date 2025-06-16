import os
from dotenv import load_dotenv # type: ignore
from fastapi import FastAPI # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from app.api.routers import api_router

# Load environment variables from a .env file
load_dotenv()

if os.getenv("ENV_NODE")!="development":
    # Disable Swagger UI & ReDoc Documentation when running on a production
    app=FastAPI(docs_url=None, redoc_url=None)
else:
    app=FastAPI()

# ----------------------------------------------------------------
# Desc: Match or include route from v1 file
# ----------------------------------------------------------------
# ***** Features **********
app.include_router(api_router, prefix="/api/v1")

# ******** Image path ***********
app.mount("/images",StaticFiles(directory="assets/images",html=True), name="images")