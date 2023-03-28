from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CONTRACT_ADDRESS: str = Field(..., env='CONTRACT_ADDRESS')
    PROVIDER_URL: str = Field(..., env='PROVIDER_URL')
    PRIVATE_KEY: str = Field(..., env='PRIVATE_KEY')

    DB_HOST: str = Field(..., env='DB_HOST')
    DB_PORT: str = Field(..., env='DB_PORT')
    DB_USER: str = Field(..., env='DB_USER')
    DB_PASSWORD: str = Field(..., env='DB_PASSWORD')
    DB_NAME: str = Field(..., env='DB_NAME')

    SECRET_KEY: str = Field(..., env='SECRET_KEY')

    OPENAI_API_KEY: str = Field(..., env='OPENAI_API_KEY')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
