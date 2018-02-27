#models.py

from django.db.models import Model, UUIDField, CharField, IntField, DateTimeField

class Product(Model):
    id = UUIDField(primary_key=True)
    name = CharField(max_length=45)
    description = CharField(max_length=45)
    brand = CharField(max_length=45)
    idprovider = IntField()


























