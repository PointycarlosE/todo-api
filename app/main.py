from fastapi import FastAPI
from .database import engine, Base
from .routes import router

#Criar as Tabelas no banco de dados
Base.metadata.create_all(bind=engine)

#Criar instância do FastAPI
app = FastAPI(
    title="Todo API",
    description="API de gerenciamento de tarefas",
    version="1.0.0"
)

#Incluir as rotas
app.include_router(router)


@app.get("/")
def root():
    """
    Endpoint raiz - verifica se a API está funcionando
    """
    return {"message": "API de tarefas funcionando! Acesse /docs para ver a documentação"}