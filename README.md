# Django Blog

![Django Blog](https://img.shields.io/badge/Django-Blog-blue.svg)

Django Blog é um projeto de blog desenvolvido com o framework Django. Ele permite a criação, edição e exibição de postagens, fornecendo uma plataforma simples para compartilhar conteúdos online.

## 🚀 Funcionalidades

- 📌 Criar, editar e excluir posts
- 🔎 Sistema de categorias e tags
- 💬 Comentários nos posts
- 🔒 Autenticação de usuários
- 📊 Painel administrativo do Django
- 📅 Publicação programada

## 📦 Tecnologias Utilizadas

- 🐍 Python 3
- 🌍 Django
- 🔢 SQLite (ou outro banco de dados suportado pelo Django)
- 🎨 HTML, CSS e Bootstrap

## 🎯 Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes itens instalados:

- Python 3.x
- Git
- Virtualenv (opcional, mas recomendado)

## 📥 Instalação

Clone o repositório e instale as dependências:

```bash
# Clonar o repositório
git clone https://github.com/henrickym13/django-blog.git
cd django-blog

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

## ⚙️ Configuração

1. Crie um arquivo `.env` e configure as variáveis de ambiente (caso necessário).
2. Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

3. Crie um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

4. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

O blog estará disponível em `http://127.0.0.1:8000/`.

## 📸 Capturas de Tela

(home_screen.png)

## 🤝 Contribuição

Sinta-se à vontade para contribuir com o projeto! Para isso:

1. Faça um fork do repositório
2. Crie uma branch com sua feature (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Adicionando minha feature'`)
4. Faça push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request


---

💡 **Dúvidas ou sugestões?** Entre em contato ou abra uma issue!

📧 Contato: henrique.so.ad@hotmail.com
