from typing import Optional, List
from pydantic import BaseModel as SCBaseModel, EmailStr
from schemas.artigo_shema import ArtigoSchema

class UsuarioSchemaBase(SCBaseModel):
    id: Optional[int] = None
    nome: str
    email: EmailStr
    eh_admin: bool = False


    class Config:
        from_attributes = True


class UsuarioShemaCreate(UsuarioSchemaBase):
    senha : str


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha : Optional[str] = None
    eh_admin: Optional[bool] = None