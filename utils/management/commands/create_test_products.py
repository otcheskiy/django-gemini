from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Создаёт тестовые товары'

    def handle(self, *args, **options):
        cat, _ = Category.objects.get_or_create(name="Оправы")

        for i in range(1, 6):
            product = Product.objects.create(
                name=f"Оправы {i}",
                price=1000 * i,
                stock=10 + i,
                code_1c=f"Oprav{i:03d}",
                # slug создаётся автоматически в методе save()
            )
            product.categories.add(cat)

        self.stdout.write(self.style.SUCCESS("✅ Тестовые товары созданы"))