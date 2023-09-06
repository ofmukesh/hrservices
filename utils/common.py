import uuid

def generate_uuid_with_prefix(prefix):
    return prefix+uuid.uuid4()[:6]

def generate_uuid():
    return uuid.uuid4()

def generate_uuid_6():
    return uuid.uuid4().hex[:6]

def generate_uuid_10():
    return uuid.uuid4().hex[:10]
