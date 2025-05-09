# utils/management/commands/create_test_products.py

from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Создаёт тестовые товары'

    def handle(self, *args, **options):
        cat, _ = Category.objects.get_or_create(name="Солнцезащитные очки")

        for i in range(1, 6):
            Product.objects.create(
                name=f"Тестовый товар {i}",
                price=1000 * i,
                stock=10 + i,
                code_1c=f"CODE{i:03d}",
                slug=slugify(f"товар-{i}"),
            ).categories.add(cat)

        self.stdout.write(self.style.SUCCESS("✅ Тестовые товары созданы"))