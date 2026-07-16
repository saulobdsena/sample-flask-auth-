# Sample Flask Auth 🔐

Uma aplicação modelo (boilerplate) em Python utilizando o framework **Flask** para demonstrar fluxos de autenticação e autorização robustos, seguros e fáceis de estender. Este projeto serve como um ponto de partida ideal para desenvolvedores que desejam implementar sistemas de login, registro e rotas protegidas em suas aplicações web.

---

## 🚀 Funcionalidades

- **Registro de Usuários:** Cadastro seguro com validação de campos.
- **Autenticação Segura:** Login e logout gerenciados de forma robusta utilizando sessões seguras.
- **Criptografia de Senhas:** Hashing de senhas utilizando algoritmos modernos e seguros (ex: `bcrypt` ou `scrypt` via Werkzeug).
- **Controle de Acesso:** Proteção de rotas utilizando decoradores para restringir o acesso apenas a usuários autenticados.
- **Banco de Dados Relacional:** Integração com banco de dados usando **Flask-SQLAlchemy** (SQLite pré-configurado para desenvolvimento).
- **Proteção CSRF:** Segurança contra ataques Cross-Site Request Forgery em formulários.
- **Layout Responsivo:** Páginas de login, cadastro e dashboard construídas com design limpo e intuitivo.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as melhores ferramentas e bibliotecas do ecossistema Python:

- **[Flask](https://flask.palletsprojects.com/):** Micro-framework web rápido e flexível.
- **[Flask-Login](https://flask-login.readthedocs.io/):** Gerenciamento de sessões de usuários.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/):** ORM para abstração e comunicação com o banco de dados.
- **[Werkzeug](https://werkzeug.palletsprojects.com/):** Utilitários de segurança para hashing de senhas.
- **[SQLite](https://www.sqlite.org/):** Banco de dados relacional leve para desenvolvimento ágil.

---

## 📁 Estrutura do Projeto

Abaixo está a organização de pastas recomendada e utilizada neste projeto:

```text
sample-flask-auth/
├── app/
│   ├── __init__.py          # Inicialização do app, configurações e extensões
│   ├── models.py            # Definição dos modelos de banco de dados (User)
│   ├── routes.py            # Rotas e controladores da aplicação (Auth, Dashboard)
│   ├── templates/           # Arquivos HTML da interface do usuário
│   │   ├── base.html        # Template base (layout comum)
│   │   ├── index.html       # Página inicial pública
│   │   ├── login.html       # Tela de login
│   │   ├── register.html    # Tela de cadastro de usuários
│   │   └── dashboard.html   # Área protegida exclusiva para logados
│   └── static/              # Arquivos estáticos (CSS, JS, Imagens)
│       └── css/
│           └── style.css    # Estilização customizada
├── .env.example             # Exemplo de variáveis de ambiente
├── requirements.txt         # Dependências do projeto
└── run.py                   # Script principal para iniciar o servidor
```

---

## ⚙️ Pré-requisitos e Instalação

Siga os passos abaixo para clonar, configurar e rodar o projeto localmente em sua máquina.

### 1. Clonar o Repositório
```bash
git clone https://github.com/saulobdsena/sample-flask-auth-.git
cd sample-flask-auth-
```

### 2. Configurar o Ambiente Virtual (Virtualenv)
Recomenda-se o uso de um ambiente virtual para isolar as dependências:

No **Linux/macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

No **Windows** (Command Prompt):
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativo, instale os pacotes necessários listados no arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Variáveis de Ambiente
Renomeie ou copie o arquivo `.env.example` para `.env` e configure suas variáveis:
```bash
cp .env.example .env
```
Abra o arquivo `.env` e defina uma chave secreta segura para a aplicação:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-altamente-segura
DATABASE_URL=sqlite:///app.db
```

### 5. Inicializar o Banco de Dados
A aplicação criará automaticamente o arquivo do banco de dados SQLite ao ser executada pela primeira vez. Caso queira criar as tabelas manualmente via terminal interativo do Python:
```bash
python -c "from app import db, create_app; db.create_all(app=create_app())"
```

---

## 🏃 Como Executar a Aplicação

Inicie o servidor de desenvolvimento do Flask utilizando o comando:
```bash
flask run
```
Ou alternativamente executando o arquivo principal:
```bash
python run.py
```

A aplicação estará disponível no endereço: **[http://127.0.0.1:5000](http://127.0.0.1:5000)** 🚀

---

## 🔒 Endpoints e Rotas Disponíveis

| Método | Rota | Descrição | Acesso |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Página de boas-vindas da aplicação | Público |
| `GET` / `POST` | `/register` | Tela de cadastro de novos usuários | Público |
| `GET` / `POST` | `/login` | Autenticação e login de usuários | Público |
| `GET` | `/logout` | Encerramento da sessão atual do usuário | Autenticado |
| `GET` | `/dashboard` | Área administrativa protegida | Autenticado |

---

## 🛡️ Melhores Práticas Implementadas

- **Proteção de Senhas:** Nenhuma senha é guardada em texto plano. O projeto utiliza hashes criptográficos unidirecionais de última geração.
- **Gestão de Sessão Segura:** Proteção contra ataques de fixação de sessão. Os identificadores de sessão são armazenados em cookies criptografados.
- **Princípio do Menor Privilégio:** Rotas sensíveis possuem o decorator `@login_required` para garantir que apenas usuários verificados tenham acesso aos dados.

---

## 📄 Licença

Este projeto é de código aberto e está licenciado sob os termos da licença **[MIT](LICENSE)**. Sinta-se livre para usá-lo, modificá-lo e distribuí-lo como preferir.