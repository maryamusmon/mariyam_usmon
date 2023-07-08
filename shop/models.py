from django.db.models import Model, CharField, IntegerField, TextChoices, TextField, JSONField, ForeignKey, CASCADE, \
    ImageField, SmallIntegerField, DateTimeField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=200)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(Model):
    # class SizeChoices(TextChoices):
    #     s = 'Small', 'S'
    #     m = 'Medium', 'M'
    #     l = 'Large', 'L'
    #     xl = 'Extra Large', 'XL'

    title = CharField(max_length=200)
    price = IntegerField()
    # size = CharField(max_length=20, choices=SizeChoices.choices, default=SizeChoices.s)
    size = CharField(max_length=200)
    brend = CharField(max_length=200, null=True, blank=True)
    quantity = IntegerField(default=0)
    views = IntegerField(default=0, null=True, blank=True)
    description = TextField()
    specification = JSONField(default=dict, blank=True)
    avaible_color = CharField(max_length=200, null=True, blank=True)
    category = ForeignKey(Category, CASCADE)
    author = ForeignKey('auth.User', CASCADE)
    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImage(Model):
    image = ImageField(upload_to='photos/')
    product = ForeignKey(Product, CASCADE)


class Cart(Model):
    product = ForeignKey('shop.Product', CASCADE)
    price = IntegerField()
    quantity = IntegerField(default=0)
    user = ForeignKey('auth.User', CASCADE)


class Comment(Model):
    product = ForeignKey('shop.Product', CASCADE)
    text = TextField(max_length=255)
    star = SmallIntegerField(default=0)
    author = ForeignKey('auth.User', CASCADE)
    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)
