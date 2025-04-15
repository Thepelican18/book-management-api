class ServerConfig:
    API_HOSTNAME = "0.0.0.0"
    API_PORT = 5080
    API_WORKERS = 1

    CORS_ORIGINS = ["*"]
    CORS_METHODS = ["GET","POST","PUT","DELETE"]
    CORS_HEADERS = ["*"]
    CORS_CREDENTIALS = True

class PathConfig:
    PICKLE_PATH = "./pickle_db.pkl"