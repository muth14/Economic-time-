from app.core.security import create_access_token, decode_access_token, verify_password, get_password_hash

def test_password_hashing():
    password = "industrial_secret_2026"
    hashed = get_password_hash(password)
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False

def test_jwt_token_creation_and_decoding():
    payload = {"sub": "engineer_elena", "role": "Lead Reliability Engineer"}
    token = create_access_token(payload)
    assert isinstance(token, str)
    
    decoded = decode_access_token(token)
    assert decoded["sub"] == "engineer_elena"
    assert decoded["role"] == "Lead Reliability Engineer"
