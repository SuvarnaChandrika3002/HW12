import hashlib
import bcrypt

def _to_bytes(s: str) -> bytes:
    if isinstance(s, str):
        return s.encode("utf-8")
    if isinstance(s, bytes):
        return s
    raise TypeError("password must be str or bytes")

def hash_password(password: str) -> str:
    
    pw_bytes = _to_bytes(password)
    digest = hashlib.sha256(pw_bytes).digest()  
    hashed = bcrypt.hashpw(digest, bcrypt.gensalt())
    return hashed.decode("utf-8")

def verify_password(plain: str, hashed: str) -> bool:
    pw_bytes = _to_bytes(plain)
    digest = hashlib.sha256(pw_bytes).digest()
    return bcrypt.checkpw(digest, hashed.encode("utf-8"))
