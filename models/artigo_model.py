from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

''''
Essa classe representa o modelo de dados para a tabela "cursos" no banco de dados.
Ela herda de settings.DBBaseModel, que é a base declarativa do SQLAlchemy.
Cada atributo da classe corresponde a uma coluna na tabela.
'''
class ArtigoModel(settings.DBBaseModel):
    __tablename__ = "artigos"

    id :int = Column(Integer, primary_key=True, autoincrement=True)
    titulo : str = Column(String(256))
    url_fonte : str = Column(String(256))
    descricao : str = Column(String(256))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined')