from django.db import models
from django import forms


class users(models.Model):
    email = models.CharField(max_length=20, primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"


class products(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "products"


class transactions(models.Model):
    tran_id = models.CharField(max_length=5, primary_key=True)
    prod_id = models.CharField(max_length=5)
    email = models.CharField(max_length=20)
    cardnum = models.CharField(max_length=25)
    cardcode = models.CharField(max_length=20)


    def __str__(self):
        return self.tran_id

    class Meta:
        db_table = "transactions"