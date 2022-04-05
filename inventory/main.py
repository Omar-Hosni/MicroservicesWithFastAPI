from base64 import decode
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from numpy import integer, product
#from redis_om import get_redis_connection
from redis_om import HashModel,get_redis_connection

app = FastAPI()

#to import localhost:3000 to allow the frontend to request APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=["*"],
    allow_headers=["*"],
) 

redis = get_redis_connection(
    host="redis-16561.c293.eu-central-1-1.ec2.cloud.redislabs.com",
    port=16561,
    password="UkqTEeJGD9ClszXvKgJ4W9P2bH6XqVio",
    decode_responses=True
)

class Product(HashModel):
    name: str
    price: int
    quantity: int

    class Meta:
        database = redis


@app.get('/products')
def all():
    list_result = [(formatProduct(pk)) for pk in Product.all_pks()]
    return list_result

def formatProduct(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': int(product.price),
        'quantity': int(product.quantity)
    }


@app.post('/products')
def create(product: Product):
    return product.save()


@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)