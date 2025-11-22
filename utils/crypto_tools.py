from hashids import Hashids
from dotenv import load_dotenv
import os

load_dotenv()

HASH_ID_SALT = os.getenv("HASH_ID_SALT")

hashid = Hashids(HASH_ID_SALT, 16)

def encode_id(id: int) -> str:
    return hashid.encode(id)

def decode_id(id: str) -> int:
    return hashid.decode(id)