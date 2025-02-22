# NoteBook Django Project

Este é um projeto de aplicação web de anotações desenvolvido com Django. A aplicação permite que os usuários criem, editem e excluam notas associadas a suas contas.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
NoteBook-Django-project/ 
├── manage.py 
├── note_book/ 
│   ├── __init__.py 
│   ├── asgi.py
│   ├── settings.py 
│   ├── urls.py 
│   └── wsgi.py 
├── notes/ 
│   ├── __init__.py 
│   ├── admin.py 
│   ├── apps.py 
│   ├── models.py 
│   ├── templates/ 
│   │   └── notes/ 
│   │       ├── add_note.html
│   │       ├── notes.html
│   │       └── update_note.html
│   ├── tests.py 
│   ├── urls.py 
│   └── views.py 
└── user/ 
    ├── __init__.py 
    ├── admin.py 
    ├── apps.py 
    ├── models.py 
    ├── templates/ 
    │   └── user/ 
    │       ├── login.html 
    │       └── register.html 
    ├── tests.py 
    ├── urls.py 
    └── views.py
```

## Funcionalidades

- **Cadastro de Usuário**: Os usuários podem se registrar fornecendo nome, email e senha.
- **Login de Usuário**: Os usuários podem fazer login usando seu email e senha.
- **Gerenciamento de Notas**: Os usuários podem adicionar, editar e excluir notas.
- **Visualização de Notas**: Os usuários podem visualizar todas as suas notas em uma lista.

## Instalação

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd NoteBook-Django-project
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

6. Acesse a aplicação em [http://127.0.0.1:8000/](http://_vscodecontentref_/33).

## Uso

- **Cadastro**: Acesse [user](http://_vscodecontentref_/34) para se registrar.
- **Login**: Acesse `/user/login` para fazer login.
- **Notas**: Após o login, acesse `/notes/<user_id>/` para visualizar suas notas, adicionar novas notas, editar ou excluir notas existentes.

## Contribuição

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.