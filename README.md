# CRUD de Usuários com Servidor HTTP em Python

## Descrição

Projeto simples de um CRUD (Create, Read, Update, Delete) de usuários, implementado em Python usando a biblioteca padrão (`http.server`).  
O servidor HTTP é construído "na mão", sem frameworks externos, para fins didáticos e práticos.

## Funcionalidades

- Listar usuários  
- Criar novo usuário  
- Editar usuário existente  
- Excluir usuário  
- Persistência simples usando arquivo texto

## Estrutura do Projeto

.
├── app.py # Arquivo principal que inicia o servidor
├── server/ # Módulo do servidor HTTP customizado
│ ├── server.py # Classe Server que gerencia o servidor
│ └── router.py # Roteamento das requisições HTTP
├── routes/ # Funções de tratamento das rotas
│ └── usuarios.py # Funções CRUD de usuários
├── usuarios.txt # Banco de dados simples em arquivo texto
└── README.md # Este arquivo de documentação


## Como rodar

1. Certifique-se de ter Python 3.12 (ou superior) instalado.  
2. (Opcional, mas recomendado) Crie e ative um ambiente virtual:


python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate

Execute o servidor:
    python app.py
Abra o navegador em http://localhost:8000/usuarios para acessar a lista de usuários.

## Dependências:
Nenhuma dependência externa.

Usa apenas bibliotecas padrão do Python.

## Possíveis melhorias
Validar entradas do usuário.

Usar banco de dados real (SQLite, MySQL, etc).

Adicionar interface web mais amigável.

Implementar métodos POST, PUT para formulários.

Usar framework como Flask para facilitar manutenção.

## Autor
João Augusto Pereira França