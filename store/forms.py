from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Phone, Review, Category
from .shop_offers import MECHTA_PRODUCTS, TECHNODOM_OFFERS, SULPAK_OFFERS

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text="Понадобится для восстановления доступа")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

class PhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = ["name", "brand", "price", "category", "image_url", "in_stock", "description", "shop_mechta_url", "shop_technodom_url", "shop_sulpak_url"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Например, iPhone 17 Pro"}),
            "brand": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apple, Samsung, Xiaomi..."}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://..."}),
            "in_stock": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "shop_mechta_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.mechta.kz/..."}),
            "shop_technodom_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.technodom.kz/..."}),
            "shop_sulpak_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://www.sulpak.kz/..."}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.name:
            mecha = MECHTA_PRODUCTS.get(self.instance.name, "")
            td = TECHNODOM_OFFERS.get(self.instance.name)
            sp = SULPAK_OFFERS.get(self.instance.name)
            if not self.instance.shop_mechta_url and mecha:
                self.initial["shop_mechta_url"] = mecha
            if not self.instance.shop_technodom_url and td:
                self.initial["shop_technodom_url"] = td["url"]
            if not self.instance.shop_sulpak_url and sp:
                self.initial["shop_sulpak_url"] = sp["url"]

class PhoneFilterForm(forms.Form):
    
    q = forms.CharField(
        required=False,
        label="Поиск",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Название или бренд...",
            "id": "live-search-input",
        }),
    )
    category = forms.ModelChoiceField(
        required=False,
        label="Категория",
        queryset=Category.objects.all(),
        empty_label="Все категории",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    sort = forms.ChoiceField(
        required=False,
        label="Сортировать",
        choices=[
            ("", "По умолчанию"),
            ("price", "Цена: сначала дешевле"),
            ("-price", "Цена: сначала дороже"),
            ("-created_at", "Сначала новинки"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

class ReviewForm(forms.ModelForm):
    

    class Meta:
        model = Review
        fields = ["text", "rating"]
        labels = {
            "rating": "Оценка",
            "text": "Текст",
        }
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control review-textarea", "rows": 4, "placeholder": "Поделитесь впечатлением о телефоне..."}),
            "rating": forms.Select(choices=[(i, f"{i} ★") for i in range(1, 6)], attrs={"class": "form-control"}),
        }
