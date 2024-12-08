from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "image",
            "name_product",
            "category",
            "description_product",
            "purchase_price",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["image"].widget.attrs.update({"class": "form-group"})

        self.fields["name_product"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название продукта"}
        )

        self.fields["category"].widget.attrs.update({"class": "form-check"})

        self.fields["description_product"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["purchase_price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите цену продукта"}
        )

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get("purchase_price")
        if purchase_price < 0:
            raise ValidationError("Цена не может быть отрицательным значением")

        return purchase_price

    def clean(self):
        cleaned_data = super().clean()
        name_product = cleaned_data.get("name_product")
        description_product = cleaned_data.get("description_product")

        bad_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        if name_product.lower() in bad_words:
            self.add_error("name_product", "Такие слова нельзя здесь использовать!")

        if description_product.lower() in bad_words:
            self.add_error(
                "description_product", "Такие слова нельзя здесь использовать!"
            )


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["unpublish_product"]
