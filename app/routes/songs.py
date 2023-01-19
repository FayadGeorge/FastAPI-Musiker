from fastapi import APIRouter, body
from fastapi.encoders import jsonable_enconder

from app.server.database import{
    retrieve_song,
    add_song
}

router= APIRouter()