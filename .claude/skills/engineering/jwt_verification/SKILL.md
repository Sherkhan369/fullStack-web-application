---
name: jwt_verification
description: Verify JWT tokens in FastAPI endpoints and extract authenticated user identity securely from Authorization headers using Better Auth secrets.
license: Complete terms in LICENSE.txt
---

# JWT Verification Skill

## Purpose

This skill provides FastAPI middleware and utility functions for secure JWT token verification. It extracts authenticated user identity from Authorization headers and handles token validation errors.

## When to Use

Use this skill when implementing authentication for FastAPI endpoints that require:

- JWT token verification from Authorization headers
- User identity extraction from valid tokens
- Proper 401 error handling for invalid/missing tokens
- Integration with Better Auth secret management

## Usage

### 1. Import the JWT verification utilities

```python
from .auth.jwt_utils import verify_jwt_token, get_current_user
```

### 2. Use as dependency in FastAPI routes

```python
from fastapi import Depends, HTTPException
from .schemas.auth import User

@app.get("/protected")
async def protected_endpoint(
    current_user: User = Depends(get_current_user)
):
    return {"message": f"Hello {current_user.username}"}
```

### 3. Manual token verification (when needed)

```python
from fastapi import Request
from .auth.jwt_utils import verify_jwt_token

async def manual_verification(request: Request):
    try:
        user = await verify_jwt_token(request)
        return {"user": user}
    except HTTPException as e:
        raise e  # Re-raise 401 errors
```

## Implementation Details

### Token Extraction

The skill extracts JWT tokens from the Authorization header in the format:
`Authorization: Bearer <token>`

If no Authorization header is present, returns `None` for optional authentication scenarios.

### Token Verification

Uses `better-auth` library to:
- Decode JWT tokens using `BETTER_AUTH_SECRET`
- Validate token signature and expiration
- Extract user identity data

### Error Handling

- **Missing token**: Returns `None` for optional auth, raises 401 for required auth
- **Invalid token**: Raises HTTPException with status_code=401
- **Expired token**: Raises HTTPException with status_code=401
- **Malformed header**: Raises HTTPException with status_code=400

### Dependencies

Required environment variable:
- `BETTER_AUTH_SECRET`: Secret key for JWT signing/verification

Required packages:
- `better-auth`: JWT token handling
- `fastapi`: Web framework
- `pydantic`: Data validation

## Security Considerations

- Always validate tokens server-side before processing requests
- Never trust client-provided user data without verification
- Use HTTPS in production to protect token transmission
- Set appropriate token expiration times
- Rotate secrets regularly

## Example Integration

```python
# main.py
from fastapi import FastAPI, Depends, HTTPException
from .auth.jwt_utils import get_current_user
from .schemas.auth import User

app = FastAPI()

@app.get("/api/profile")
async def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }
```

## Testing

When testing endpoints that use this skill:

1. Include valid Authorization header: `Authorization: Bearer <valid-jwt>`
2. Test error cases: missing header, invalid token, expired token
3. Verify 401 responses are returned for invalid authentication
4. Mock the JWT verification in unit tests to avoid external dependencies