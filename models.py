from peewee import (CharField, DateField, ForeignKeyField, IntegerField, Model,
                    SqliteDatabase)

db = SqliteDatabase('companies.db')


class Company(Model):
    name = CharField(unique=True)

    class Meta:
        database = db


class FactQliq(Model):
    company = ForeignKeyField(Company)
    data1 = IntegerField()
    data2 = IntegerField()
    total = IntegerField()
    date = DateField()

    class Meta:
        database = db


class FactQoil(Model):
    company = ForeignKeyField(Company)
    data1 = IntegerField()
    data2 = IntegerField()
    total = IntegerField()
    date = DateField()

    class Meta:
        database = db


class ForecastQliq(Model):
    company = ForeignKeyField(Company)
    data1 = IntegerField()
    data2 = IntegerField()
    total = IntegerField()
    date = DateField()

    class Meta:
        database = db


class ForecastQoil(Model):
    company = ForeignKeyField(Company)
    data1 = IntegerField()
    data2 = IntegerField()
    total = IntegerField()
    date = DateField()

    class Meta:
        database = db