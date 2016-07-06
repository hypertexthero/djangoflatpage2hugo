# _*_ coding:utf-8 _*_
from django.core.management.base import BaseCommand
from django.contrib.flatpages.models import FlatPage
import os
import re
from django.utils.text import slugify
# Thanks to http://stackoverflow.com/a/15364584/412329 for:
from django.utils.encoding import smart_str, smart_unicode

class Command(BaseCommand):
    """ 
    Usage: 
    1. Put this file in: 
    yourdjangoproject/
                management/
                        commands/
                                djangoflatpages2hugo.py
    2. Make sure there are __init__.py files in both management and commands folders
    3. Run: python manage.py djangoflatpages2hugo /chosen/output/directory/
    4. Find the converted .md files in /chosen/output/directory
    """
    help = 'Export hth flat pages as Hugo markdown files'

    def add_arguments(self, parser):
        parser.add_argument('output_dir', help='Output directory.')

    def handle(self, *args, **options):
        for page in FlatPage.objects.all():
            header = {
                'date': '2000-01-01',
                'title': page.title.replace(':', ''),
                # change /design/ to your section url
                'url': '/design/' + slugify(page.title) + '/',
            }
            
            output_dir = args[0]
            filename = '{slug}.markdown'.format(slug=slugify(page.title))
            
            content = page.content.encode('utf-8').replace('\r', '')
            
            # Write out the file
            with open(os.path.join(output_dir, filename), 'w') as fp:
                fp.write('---' + os.linesep)
                for k, v in header.items():
                    fp.write(smart_str('%s: %s%s' % (k, v, os.linesep)))
                fp.write('---' + os.linesep)
                fp.write(smart_str(content))
