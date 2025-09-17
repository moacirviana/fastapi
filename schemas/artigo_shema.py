from typing import Optional
from pydantic import BaseModel as SCBaseModel, HttpUrl

class ArtigoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: str
    usuario_id: Optional[int] = None

    class Config:
        from_attributes = True


''''
 id :int = Column(Integer, primary_key=True, autoincrement=True)
    titulo : str = Column(String(256))
    url_fonte : str = Column(String(256))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')
'''