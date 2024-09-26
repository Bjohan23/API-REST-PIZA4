from werkzeug.security import generate_password_hash, check_password_hash

# Contraseña a hashear
password = "123"

# Hashear la contraseña
hashed_password = generate_password_hash(password)

print("Contraseña hasheada:", hashed_password)

# Verificar la contraseña
is_correct = check_password_hash(hashed_password, "123")
print("¿La contraseña es correcta?", is_correct)
