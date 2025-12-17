import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_portfolio.settings')
django.setup()

from skills.models import SkillCategory, Skill

def populate():
    # Programming Languages
    cat_prog, _ = SkillCategory.objects.get_or_create(
        name="Programming Languages",
        defaults={'subtitle': "More than 3 years", 'icon_class': "uil uil-server-network", 'order': 1}
    )
    skills_prog = ["C", "Python", "Java", "C++", "JavaScript"]
    for i, name in enumerate(skills_prog):
        Skill.objects.get_or_create(category=cat_prog, name=name, defaults={'order': i})

    # Frontend
    cat_front, _ = SkillCategory.objects.get_or_create(
        name="Frontend",
        defaults={'subtitle': "More than 1 years", 'icon_class': "uil uil-brackets-curly", 'order': 2}
    )
    skills_front = ["HTML", "JavaScript", "CSS", "React", "Django", "Vue"]
    for i, name in enumerate(skills_front):
        Skill.objects.get_or_create(category=cat_front, name=name, defaults={'order': i})

    # Backend
    cat_back, _ = SkillCategory.objects.get_or_create(
        name="Backend",
        defaults={'subtitle': "More than 3 years", 'icon_class': "uil uil-server-network", 'order': 3}
    )
    skills_back = ["C++", "Node Js", "Flask"]
    for i, name in enumerate(skills_back):
        Skill.objects.get_or_create(category=cat_back, name=name, defaults={'order': i})

    # Database
    cat_db, _ = SkillCategory.objects.get_or_create(
        name="Database",
        defaults={'subtitle': "More than 1 year", 'icon_class': "uil uil-swatchbook", 'order': 4}
    )
    skills_db = ["MongoDB", "SQL", "Firebase"]
    for i, name in enumerate(skills_db):
        Skill.objects.get_or_create(category=cat_db, name=name, defaults={'order': i})

    # Tools
    cat_tools, _ = SkillCategory.objects.get_or_create(
        name="Tools",
        defaults={'subtitle': "More than 3 years", 'icon_class': "uil uil-server-network", 'order': 5}
    )
    skills_tools = ["VS Code", "Intellij", "Git", "MySQL", "WordPress", "Postman"]
    for i, name in enumerate(skills_tools):
        Skill.objects.get_or_create(category=cat_tools, name=name, defaults={'order': i})

    # Cloud
    cat_cloud, _ = SkillCategory.objects.get_or_create(
        name="Cloud",
        defaults={'subtitle': "More than 1 years", 'icon_class': "uil uil-brackets-curly", 'order': 6}
    )
    skills_cloud = ["Google Cloud", "Azure", "AWS"]
    for i, name in enumerate(skills_cloud):
        Skill.objects.get_or_create(category=cat_cloud, name=name, defaults={'order': i})

    # AI
    cat_ai, _ = SkillCategory.objects.get_or_create(
        name="AI",
        defaults={'subtitle': "More than 1 years", 'icon_class': "uil uil-brackets-curly", 'order': 7}
    )
    skills_ai = ["Machine Learning", "Natural Language Processing", "Large Language Models"]
    for i, name in enumerate(skills_ai):
        Skill.objects.get_or_create(category=cat_ai, name=name, defaults={'order': i})

if __name__ == '__main__':
    print("Populating skills...")
    populate()
    print("Done!")
