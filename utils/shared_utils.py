import hashlib


def generate_hash(value):
    if not value:
        return None
    md5_hash=hashlib.md5()
    md5_hash.update(value.encode('utf-8'))
    return md5_hash.hexdigest()