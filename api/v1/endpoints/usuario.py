from typing import List, Optional, Any
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.usuario_model import UsuarioModel
from schemas.usuario_shema import UsuarioSchemaBase, UsuarioShemaCreate, UsuarioSchemaUp, UsuarioSchemaArtigos
from core.deps import get_session, get_current_user
from core.security import gerar_hash_senha
from core.auth import autenticar, criar_token_acesso

router = APIRouter()


# USUARIO Logado
@router.get('/logado', response_model=UsuarioSchemaBase)
async def get_logado(usuario_logado : UsuarioModel = Depends(get_current_user)):
    return usuario_logado
     

# POST / Signup
@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def post_usuario(usuario: UsuarioShemaCreate, db: AsyncSession = Depends(get_session)):
    #novo_curso = CursoModel(**curso.model_dump())
    novo_usuario = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=gerar_hash_senha(usuario.senha))
    try:
        db.add(novo_usuario)
        await db.commit()
        return novo_usuario
    except IntegrityError:  
        raise HTTPException(detail='Já existe usuário com esse Email já cadastrado', status_code=status.HTTP_406_NOT_ACCEPTABLE)
  


@router.get('/', response_model=List[UsuarioSchemaBase])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        cursos: List[UsuarioSchemaBase] = result.scalars().unique().all()
        return cursos

@router.get('/{id}', response_model=UsuarioSchemaArtigos, status_code=status.HTTP_200_OK)
async def get_usuario(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == id)
        result = await session.execute(query)
        usuario: UsuarioSchemaArtigos | None = result.scalars().first()
        #curso = result.scalars_one_or_none()
        if not usuario:
            raise HTTPException(detail='Usuario não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        return usuario    


@router.put('/', response_model=UsuarioSchemaBase, status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuario: UsuarioSchemaUp, db: AsyncSession = Depends(get_session), usuario_logado:UsuarioModel = Depends(get_current_user)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario.id)
        result = await session.execute(query)
        usuario_up: UsuarioSchemaBase | None = result.scalars().first()
        #curso_obj = result.scalars_one_or_none()
        if usuario_up:
            if usuario.nome:
                usuario_up.nome = usuario.nome
            if usuario.email:
                usuario_up.email = usuario.email
            if usuario.eh_admin:
                usuario_up.eh_admin = usuario.eh_admin
            if usuario.senha:
                usuario_up.senha = gerar_hash_senha(usuario.senha)
            await session.commit()
            return usuario_up
        else:
            raise HTTPException(detail='Artigo não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == id)
        result = await session.execute(query)
        usuario_del: UsuarioModel | None = result.scalars().first()
        #curso_del = result.scalars().one_or_none()
        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Usuario não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        

#POST LOGIN
@router.post('/login', response_model=None)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    usuario = await autenticar(form_data.username, form_data.password, db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Dados de acesso incorretos')
    return JSONResponse(content={'access_token': criar_token_acesso(sub=usuario.id), 'token_type': 'bearer'}, status_code=status.HTTP_200_OK)
