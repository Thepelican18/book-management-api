import os

class ServerConfig:
    API_HOSTNAME = "0.0.0.0"
    API_PORT = 5080
    API_WORKERS = 1

    CORS_ORIGINS = ["*"]
    CORS_METHODS = ["GET","POST","PUT","DELETE"]
    CORS_HEADERS = ["*"]
    CORS_CREDENTIALS = True

    API_KEY_NAME = "X-API-Key"  
    API_KEY = os.getenv("API_KEY","N23489NDSAsaddI1239MCK")      

class PathConfig:
    PICKLE_PATH = "./pickle_db.pkl"