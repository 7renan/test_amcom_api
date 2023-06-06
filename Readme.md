# TESTE AMCOM API

## Iniciando projeto

### Após fazer o download do repositório execute os seguintes comandos na raiz pro projeto
#### Criando uma máquina virtual
```` python -m venv .venv ```` 

#### Ativar a máquina Virtual
```` .venv/Scripts/activate ````

#### Instalando todas as deoendências
```` pip install -r requirements.txt ````

#### Aplicando migrações de banco de dados
```` python manage.py makemigrations ````
```` python manage.py migrate ````

#### Executando o projeto
```` python manage.py runserver ````

## Rotas
### Rota raiz de documentação da API ``/api/v1/``

