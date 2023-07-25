import hashlib

from shortener.exceptions import EmptyHashValueException, InvalidHashValueException

def get_md5_hash(value: str, hash_size: int = 10):
    if not value:
        raise EmptyHashValueException("")
    if type(value) is not str:
        raise InvalidHashValueException("", type(value))
    try:
        value = value.encode('utf-8')
        hash_object = hashlib.md5(value)
        hash_value = hash_object.hexdigest()[:hash_size]
    except Exception:
        raise Exception
    return hash_value