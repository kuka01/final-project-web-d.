from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import PhoneFilterForm, PhoneForm, RegisterForm, ReviewForm
from .mixins import ModeratorRequiredMixin
from .models import Category, Phone
from .product_specs import get_phone_detail_content
from .shop_offers import get_shop_offers

def home(request):
    latest_phones = Phone.objects.order_by("id")[:6]
    categories = Category.objects.all()
    return render(
        request,
        "store/home.html",
        {
            "latest_phones": latest_phones,
            "categories": categories,
            "total_phones": Phone.objects.count(),
        },
    )

def phone_list(request):
    phones = Phone.objects.select_related("category").order_by("id")
    form = PhoneFilterForm(request.GET or None)

    if form.is_valid():
        q = form.cleaned_data.get("q")
        category = form.cleaned_data.get("category")
        sort = form.cleaned_data.get("sort")

        if q:
            phones = phones.filter(name__icontains=q) | phones.filter(brand__icontains=q)
        if category:
            phones = phones.filter(category=category)
        if sort:
            phones = phones.order_by(sort)

    return render(request, "store/phone_list.html", {"phones": phones.distinct(), "form": form})

def favorites(request):
    phones = Phone.objects.select_related("category").order_by("id")
    return render(request, "store/favorites.html", {"phones": phones})

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    reviews = phone.reviews.all()
    average_rating = reviews.aggregate(value=Avg("rating"))["value"]

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Войдите в аккаунт, чтобы оставить отзыв.")
            return redirect("login")
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.phone = phone
            review.user = request.user
            review.save()
            messages.success(request, "Спасибо! Ваш отзыв опубликован.")
            return redirect("phone_detail", pk=phone.pk)
    else:
        review_form = ReviewForm()

    return render(
        request,
        "store/phone_detail.html",
        {
            "phone": phone,
            "reviews": reviews,
            "average_rating": average_rating,
            "review_form": review_form,
            "detail_content": get_phone_detail_content(phone),
            "shop_offers": get_shop_offers(phone),
        },
    )

class PhoneCreateView(ModeratorRequiredMixin, CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = "store/phone_form.html"
    extra_context = {"title": "Добавить новый телефон"}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Товар «{self.object.name}» успешно добавлен.")
        return response

    def get_success_url(self):
        return redirect("phone_detail", pk=self.object.pk).url

class PhoneUpdateView(ModeratorRequiredMixin, UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name = "store/phone_form.html"
    extra_context = {"title": "Редактировать телефон"}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Товар «{self.object.name}» успешно обновлён.")
        return response

    def get_success_url(self):
        return redirect("phone_detail", pk=self.object.pk).url

class PhoneDeleteView(ModeratorRequiredMixin, DeleteView):
    model = Phone
    template_name = "store/phone_confirm_delete.html"

    def form_valid(self, form):
        phone_name = self.object.name
        response = super().form_valid(form)
        messages.success(self.request, f"Товар «{phone_name}» успешно удалён.")
        return response

    def get_success_url(self):
        return redirect("phone_list").url

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("home")
        messages.error(request, "Не удалось зарегистрироваться. Проверьте форму.")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
