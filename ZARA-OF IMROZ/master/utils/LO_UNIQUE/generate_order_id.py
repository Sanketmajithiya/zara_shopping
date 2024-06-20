import uuid

def generate_unique_order_id():
    # Generate a unique UUID
    order_id = uuid.uuid4()
    return str(order_id)


if __name__ == "__main__":

    print(generate_unique_order_id())
    