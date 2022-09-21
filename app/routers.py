from fastapi import APIRouter

# from app import contracts

router = APIRouter()


@router.get('/')
def read_root():
    return {"Hello": "World"}
