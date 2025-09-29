import os
import django

# tell Django which settings to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from django.contrib.auth.models import User
from Library.models import Book, Student, IssuedBook
from faker import Faker
import random

fake = Faker()

# Example seeding logic
for _ in range(5):
    username = fake.unique.user_name()
    user = User.objects.create_user(
        username=username,
        email=fake.unique.email(),
        password="password123"
    )
    Student.objects.create(
        user=user,
        classroom=fake.random_element(elements=("A1", "B1", "C2", "D2")),
        branch=fake.word(),
        roll_no=str(fake.random_int(min=1, max=999)).zfill(3),
        phone=fake.msisdn()[:10],
    )

print("✅ Database populated successfully!")
