import json
from client import MailClient
from service import MailService
from aiokafka import AIOKafkaConsumer

consumer = AIOKafkaConsumer(
    "email_topic",
    bootstrap_servers="127.0.0.1:9092",
    value_deserializer=lambda message: json.loads(message.decode("utf-8")),
)


async def get_mail_service() -> MailService:
    return MailService(mail_client=MailClient())


async def consume_message():
    mail_service = await get_mail_service()
    await consumer.start()

    try:
        async for message in consumer:
            await mail_service.consume_mail(message.value)
            print(message)
    finally:
        await consumer.stop()
