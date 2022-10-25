import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            slug_v1 = list(phone['name'].lower().split(' '))[:2]
            slug = '-'.join(slug_v1)
            print(phone)
            Phone(name=phone['name'], price=phone['price'], image=phone['image'], release_date=phone['release_date'], lte_exists=phone['lte_exists'], slug=slug).save()
