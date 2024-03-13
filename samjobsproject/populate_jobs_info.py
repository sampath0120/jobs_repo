import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","samjobsproject.settings")
import django
django.setup()

from testapp.models import hydjobs,bangulorjobs,punejobs
from faker import Faker
from random import *

def phnogen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)          #randint means choose the randomly one number
def populate(n):
    for i in range(n):
        fake=Faker()
        finterviewdate=fake.date()
        fcompanyname=fake.company()
        ftittle=fake.random_element(elements=('assistant manager','software developer','frontend developer'))
        fqualification=fake.random_element(elements=('MBA','MTECH','BTECH','phd'))
        faddress=fake.address()
        femail=fake.email()
        fphno=phnogen()
        hydjobs.objects.get_or_create(interviewdate=finterviewdate,
        companyname=fcompanyname,
        tittle=ftittle,
        qualification=fqualification,
        address=faddress,
        email=femail,
        phno=fphno)
        bangulorjobs.objects.get_or_create(interviewdate=finterviewdate,companyname=fcompanyname,tittle=ftittle,qualification=fqualification,address=faddress,email=femail,phno=fphno)
        punejobs.objects.get_or_create(interviewdate=finterviewdate,companyname=fcompanyname,tittle=ftittle,qualification=fqualification,address=faddress,email=femail,phno=fphno)
n=int(input("enter no of records you want:"))
populate(n)
print(f'{n} you have been entered records inserted successfully')
