from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = "Описание"

    class Config:
        env_file = '.env'


settings = Settings()
