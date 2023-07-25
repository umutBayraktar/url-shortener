import hashlib

def get_md5_hash(value: str, hash_size: int = 10):
    value = value.encode('utf-8')
    hash_object = hashlib.md5(value)
    hash_value = hash_object.hexdigest()[:hash_size]
    return hash_value