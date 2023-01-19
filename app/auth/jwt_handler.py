#This file is responsible for signing, encoding and decoding returning JWTs

import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

#Function returns generated token (JWTs)
def token_response(token:str):
    return{
        "acceess token" : token
    }

def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600
    }
    token= jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token : str):
    try:
        decode_token= jwt.decode(token, JWT_ALGORITHM, algorithm= JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}

