from fastapi import Depends, UploadFile, Response
from repository.account_repository import AccountRepository
from utils.tokens import create_token
from utils.crypto_tools import encode_id
from dotenv import load_dotenv
import os

load_dotenv()

COOKIE_SECURE_OPTION = os.getenv("COOKIE_SECURE_OPTION")

class AccountService:
    def __init__(self, repository: AccountRepository = Depends()):
        self.repository = repository

    def create_account(self, userName: str, userImage: bytes):

        # todo 얼굴 인식 로직

        account = self.repository.create_account(userName, userImage)

        login_token = create_token(
            payload={
                "userId": encode_id(account.userId),
                "userName": account.userName
            },
            expire=86400 # 하루
        )
        
        response = Response(status_code=201)
        response.set_cookie(
            key="login_token",
            value=login_token,
            max_age=86400, # 하루
            httponly=True,
            samesite="strict",
            secure = not COOKIE_SECURE_OPTION is None
        )

        return response