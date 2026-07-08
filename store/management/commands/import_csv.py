import csv
from django.core.management.base import BaseCommand
from store.models import Phone, Category

class Command(BaseCommand):
    help = "Импортирует реальные товары (смартфоны) из CSV-файла в базу данных."

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Очистить базу данных перед импортом',
        )

    def handle(self, *args, **options):
        csv_file_path = 'phones.csv'

        if options['clear']:
            self.stdout.write("Очистка базы данных перед импортом...")
            Phone.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("База данных успешно очищена."))

        try:
            with open(csv_file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                required_fields = ['name', 'brand', 'price', 'category', 'description', 'image_url', 'in_stock']
                for field in required_fields:
                    if field not in reader.fieldnames:
                        self.stdout.write(self.style.ERROR(f"Ошибка: В CSV отсутствует обязательное поле '{field}'"))
                        return

                count = 0
                for row in reader:
                    category_name = row['category'].strip()
                    category, _ = Category.objects.get_or_create(name=category_name)

                    in_stock = row['in_stock'].strip().lower() in ['true', '1', 'yes', 'y']

                    try:
                        price = float(row['price'].strip())
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Пропущена строка: Неверный формат цены для '{row['name']}'"))
                        continue

                    phone, created = Phone.objects.update_or_create(
                        name=row['name'].strip(),
                        defaults={
                            'brand': row['brand'].strip(),
                            'price': price,
                            'description': row['description'].strip(),
                            'image_url': row['image_url'].strip(),
                            'category': category,
                            'in_stock': in_stock,
                        }
                    )
                    
                    if created:
                        action = "Добавлен"
                    else:
                        action = "Обновлен"
                        
                    self.stdout.write(f"- {action}: {phone.brand} {phone.name} ({price} тг.)")
                    count += 1

                self.stdout.write(self.style.SUCCESS(f"Импорт успешно завершен. Обработано товаров: {count}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Файл '{csv_file_path}' не найден в корневом каталоге проекта."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Произошла непредвиденная ошибка при чтении файла: {e}"))
