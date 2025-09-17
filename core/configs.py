from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from typing import ClassVar

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    #DB_URL: str = "sqlite+aiosqlite:///./Users/moacirmoacir/dev/db/xibefood.db3"
    DB_URL: str = "sqlite+aiosqlite:////Users/moacirmoacir/dev/db/xibefood.db3"
    DBBaseModel : ClassVar[DeclarativeMeta] =  declarative_base()

    JWT_SECRET : str = 'seLtKtzdkPp1FhUvQaXBjxgqbhp3iKIK'
    ALGORITHM : str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings : Settings = Settings()


'''' GERANDO UM JWT_SECRET
import secrets
token : str = secrets.token_urlsafe(32)
token
'''