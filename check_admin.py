import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_accelartor.settings')
django.setup()

from django.contrib.auth.models import User

admin_users = User.objects.filter(is_superuser=True)
print(f"Admin users count: {admin_users.count()}")
for user in admin_users:
    print(f"Username: {user.username}, Email: {user.email}, Is Staff: {user.is_staff}, Is Active: {user.is_active}")

all_users = User.objects.all()
print(f"\nTotal users count: {all_users.count()}")
for user in all_users:
    print(f"Username: {user.username}, Email: {user.email}, Is Superuser: {user.is_superuser}, Is Staff: {user.is_staff}")
