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
            "category": "work",
            "link": "",
            "start_date": date(2017, 6, 1),
            "end_date": None
        },
        {
            "title": "Undergraduate Research Assistant",
            "subtitle": "Howard University",
            "category": "work",
            "link": "",
            "start_date": date(2023, 6, 1),
            "end_date": None
        },
        {
            "title": "Career Explore Intern",
            "subtitle": "Road to Hire",
            "category": "work",
            "link": "",
            "start_date": date(2023, 6, 1),
            "end_date": date(2023, 6, 1)
        },
        {
            "title": "CCI Instructional Assistant",
            "subtitle": "University of North Carolina at Charlotte",
            "category": "work",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": None
        },
        {
            "title": "Summer Analyst Intern",
            "subtitle": "Eastdil Secured",
            "category": "work",
            "link": "",
            "start_date": date(2022, 6, 1),
            "end_date": date(2022, 8, 1)
        },
        {
            "title": "Community Software Engineer",
            "subtitle": "Cemetech.net",
            "category": "work",
            "link": "",
            "start_date": date(2017, 6, 1),
            "end_date": None
        },

        # Education
        {
            "title": "B.Sc Computer Science",
            "subtitle": "University of North Carolina at Charlotte",
            "category": "education",
            "link": "",
            "start_date": date(2022, 1, 1),
            "end_date": None
        },
        {
            "title": "M.S Computer Science",
            "subtitle": "University of North Carolina at Charlotte",
            "category": "education",
            "link": "",
            "start_date": date(2024, 1, 1),
            "end_date": None
        },

        # School Activities
        {
            "title": "Active Member",
            "subtitle": "National Society of Black Engineers",
            "category": "school",
            "link": "https://ninerengage.charlotte.edu/organization/national-society-of-black-engineers",
            "start_date": date(2024, 1, 1),
            "end_date": None
        },
        {
            "title": "Active Member",
            "subtitle": "Association for Computing Machinery",
            "category": "school",
            "link": "https://ninerengage.charlotte.edu/organization/acm",
            "start_date": date(2023, 8, 1),
            "end_date": None
        },
        {
            "title": "Capital One Hackathon",
            "subtitle": "Capital One",
            "category": "school",
            "link": "",
            "start_date": date(2023, 7, 1),
            "end_date": date(2023, 7, 1)
        },
        {
            "title": "Freshmen Representative",
            "subtitle": "Blacks in Technology",
            "category": "school",
            "link": "https://ninerengage.charlotte.edu/organization/blacks-in-technology",
            "start_date": date(2023, 1, 1),
            "end_date": None
        },
        {
            "title": "Dean's List",
            "subtitle": "University of North Carolina at Charlotte",
            "category": "school",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": None
        },
        {
            "title": "Chancellor's List",
            "subtitle": "University of North Carolina at Charlotte",
            "category": "school",
            "link": "",
            "start_date": date(2022, 8, 1),
            "end_date": date(2022, 12, 1)
        },

        # Certifications
        {
            "title": "AI Agents in LangGraph",
            "subtitle": "DeepLearning.AI",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 2, 1),
            "end_date": date(2025, 2, 1)
        },
        {
            "title": "Microsoft Azure Fundamentals: Describe cloud concepts",
            "subtitle": "Microsoft Learning",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 2, 1),
            "end_date": date(2025, 2, 1)
        },
        {
            "title": "Review intermediate C++",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 2, 1),
            "end_date": date(2025, 2, 1)
        },
        {
            "title": "ChatGPT Prompt Engineering for Developers",
            "subtitle": "DeepLearning.AI",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 1, 1),
            "end_date": date(2025, 1, 1)
        },
        {
            "title": "LangChain Chat with Your Data",
            "subtitle": "DeepLearning.AI",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 1, 1),
            "end_date": date(2025, 1, 1)
        },
        {
            "title": "LangChain for LLM Application Development",
            "subtitle": "DeepLearning.AI",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 1, 1),
            "end_date": date(2025, 1, 1)
        },
        {
            "title": "Prompt Engineering with Llama 2&3",
            "subtitle": "DeepLearning.AI",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 1, 1),
            "end_date": date(2025, 1, 1)
        },
        {
            "title": "Vector Databases: from Embeddings to Applications",
            "subtitle": "DeepLearning.AI",
            "category": "certifications",
            "link": "",
            "start_date": date(2025, 1, 1),
            "end_date": date(2025, 1, 1)
        },
        {
            "title": "AI Framework Overview: AI Developer Role",
            "subtitle": "Skillsoft",
            "category": "certifications",
            "link": "",
            "start_date": date(2024, 3, 1),
            "end_date": date(2024, 3, 1)
        },
        {
            "title": "Black Students in Technology Scholarship 2023",
            "subtitle": "Cadence",
            "category": "certifications",
            "link": "",
            "start_date": date(2024, 1, 1),
            "end_date": date(2024, 1, 1)
        },
        {
            "title": "Social and Behavioral Sciences: RCR",
            "subtitle": "CITI Program",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 7, 1),
            "end_date": date(2023, 7, 1)
        },
        {
            "title": "Introduction to JavaScript",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 6, 1),
            "end_date": date(2023, 6, 1)
        },
        {
            "title": "JavaScript Intermediate",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 6, 1),
            "end_date": date(2023, 6, 1)
        },
        {
            "title": "C Intermediate",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 5, 1),
            "end_date": date(2023, 5, 1)
        },
        {
            "title": "Introduction to C++",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 5, 1),
            "end_date": date(2023, 5, 1)
        },
        {
            "title": "C# Intermediate",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 4, 1),
            "end_date": date(2023, 4, 1)
        },
        {
            "title": "Java Intermediate",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 3, 1),
            "end_date": date(2023, 3, 1)
        },
        {
            "title": "Introduction to Cloud 101",
            "subtitle": "Amazon Web Services (AWS)",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 2, 1),
            "end_date": date(2023, 2, 1)
        },
        {
            "title": "Machine Learning Foundations",
            "subtitle": "Amazon Web Services (AWS)",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 2, 1),
            "end_date": date(2023, 2, 1)
        },
        {
            "title": "Python Intermediate",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 2, 1),
            "end_date": date(2023, 2, 1)
        },
        {
            "title": "Cybersecurity Workshop",
            "subtitle": "Bank of America",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": date(2023, 1, 1)
        },
        {
            "title": "Introduction to Python",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": date(2023, 1, 1)
        },
        {
            "title": "Introduction to SQL",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2023, 1, 1),
            "end_date": date(2023, 1, 1)
        },
        {
            "title": "Introduction to C#",
            "subtitle": "Sololearn",
            "category": "certifications",
            "link": "",
            "start_date": date(2022, 12, 1),
            "end_date": date(2022, 12, 1)
        },
    ]

    for q in qualifications:
        Qualification.objects.update_or_create(
            title=q["title"],
            subtitle=q["subtitle"],
            defaults={
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
