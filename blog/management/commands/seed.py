from django.core.management.base import BaseCommand

from blog.tests.blog_factories import PostFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--posts',
                            default=50,
                            type=int,
                            help='The number of fake post to create.')

    def handle(self, *args, **options):
        PostFactory.create_batch(options['posts'])
