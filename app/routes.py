from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import get_db

router = APIRouter(
    prefix="/tarefas",
    tags=["tarefas"]
)

@router.post("/", response_model=schemas.TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    """
    Criar uma nova tarefa
    """
    #Cria uma nova instância do modelo
    nova_tarefa = models.Tarefa(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao
    )

    #Adicionar ao banco
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa) # atualiza com os dados do banco (id, ciada_em)

    return nova_tarefa

@router.get("/", response_model=List[schemas.TarefaResponse])
def listar_tarefas(concluida: bool = None, db: Session = Depends(get_db)):
    """
    Lista todas as tarefas. Pode filtrar por status usando o parâmetro 'concluida'.
    """
    query = db.query(models.Tarefa)

    if concluida is not None:
        query = query.filter(models.Tarefa.concluida == concluida)

    tarefas = query.all()
    return tarefas



@router.get("/{tarefa_id}", response_model=schemas.TarefaResponse)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    """
    Busca uma tarefa especifica por ID
    """
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()

    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {tarefa_id} não encontrada"
        )
    return tarefa

@router.put("/", response_model=schemas.TarefaResponse)
def atualizar_tarefas(tarefa_id:int, tarefa_atualizada: schemas.TarefaCreate, db: Session = Depends(get_db)):
    """
    Atualiza uam tarefa existente
    """
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()

    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {tarefa_id} não encontrada"
        )

    tarefa.titulo = tarefa_atualizada.titulo
    tarefa.descricao = tarefa_atualizada.descricao

    db.commit()
    db.refresh(tarefa)

    return tarefa


@router.patch("/{tarefa_id}/concluir", response_model=schemas.TarefaResponse)
def marcar_concluida(tarefa_id: int, db: Session = Depends(get_db)):
    """
    Marca uma tarefa como concluída/não concluída (toggle)
    """
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()

    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {tarefa_id} não encontrada"
        )

    tarefa.concluida = not tarefa.concluida  # Toggle

    db.commit()
    db.refresh(tarefa)

    return tarefa

@router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    """
    Deleta uma tarefa
    """
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()

    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {tarefa_id} não encontrada"
        )

    db.delete(tarefa)
    db.commit()

    return None

    return None