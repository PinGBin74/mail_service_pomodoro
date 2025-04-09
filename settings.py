from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    from_email: str = "no-repplysmt@yandex.ru"
    SMTP_PORT: int = 465
    SMTP_HOST: str = "smtp.yandex.ru"
    SMTP_PASSWORD: str = "hltcizdaxcqbluuu"
    BROKER_URL: str = "127.0.0.1:9092"
    EMAIL_CALLBACK_TOPIC: str = "callback_email_topic"
