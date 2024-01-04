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

#
# # from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
# # from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
#
# # Generate an RSA private key
# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
#
# )
#
# # Serialize the private key to PEM format
# # pem_private = private_key.private_bytes(
# #     encoding=serialization.Encoding.PEM,
# #     format=serialization.PrivateFormat.TraditionalOpenSSL,
# #     encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')  # Replace 'mypassword' with your passphrase
# # )
#
# # Save private key to a file
# with open('private_key.pem', 'wb') as private_key_file:
#     private_key_file.write(private_key.private_bytes())
#
# # Get the corresponding public key
# public_key = private_key.public_key()
#
# # Serialize the public key to PEM format
# # pem_public = public_key.public_bytes(
# #     encoding=serialization.Encoding.PEM,
# #     format=serialization.PublicFormat.SubjectPublicKeyInfo
# # )
#
# # Save public key to a file
# with open('public_key.pem', 'wb') as public_key_file:
#     public_key_file.write(public_key.public_bytes())
