from optparse import make_option
from django.core.management.base import BaseCommand

from linkcheck.utils import get_suggestions
from linkcheck.linkcheck_settings import MAX_CHECKS_PER_RUN, MAX_SUGGESTIONS_PER_RUN

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--model', '-m', type='string',
            help='Specifies the verbose name of the model for which to find suggestions'),
        make_option('--limit', '-l', type='int',
            help='Specifies the maximum number of links for which to find suggestion. Default is 100.')
    )
    help = 'Use google search API to find link suggestions. You must provide API key in settings and search_fields in linkslist.py'

    def execute(self, *args, **options):
            
        if options['limit']:
            limit = options['limit']
        else:
            limit = MAX_SUGGESTIONS_PER_RUN

        if options['model']:
            model = options['model']
        else:
            model = None

        print "Finding link suggestions."

        return get_suggestions(limit=limit, model=model)
