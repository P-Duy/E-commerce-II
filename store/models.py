from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    category_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_creator"
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    slug = models.SlugField(max_length=255, unique=True, default="default-slug")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("store:products_detail", args=[self.slug])

    def __str__(self) -> str:
        return self.title
