from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    descriptions_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name_category"]


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name="наименование")
    description_product = models.CharField(max_length=100, verbose_name="описание")
    image = models.ImageField(upload_to="media/photos/", verbose_name="фотография")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="категория"
    )
    purchase_price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата последнего изменения"
    )
    unpublish_product = models.BooleanField(
        default=False, verbose_name="статус публикации"
    )
    owner = models.ForeignKey(
        CustomUser,
        help_text="Укажите владельца продукта",
        null=True,
        blank=True,
        verbose_name="Владелец",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name_product"]
        permissions = [("can_unpublish_product", "Can unpublish product")]
