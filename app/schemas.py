from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TarefaBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200, description="Titulo da tarefa")
    descricao: Optional[str] = Field(None, max_length=1000, description="Descrição opcional")

class TarefaCreate(TarefaBase):
    pass

class TarefaResponse(TarefaBase):
    id: int
    concluida: bool
    criada_em: datetime

    class Config:
        from_attributes = True

        