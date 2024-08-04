import uuid

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    level = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class SeasonalEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name


class Product(models.Model):
    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACKORDERED = "BO"
    
    STOCK_STATUS = {
        IN_STOCK: "In Stock",
        OUT_OF_STOCK: "Out of stock",
        BACKORDERED: "Back Ordered",
    }
    
    pid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    stock_status = models.CharField(
        max_length=3,
        choices=STOCK_STATUS,
        default=OUT_OF_STOCK,
    )
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    seasonal_event = models.ForeignKey(
        SeasonalEvent, on_delete=models.SET_NULL, null=True, blank=True
    )
    product_type = models.ManyToManyField('ProductType', through='Product_ProductType')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.attribute.name}: {self.attribute_value}"


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5, help_text="€")
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField(help_text="grams")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute_values = models.ManyToManyField('AttributeValue', through='ProductLine_AttributeValue')


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)


class ProductLine_AttributeValue(models.Model):
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)


class Product_ProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class StockControl(models.Model):
    stock_qty = models.IntegerField()
    name = models.CharField(max_length=100)
    stock_product = models.OneToOneField(Product, on_delete=models.CASCADE)
