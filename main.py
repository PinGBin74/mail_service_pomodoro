from contextlib import asynccontextmanager

from fastapi import FastAPI

from utils import consume_message


@asynccontextmanager
async def lifespan(app: FastAPI):
    await consume_message()
    yield


app = FastAPI(lifespan=lifespan)
