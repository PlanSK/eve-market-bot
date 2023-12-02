from peewee import SqliteDatabase, Model, CharField, IntegerField, ForeignKeyField, IntegrityError, chunked


class User(Model):
    id = IntegerField(primary_key=True)
    first_name = CharField()
    last_name = CharField(null=True)


class BaseItem(Model):
    id = IntegerField(primary_key=True)
    name_en = CharField()
    name_ru = CharField(null=True)


class Category(BaseItem):
    pass


class Group(Category):
    category = ForeignKeyField(Category, backref='groups')


class Item(BaseItem):
    group = ForeignKeyField(Group, backref='items')


class Command(Model):
    user = ForeignKeyField(User)
    command_text = CharField()
