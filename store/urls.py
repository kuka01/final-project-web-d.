from django.contrib.auth import views as auth_views
from django.urls import path

from . import views, api_views
from .forms import LoginForm

urlpatterns = [
    path("", views.home, name="home"),
    path("phones/", views.phone_list, name="phone_list"),
    path("favorites/", views.favorites, name="favorites"),
    path("phones/<int:pk>/", views.phone_detail, name="phone_detail"),
    path("phones/new/", views.PhoneCreateView.as_view(), name="phone_create"),
    path("phones/<int:pk>/edit/", views.PhoneUpdateView.as_view(), name="phone_edit"),
    path("phones/<int:pk>/delete/", views.PhoneDeleteView.as_view(), name="phone_delete"),

    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),

    path("api/login/", api_views.api_login, name="api_login"),
    path("api/logout/", api_views.api_logout, name="api_logout"),
    path("api/register/", api_views.UserRegisterView.as_view(), name="api_register"),

    path("api/categories/", api_views.api_category_list, name="api_categories"),
    path("api/categories/<int:pk>/", api_views.api_category_detail, name="api_category_detail"),

    path("api/phones/", api_views.api_phone_list_readonly, name="api_phone_list"),
    path("api/phones/<int:pk>/", api_views.api_phone_detail_readonly, name="api_phone_detail"),

    path("api/phones/manage/", api_views.PhoneListAPIView.as_view(), name="api_phone_manage_list"),
    path("api/phones/manage/<int:pk>/", api_views.PhoneDetailAPIView.as_view(), name="api_phone_manage_detail"),

    path("api/reviews/", api_views.ReviewListCreateAPIView.as_view(), name="api_review_list"),
    path("api/reviews/<int:pk>/", api_views.api_review_detail, name="api_review_detail"),
    path("api/phones/<int:pk>/reviews/", api_views.api_phone_reviews, name="api_phone_reviews"),

    path("api/orders/", api_views.OrderListCreateAPIView.as_view(), name="api_order_list"),
    path("api/orders/<int:pk>/", api_views.api_order_detail, name="api_order_detail"),
]
