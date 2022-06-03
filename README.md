# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver
1. Clone o repo.
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:assisthiago/wttd_eventex.git wttd_eventex
cd wttd_eventex
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy
1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina um SECRET_KEY segura para instância.
4. Defina o DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku create <minhainstancia>
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# Configuro o email
git push heroku master --force
```
