from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from store.models import Category, Phone

POPULAR_MECHTA_PHONES = [
    {
        "name": "Samsung Galaxy A56 5G 128GB Awesome Lightgray (SM-A566) EZAAS",
        "brand": "Samsung",
        "price": 179990,
        "category": "Средний сегмент",
        "description": "Популярная модель из каталога Mechta.kz: Galaxy A56 5G с 128GB памяти.",
        "image_url": "https://pi.mdev.kz/5e72a5ef-5a59-42e3-bd26-523ae75f59ca?type=webp&w=360&h=360",
    },
    {
        "name": "HONOR 600 Pro (12/512GB) Orange",
        "brand": "HONOR",
        "price": 549990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: HONOR 600 Pro с 512GB памяти.",
        "image_url": "https://pi.mdev.kz/8c25e3bd-18d7-479a-872a-53392871ebf9?type=webp&w=360&h=360",
    },
    {
        "name": "APPLE iPhone 17 Pro Max 256GB (Silver)",
        "brand": "Apple",
        "price": 898990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: iPhone 17 Pro Max на 256GB.",
        "image_url": "https://pi.mdev.kz/791795b8-ce30-42b2-92b3-b803846589ac?type=webp&w=360&h=360",
    },
    {
        "name": "Apple iPhone 16 128GB (Pink)",
        "brand": "Apple",
        "price": 515990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: iPhone 16 на 128GB.",
        "image_url": "https://pi.mdev.kz/b12b3793-7714-11ef-a269-005056b6e990?type=webp&w=360&h=360",
    },
    {
        "name": "APPLE iPhone 17 Pro 256GB (Silver)",
        "brand": "Apple",
        "price": 836990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: iPhone 17 Pro на 256GB.",
        "image_url": "https://pi.mdev.kz/4610a9f4-df74-43d7-bea4-e9ebabf8f16b?type=webp&w=360&h=360",
    },
    {
        "name": "HONOR 600 (8/256GB) Orange",
        "brand": "HONOR",
        "price": 329990,
        "category": "Средний сегмент",
        "description": "Популярная модель из каталога Mechta.kz: HONOR 600 с 256GB памяти.",
        "image_url": "https://pi.mdev.kz/a9bde911-9690-43cb-9185-2ed3536c744b?type=webp&w=360&h=360",
    },
    {
        "name": "Apple iPhone 15 128GB (Pink)",
        "brand": "Apple",
        "price": 443990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: iPhone 15 на 128GB.",
        "image_url": "https://pi.mdev.kz/6cb62cda-5394-11ee-a261-005056b6dbd7?type=webp&w=360&h=360",
    },
    {
        "name": "APPLE iPhone 17 Pro Max 2TB (Cosmic Orange)",
        "brand": "Apple",
        "price": 1522990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: iPhone 17 Pro Max на 2TB.",
        "image_url": "https://pi.mdev.kz/307b259a-45de-4d93-8892-f68f82008051?type=webp&w=360&h=360",
    },
    {
        "name": "Apple iPhone 15 128GB (Black)",
        "brand": "Apple",
        "price": 443990,
        "category": "Флагманы",
        "description": "Популярная модель из каталога Mechta.kz: iPhone 15 на 128GB.",
        "image_url": "https://pi.mdev.kz/d44e83f3-5382-11ee-a261-005056b6dbd7?type=webp&w=360&h=360",
    },
    {
        "name": "Xiaomi Redmi Note 13 Pro+ 5G 12/512GB Midnight Black",
        "brand": "Xiaomi",
        "price": 199990,
        "category": "Средний сегмент",
        "description": "Популярная модель из каталога Mechta.kz: Redmi Note 13 Pro+ 5G с 512GB памяти.",
        "image_url": "https://pi.mdev.kz/228f5cec-b357-11ee-a264-005056b6dbd7?type=webp&w=360&h=360",
    },
    {
        "name": "Samsung Galaxy A26 5G 256GB White (SM-A266) BZWHS",
        "brand": "Samsung",
        "price": 149990,
        "category": "Бюджетные",
        "description": "Бюджетная модель из каталога Mechta.kz: Galaxy A26 5G с 256GB памяти.",
        "image_url": "https://pi.mdev.kz/e484967d-055b-4052-911e-e9e15b7ce232?type=webp&w=360&h=360",
    },
    {
        "name": "OPPO A6 (8/256) Aurora Gold",
        "brand": "OPPO",
        "price": 164990,
        "category": "Бюджетные",
        "description": "Бюджетная модель из каталога Mechta.kz: OPPO A6 с 8GB RAM и 256GB памяти.",
        "image_url": "https://pi.mdev.kz/90adf828-bb5e-4ce7-a354-1466b21b397e?type=webp&w=360&h=360",
    },
]

class Command(BaseCommand):
    help = "Заполняет базу 10 популярными смартфонами из каталога Mechta.kz."

    def handle(self, *args, **options):
        Phone.objects.all().delete()

        categories = {
            name: Category.objects.get_or_create(name=name)[0]
            for name in ["Флагманы", "Средний сегмент", "Бюджетные"]
        }

        for item in POPULAR_MECHTA_PHONES:
            Phone.objects.create(
                name=item["name"],
                brand=item["brand"],
                price=item["price"],
                category=categories[item["category"]],
                in_stock=True,
                description=item["description"],
                image_url=item["image_url"],
            )

        if not User.objects.filter(username="demo").exists():
            User.objects.create_user("demo", password="demo12345")
            self.stdout.write(self.style.SUCCESS("Создан демо-пользователь: demo / demo12345"))

        self.stdout.write(self.style.SUCCESS(f"Готово. Товаров в базе: {Phone.objects.count()}"))
