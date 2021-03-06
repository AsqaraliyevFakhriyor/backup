from django.db import models

# Create your models here.

# Promotion - Product
class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount =models.FloatField()

# Collection model of store
class Collection(models.Model):
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, related_name = "featured_product")


# Product model of store
class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(
        Collection, on_delete = models.PROTECT
        )
    promotion = models.ManyToManyField(
        Promotion,
        # related_name = "products"
    )


# Customers model of store
class Customer(models.Model):
    MEMBERSHIP_CHOICES = (
        ("B", "Bronze"),
        ("S", "Silver"),
        ("G", "Gold"),
    )
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = "B")


# Orders model of store
class Order (models.Model):
    PAYMENT_STATUS_CHOICES = (
        ("P", "Pending"),
        ("C", "Complete"),
        ("F", "Failed"),
    )    
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS_CHOICES, default = "P")
    customer = models.ForeignKey(
        Customer, on_delete = models.PROTECT
    )
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)


# Address model of store
class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customer = models.ForeignKey(
        Customer, on_delete = models.CASCADE)


# Cart model of store
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()