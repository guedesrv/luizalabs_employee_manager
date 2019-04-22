# Luizalabs Teste

## Informações Técnicas

Esta aplicação foi desenvolvida utilizando as tecnologias:

* [Python 3.6](https://www.python.org/)
* [Django 2.2](https://www.djangoproject.com/)
* [Django REST framework 3.9](https://www.django-rest-framework.org/)

**OBS: Considerando que tenha um ambiente virtualizado pronto para uso.**

Rodar o comando para instalar as dependências:

```
pip install -r requirements.txt
```

Rodar o comando para criar o DB:
```
python manage.py migrate
```

Comando para iniciar com os dados de acesso:
```
python manage.py loaddata fixtures/initial_user.json
```
```
python manage.py loaddata fixtures/initial_employee.json
```

Rodar a aplicação:
```
python manage.py runserver
```

Acessar no browser:

`http://localhost:8000/employee/`

#### Acesso admin ####

`http://localhost:8000/admin`

usuário: `Luizalabs`
senha: `123456`

## Teste:

Rodar o comando para realizar os testes:
```
pytest
```

## Opção adicional:

Caso queira paginar as requisições, alterar variável `REST_FRAMEWORK` abaixo no arquivo `luizalabs_employee_manager/settings.py`, onde `PAGE_SIZE` é a quantidade de registros por página:
```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}
```
***Reiniciar a aplicação***
