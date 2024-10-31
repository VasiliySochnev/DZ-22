from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name_category='Выпечка', descriptions_category='Торты и пироги')

        products = [
            {'name_product': 'Торт Наполеон', 'description_product': 'Торты Яковлева', 'image': 'photos/',
             'category': category, 'purchase_price': 200.50},
            {'name_product': 'Пирог с капустой', 'description_product': 'Пироги бабы Маши', 'image': 'photos/',
             'category': category, 'purchase_price': 20.50}
        ]

        for products_data in products:
            product, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name_product} {product.description_product}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name_product} {product.description_product}'))