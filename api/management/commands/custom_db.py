from django.core.management.base import BaseCommand, CommandError
from ...models import Userdetail
from ...models import Activity

class Command(BaseCommand):

    help = "Information for this custom command"

    def add_arguments(self, parser):
        parser.add_argument('uid', type= str, help='User id ')
        parser.add_argument('--name', type= str, help='User Name ')
        parser.add_argument('--tz', type= str, help='Time Zone ')
        parser.add_argument('--st', type= str, help='Enter Start Time')
        parser.add_argument('--et', type= str, help='Enter End Time')



    def handle(self, *args, **options):


        if options['uid'] in Userdetail.objects.all().values_list('userid', flat=True):
            if options['uid'] and options['st'] and options['et'] is not None:
                user_activity = Activity(
                    userid=options['uid'],
                    start_time=options['st'],
                    end_time=options['et']
                )
                user_activity.save()
                self.stdout.write(self.style.SUCCESS('Activity entered Successfully..!!'))
            else:
                raise CommandError('Incorrect Activity details')

        elif options['uid'] and options['name'] and options['tz'] is not None:
            user = Userdetail(
            userid = options['uid'],
            real_name = options['name'],
            tz = options['tz'],
            )
            user.save()
            self.stdout.write(self.style.SUCCESS('User Details entered Successfully..!!'))
        else:
            raise CommandError('Enter correct details. For help type [command_name] --help')
