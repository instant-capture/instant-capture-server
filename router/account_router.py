from fastapi import APIRouter, UploadFile, Form, File, Depends
from service.account_service import AccountService

router = APIRouter(prefix="/account", tags=["account"])

@router.post("")
async def create_account(userName: str = Form(), userImage: UploadFile = File(), service: AccountService = Depends()):
    return service.create_account(userName, await userImage.read())