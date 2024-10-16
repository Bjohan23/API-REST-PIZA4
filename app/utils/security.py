from werkzeug.security import check_password_hash

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)