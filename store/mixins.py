from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class ModeratorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    

    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.groups.filter(name="Moderators").exists()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("Доступ запрещён. Требуются права модератора.")
        return super().handle_no_permission()
