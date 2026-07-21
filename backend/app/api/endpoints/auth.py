from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import UserLogin, Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(credentials: UserLogin):
    # Enterprise Auth Endpoint
    if credentials.username in ["admin", "engineer", "auditor"] and credentials.password in ["admin123", "password", "industrial2026"]:
        role = "System Administrator" if credentials.username == "admin" else ("Lead Reliability Engineer" if credentials.username == "engineer" else "Compliance Auditor")
        return Token(
            access_token=f"jwt-token-industrial-brain-{credentials.username}-2026",
            user={
                "id": f"USR-{hash(credentials.username) % 1000:03d}",
                "username": credentials.username,
                "name": f"Enterprise User ({credentials.username.capitalize()})",
                "role": role,
                "email": f"{credentials.username}@industrialbrain.ai"
            }
        )
    raise HTTPException(status_code=401, detail="Invalid credentials. Use admin/admin123 or engineer/password.")
