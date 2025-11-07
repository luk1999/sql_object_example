import hashlib


MIN_PASS_LEN = 8


def encode_password(password: str) -> str:
    """Just for demo purpose. It should not be used in real-world app!"""
    return hashlib.md5(password.encode()).hexdigest()


class UserService:
    encode_password = encode_password
