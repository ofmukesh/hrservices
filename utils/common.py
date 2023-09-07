import uuid


def generate_uuid_with_prefix(prefix):
    key = prefix+uuid.uuid4().hex[:10].upper()
    print(key)
    return key


def generate_uuid():
    return uuid.uuid4()


def generate_uuid_6():
    return uuid.uuid4().hex[:6]


def generate_uuid_10():
    return uuid.uuid4().hex[:10]


low_balance_err = "Insufficient funds to complete this transaction. Please add money to your wallet."
