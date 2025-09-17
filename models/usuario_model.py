from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

''''
Essa classe representa o modelo de dados para a tabela "cursos" no banco de dados.
Ela herda de settings.DBBaseModel, que é a base declarativa do SQLAlchemy.
Cada atributo da classe corresponde a uma coluna na tabela.
'''
class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id :int = Column(Integer, primary_key=True, autoincrement=True)
    email : str = Column(String(256), nullable=False, index=True, unique=True)
    nome : str = Column(String(256), nullable=True)
    senha : str = Column(String(256), nullable=False)
    eh_admin : bool = Column(Boolean, default=False)
    artigos = relationship(
        'ArtigoModel',
        cascade="all, delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
