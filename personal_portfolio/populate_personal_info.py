import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
django.setup()

from pages.models import PersonalInfo

def populate():
    PersonalInfo.objects.get_or_create(
        first_name='Alvajoy',
        last_name='Asante',
        phone_number='(980) 202-2669',
        email='aasante@charlotte.edu',
        location='Charlotte, NC',
        site_name='Alvajoy Asante',
        occupation='Software Engineer',
        linkedin_link='https://www.linkedin.com/in/alvajoy-asante/',
        github_link='https://github.com/AlvajoyAsante',
        youtube_link='https://www.youtube.com/@alvajoyasante',
        youtube_channel_id='UCH5z7WzZqLOmv6aAblt4Waw'
    )

if __name__ == '__main__':
    print("Populating personal info...")
    populate()
    print("Done!")