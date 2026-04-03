import uuid

def generate_id ():
    return str(uuid.uuid4())

generate_id()
print(generate_id())