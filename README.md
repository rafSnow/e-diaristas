# Projeto e-diarista

### Instalando o projeto


#### Clonar o Projeto
`git clone https://github.com/rafSnow/e-diaristas.git`

#### Instalar dependências
`pip install -r requirements.txt`

#### Alterar configurações do BD no arquivo `settings.py`
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "<nome_do_banco_de_dados>",
        "HOST": "<host_do_bd>",
        "PORT": <porta>,
        "USER": "<usuario>",
        "PASSWORD": "<senha>"
    }
}
```
 
#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar o Servidor
`python manage.py runserver`