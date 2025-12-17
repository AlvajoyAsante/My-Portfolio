import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
django.setup()

from projects.models import Project

def populate():
    projects = [
        {
            "title": "DUCK HUNT",
            "description": "A classic NES Duck Hunt clone for the TI-84 Plus CE calculator.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/duckhunt.png",
            "github_link": "https://github.com/Overload02/DuckHunt",
            "order": 1
        },
        {
            "title": "GFX3",
            "description": "A sprite stacking library for creating complex visuals on the TI-84 Plus CE.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/gfx3.png",
            "github_link": "https://github.com/Overload02/GFX3",
            "order": 2
        },
        {
            "title": "KIRA",
            "description": "An award-winning AI advisor helping minority communities build financial literacy.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/kira.png",
            "github_link": "",
            "order": 3
        },
        {
            "title": "ReliQ",
            "description": "A gamified app rewarding students for completing homework with virtual currency.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/reliq.jpg",
            "github_link": "",
            "order": 4
        },
        {
            "title": "Scratch CE",
            "description": "Block coding language for the TI-84 Plus CE to create stories and games.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/scratch_ce.png",
            "github_link": "https://github.com/Overload02/Scratch-CE",
            "order": 5
        },
        {
            "title": "Oxygen",
            "description": "GUI framework for creating user-friendly interfaces on the TI-84 Plus CE.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/oxygen.png",
            "github_link": "https://github.com/Overload02/Oxygen",
            "order": 6
        },
        {
            "title": "Virtual Trading Floor",
            "description": "Award-winning VR/AR trading simulation for training and strategy testing.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/vtf.png",
            "github_link": "",
            "order": 7
        },
        {
            "title": "Xenon",
            "description": "Comprehensive shell with CLI and GUI interfaces for the TI-84 Plus CE.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/xenon.gif",
            "github_link": "https://github.com/Overload02/Xenon",
            "order": 8
        },
        {
            "title": "Neural",
            "description": "Coevolutionary network for detecting handwritten digits on the TI-84 Plus CE.",
            "image_url": "https://storage.googleapis.com/my-portfolio-408919_cloudbuild/static/img/projects/neural.png",
            "github_link": "https://github.com/Overload02/Neural",
            "order": 9
        }
    ]

    for p in projects:
        Project.objects.get_or_create(
            title=p["title"],
            defaults={
                "description": p["description"],
                "image_url": p["image_url"],
                "github_link": p["github_link"],
                "order": p["order"]
            }
        )

if __name__ == '__main__':
    print("Populating projects...")
    populate()
    print("Done!")
