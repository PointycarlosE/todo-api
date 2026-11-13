# 📝 Todo API

API REST para gerenciamento de tarefas construída com FastAPI e SQLAlchemy.

## 🚀 Sobre o Projeto

Esta é uma API completa de gerenciamento de tarefas (To-Do List) que permite criar, listar, atualizar e deletar tarefas. Desenvolvida como projeto de portfólio para demonstrar conhecimentos em:

- Desenvolvimento de APIs REST
- Python e FastAPI
- ORM com SQLAlchemy
- Validação de dados com Pydantic
- Documentação automática com Swagger/OpenAPI
- Boas práticas de organização de código

## ✨ Funcionalidades

- ✅ Criar nova tarefa
- ✅ Listar todas as tarefas
- ✅ Buscar tarefa específica por ID
- ✅ Atualizar tarefa (título e descrição)
- ✅ Marcar tarefa como concluída/pendente
- ✅ Deletar tarefa
- ✅ Validação automática de dados
- ✅ Documentação interativa

## 🛠️ Tecnologias Utilizadas

- **[Python 3.14](https://www.python.org/)** - Linguagem de programação
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para banco de dados
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI
- **[SQLite](https://www.sqlite.org/)** - Banco de dados

## 📁 Estrutura do Projeto

```bash
todo-api/
├── app/
│   ├── init.py
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── models.py        # Modelos do banco de dados
│   ├── schemas.py       # Schemas de validação (Pydantic)
│   ├── routes.py        # Rotas/Endpoints da API
│   └── database.py      # Configuração do banco de dados
├── venv/                # Ambiente virtual
├── .gitignore
├── requirements.txt     # Dependências do projeto
└── README.md
```

## 🔧 Instalação e Execução

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a passo

1. **Clone o repositório**
```bash
git clone https://github.com/SEU-USUARIO/todo-api.git
cd todo-api
```
2. **Crie e ative o ambiente virtual**
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
3. **Instale as dependências**
```bash
pip install -r requiriments.txt
```
4. **Execute a aplicação**
```bash
uvicorn app.main:app --reload
```
5. **Acesse a documentação Interativa**
Abra seu navegador em: http://127.0.0.1:8000/docs

Documentação da API
Endpoints disponíveis:
Método	Endpoint	Descrição
POST	/tarefas/	Cria uma nova tarefa
GET	/tarefas/	Lista todas as tarefas
GET	/tarefas/{id}	Busca uma tarefa específica
PUT	/tarefas/{id}	Atualiza uma tarefa
PATCH	/tarefas/{id}/concluir	Marca/desmarca como concluída
DELETE	/tarefas/{id}	Deleta uma tarefa
Exemplos de uso:
Criar uma tarefa

curl -X POST "http://127.0.0.1:8000/tarefas/" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Estudar FastAPI",
    "descricao": "Aprender a criar APIs REST"
  }'
Listar todas as tarefas

curl -X GET "http://127.0.0.1:8000/tarefas/"
Marcar como concluída

curl -X PATCH "http://127.0.0.1:8000/tarefas/1/concluir"
🧪 Testando a API
Acesse a documentação interativa (Swagger UI) em:


http://127.0.0.1:8000/docs
Lá você pode testar todos os endpoints diretamente pelo navegador!

🎯 Próximas Melhorias
 Adicionar autenticação JWT
 Implementar filtros (listar só concluídas/pendentes)
 Adicionar paginação
 Adicionar categorias/tags
 Implementar data de vencimento
 Adicionar testes automatizados
 Migrar para PostgreSQL
 Deploy em produção
📝 Licença
Este projeto está sob a licença MIT.

👤 Autor
Carlos Eduardo Martins Rodrigues

GitHub: @PointycarlosE
LinkedIn: https://www.linkedin.com/in/carlos-martins-rodrigues/
⭐ Se este projeto te ajudou, considere dar uma estrela!

