import logging
from os import path

from django.core.management import base

from fest_demo_main.models import Medication

logger = logging.getLogger(__name__)


class Command(base.BaseCommand):
    args = '<FEST data filename>'
    help = 'Imports data from a FEST data file.'

    def handle(self, *args, **options):
        if not args:
            raise base.CommandError('Usage: python manage.py importfest %s' % self.args)

        if not path.isfile(args[0]):
            raise base.CommandError('"%s" does not exist' % args[0])

        if Medication.objects.count():
            raise base.CommandError('Medication table is not empty')

        with open(args[0], 'r') as fest_data_file:
            count = 0
            for line in fest_data_file:
                name, atc_code = line.strip().split('\t')
                Medication.objects.create(name=name, atc_code=atc_code)
                count += 1

        logger.info('Imported %i rows into medication table')
