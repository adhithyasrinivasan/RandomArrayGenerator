from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Dict, List
import numpy as np
from pydantic import BaseModel,Field,validator
from jose import JWTError, jwt

router = APIRouter()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_jwt_token(data: Dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception

class SentenceInput(BaseModel):
    #sentence: str = Field(..., title="Input Sentence", description="The input sentence for processing.")
    sentence: str = Field (default=None,title="Input Sentence", description="The input sentence for processing.",max_length=1000,min_length=1)

    @validator("sentence", pre=True, always=True)
    def check_sentence_type(cls, value):
        if not isinstance(value, str):
            raise ValueError("Invalid type. Sentence must be a string.")
        return value
    

def generate_random_array() -> List[float]:
    return list(np.random.rand(500))

@router.post("/", response_model=Dict[str, List[float]])
async def get_random_array(sentenceInput: SentenceInput,current_user: Dict = Depends(get_current_user)):
    try:
        # Additional input validation
        random_array = generate_random_array()

        return {'random_array': random_array}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.post("/token")
def login_for_access_token():
    token_data = {"sub": "test@example.com"}
    return {"access_token": create_jwt_token(token_data), "token_type": "bearer"}