from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Создаёт группу Moderators, если она ещё не существует."

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Moderators")
        if created:
            self.stdout.write(self.style.SUCCESS("Группа Moderators создана."))
        else:
            self.stdout.write("Группа Moderators уже существует.")
