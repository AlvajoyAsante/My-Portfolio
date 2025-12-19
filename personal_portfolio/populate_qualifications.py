import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
django.setup()

from qualifications.models import Qualification

def populate():
    qualifications = [
        # Work
        {
            "title": "CS Research Mentorship Program Scholar",
            "subtitle": "Google",
            "date_range": "Jun 2017 - present",
            "category": "work",
            "link": "",
            "start_date": date(2017, 6, 1),
            "end_date": None
        },
        {
            "title": "Undergraduate Research Assistant",
            "subtitle": "Howard University",
            "date_range": "Jun 2023 – Present",
            "category": "work",
            "link": "",
            "start_date": date(2023, 6, 1),
            "end_date": None
        },
        {
            "title": "Career Explore Intern",
            "subtitle": "Road to Hire",
            "date_range": "Jun 2023 - Jun 2023",
            "category": "work",
            "link": "",
            "start_date": date(2023, 6, 1),
            "end_date": date(2023, 6, 1)
        },
        {
            "title": "CCI Instructional Assistant",
            "subtitle": "University of North Carolina at Charlotte",
            "date_range": "Jan 2023 – Present",
            "category": "work",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": None
        },
        {
            "title": "Summer Analyst Intern",
            "subtitle": "Eastdil Secured",
            "date_range": "June 2022 – August 2022",
            "category": "work",
            "link": "",
            "start_date": date(2022, 6, 1),
            "end_date": date(2022, 8, 1)
        },
        {
            "title": "Community Software Engineer",
            "subtitle": "Cemetech.net",
            "date_range": "Jun 2017 - present",
            "category": "work",
            "link": "",
            "start_date": date(2017, 6, 1),
            "end_date": None
        },

        # Education
        {
            "title": "B.Sc Computer Science",
            "subtitle": "University of North Carolina at Charlotte",
            "date_range": "2022 - Present",
            "category": "education",
            "link": "",
            "start_date": date(2022, 1, 1),
            "end_date": None
        },
        {
            "title": "M.S Computer Science",
            "subtitle": "University of North Carolina at Charlotte",
            "date_range": "2024 - Present",
            "category": "education",
            "link": "",
            "start_date": date(2024, 1, 1),
            "end_date": None
        },

        # School Activities
        {
            "title": "Active Member",
            "subtitle": "National Society of Black Engineers",
            "date_range": "Jan 2024 - present",
            "category": "school",
            "link": "https://ninerengage.charlotte.edu/organization/national-society-of-black-engineers",
            "start_date": date(2024, 1, 1),
            "end_date": None
        },
        {
            "title": "Active Member",
            "subtitle": "Association for Computing Machinery",
            "date_range": "Aug 2023 - present",
            "category": "school",
            "link": "https://ninerengage.charlotte.edu/organization/acm",
            "start_date": date(2023, 8, 1),
            "end_date": None
        },
        {
            "title": "Capital One Hackathon",
            "subtitle": "Capital One",
            "date_range": "Jul 2023 - Jul 2023",
            "category": "school",
            "link": "",
            "start_date": date(2023, 7, 1),
            "end_date": date(2023, 7, 1)
        },
        {
            "title": "Freshmen Representative",
            "subtitle": "Blacks in Technology",
            "date_range": "Jan 2023 - present",
            "category": "school",
            "link": "https://ninerengage.charlotte.edu/organization/blacks-in-technology",
            "start_date": date(2023, 1, 1),
            "end_date": None
        },
        {
            "title": "Dean's List",
            "subtitle": "University of North Carolina at Charlotte",
            "date_range": "Jan 2023 - present",
            "category": "school",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": None
        },
        {
            "title": "Chancellor's List",
            "subtitle": "University of North Carolina at Charlotte",
            "date_range": "Aug 2022 - Dec 2022",
            "category": "school",
            "link": "",
            "start_date": date(2022, 8, 1),
            "end_date": date(2022, 12, 1)
        },

        # Certifications
    ]

    for q in qualifications:
        Qualification.objects.update_or_create(
            title=q["title"],
            subtitle=q["subtitle"],
            defaults={
                "date_range": q["date_range"],
                "category": q["category"],
                "link": q["link"],
                "start_date": q["start_date"],
                "end_date": q["end_date"]
            }
        )

if __name__ == '__main__':
    print("Populating qualifications...")
    populate()
    print("Done!")
