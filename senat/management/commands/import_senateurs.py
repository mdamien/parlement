import json, tqdm

from django.core.management.base import BaseCommand
from senat.models import Senateur


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='?')

    def handle(self, *args, **options):
        Senateur.objects.all().delete()
        data = json.load(open(options['file']))['results']
        senateurs = []
        slugs = set()
        for sen in tqdm.tqdm(data):
            slug = sen['Prenom_usuel'].lower().replace(' ', '-') + '-' + sen['Nom_usuel'].lower().replace(' ', '-')
            if slug in slugs:
                slug = sen['Matricule'] + '-' + slug
            print(slug)
            slugs.add(slug)
            sen['slug'] = slug
            senateurs.append(Senateur(**sen))
        Senateur.objects.bulk_create(senateurs)