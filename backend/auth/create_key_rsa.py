from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate an RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Convert private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Convert public key to PEM format
public_key = private_key.public_key()
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the private key to a PEM file
with open("../auth/private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_pem)

# Save the public key to a PEM file
with open("../auth/public_key.pem", "wb") as public_key_file:
    public_key_file.write(public_pem)
