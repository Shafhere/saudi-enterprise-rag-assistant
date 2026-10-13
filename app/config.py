from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./docintel.db"
    chroma_dir: str = "./chroma_db"
    upload_dir: str = "./data"

settings = Settings()