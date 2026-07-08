from django.conf import settings
from django.db import models
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

class Category(models.Model):
    
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Phone(models.Model):

    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True, help_text="Ссылка на изображение товара")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="phones")
    in_stock = models.BooleanField(default=True)
    shop_mechta_url = models.URLField(blank=True, default="", verbose_name="Mechta")
    shop_technodom_url = models.URLField(blank=True, default="", verbose_name="Technodom")
    shop_sulpak_url = models.URLField(blank=True, default="", verbose_name="Sulpak")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    @property
    def display_image_url(self):
        if not self.image_url:
            return ""

        parts = urlsplit(self.image_url)
        query = [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if key.lower() not in {"fit", "crop", "h", "height"}
        ]
        return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))

class Review(models.Model):
    
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Review by {self.user} on {self.phone}"

class Order(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.phone} x{self.quantity}"
