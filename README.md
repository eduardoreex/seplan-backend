API SEPLAN-PI - Sistema de Gestão de Territórios e Cidades

Repositório oficial do teste técnico para a vaga de Estágio em Desenvolvimento Backend na Secretaria de Planejamento do Estado do Piauí (SEPLAN-PI).

Este projeto consiste numa API REST para a gestão da divisão territorial e municipal do Estado, focada em integridade de dados e facilidade de consumo.

Stack Tecnológica:

Linguagem: Python 3.12+

Framework Web: Django 5.0

API Engine: Django Ninja (Framework moderno e de alta performance, inspirado no FastAPI)

Banco de Dados: SQLite (Persistência local para agilidade de avaliação)

Documentação: Swagger UI (OpenAPI 3.0)

Desafios Implementados (Tasks)

✅ Task 1: CRUD de Territórios de Desenvolvimento

Implementação completa das operações de listagem, criação, edição e remoção dos territórios (Ex: Entre Rios, Planície Litorânea, etc).

✅ Task 2: CRUD de Cidades com Filtros Avançados

Chave Primária Customizada: Utilização do codigo_ibge (7 dígitos) como Identificador Único, garantindo conformidade com padrões governamentais.

Relacionamento Aninhado: A listagem de cidades retorna o objeto completo do território vinculado, facilitando o consumo pelo Frontend sem necessidade de múltiplas requisições.

Filtros de Busca:

Busca por trecho do nome (utilizando icontains).

Filtro por ID do Território.

✅ Task 3: Documentação e Testes (Postman)

Coleção completa exportada com exemplos de requisições de sucesso para cada funcionalidade.

ESTRUTURA DO PROJETO

seplan-backend/
├── core/               # Aplicação principal (Models, Schemas, API)
│   ├── api.py          # Roteamento e Lógica de Negócio (Django Ninja)
│   ├── models.py       # Definição das Tabelas no Banco de Dados
│   └── schemas.py      # Contratos de Entrada e Saída (Pydantic/Ninja)
├── setup/              # Configurações do Projeto Django
├── postman_collection.json # Arquivo para importação no Postman
├── requirements.txt    # Dependências do sistema
└── manage.py           # Utilitário de comando do Django


COMO EXECUTAR O PROJETO:

1- Preparação do Ambiente

# Clonar o repositório
git clone [https://github.com/eduardoreex/seplan-backend.git](https://github.com/eduardoreex/seplan-backend.git)
cd seplan-backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
.\venv\Scripts\Activate

2- Instalação e Banco de Dados

# Instalar dependências
pip install -r requirements.txt

# Executar as migrações para criar as tabelas
python manage.py migrate

3- Inicialização

python manage.py runserver

A API estará disponível em: http://127.0.0.1:8000/api/docs
(Acesse para testar os endpoints diretamente pelo navegador via Swagger)

Testando com Postman (Task 3)

Abra o Postman.

Clique em Import.

Selecione o arquivo postman_collection.json na raiz deste repositório.

As pastas CRUD de Territórios e CRUD de Cidades estarão configuradas com as URLs corretas e corpos de requisição prontos para teste.

AUTOR

Eduardo Oliveira

Fundador e Lead Developer na Reex AI Digital

Graduando em Engenharia de Software (iCEV - Instituto de Ensino Superior)

Graduando em Inteligência Artificial Aplicada (PUCPR)