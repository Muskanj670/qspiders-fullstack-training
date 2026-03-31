import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')

import django
django.setup()

from faker import Faker
f = Faker()

from modelapp.models import StudentModel
def populate(n):
    for i in range(n):
        name = f.name()
        roll = f.random_int(min=1, max=1000)
        subject = f.word()
        email = f.email()
        address = f.address()
        StudentModel.objects.create(name = name,roll= roll, subject= subject, email = email, address = address)

n = int(input("Enter a number: "))
populate(n)
print(f'{n} record created Successfully')
        

from trainerapp.models import TrainerModel
subjects = ['Python', 'Django', 'JavaScript', 'React', 'Angular', 'Node.js', 'Java', 'C++', 'C#', 'Ruby']
def populate(n):
    for i in range(n):
        name = f.name()
        subject = f.random.choice(subjects)
        email = f.email()
        address = f.address()
        TrainerModel.objects.create(name = name, subject= subject, email = email, address = address)

n = int(input("Enter a number: "))
populate(n)
print(f'{n} record created Successfully')
        