# pizzeria

application pizzeria et commande en ligne avec stripe.
paiement stripe personnalisé

## pre-requis

- docker
- docker-compose
- un compte stripe

## installation

`git clone https://github.com/makan-dianka/pizzeria.git`

`cd pizzeria`

Créer le .env `touch .env`

ajouter ces variables d'environnement

```
SECRET_KEY='changemoi'
DEBUG=1

STRIPE_TEST_KEY="changemoi"
STRIPE_LIVE_KEY="changeme"

EMAIL_HOST_USER="changemoi"
EMAIL_HOST_PASSWORD="changemoi"

ALLOWED_HOST_DEV="127.0.0.1,localhost"
ALLOWED_HOST_PROD="changeme"
```

## Demarrer l'application

`docker-compose --env-file .env up`

## Faire la migration

```
docker exec pizzeria python manage.py makemigrations accounts pizzeria

docker exec pizzeria python manage.py migrate
```
