def validate_amount(amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number")

def validate_name(name):
    def validate_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")