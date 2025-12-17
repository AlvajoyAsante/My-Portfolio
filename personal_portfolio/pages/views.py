from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from qualifications.models import Qualification
from skills.models import SkillCategory
from projects.models import Project
from videos.models import Video
from .models import PersonalInfo
import json

# Create your views here.
def home(request):
    qualifications = Qualification.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    videos = Video.objects.filter(is_active=True)
    personal_info = PersonalInfo.objects.first()
    
    context = {
        'personal_info': personal_info,
        'qualifications': qualifications,
        'skill_categories': skill_categories,
        'projects': projects,
        'videos': videos,
    }

    return HttpResponse(render(request, "pages/home.html", context))

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        # Rate Limiting
        ip = request.META.get('REMOTE_ADDR')
        cache_key = f"email_rate_limit_{ip}"
        email_count = cache.get(cache_key, 0)

        if email_count >= 5:  # Limit: 5 emails per hour
            return JsonResponse({'status': 'error', 'message': 'Rate limit exceeded. Please try again later.'}, status=429)

        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not name or not email or not message:
                return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)

            personal_info = PersonalInfo.objects.first()
            if not personal_info or not personal_info.email:
                return JsonResponse({'status': 'error', 'message': 'Recipient email not configured.'}, status=500)

            subject = f"Portfolio Contact: {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Send email to yourself
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER, # From email
                [personal_info.email.strip()], # To email
                fail_silently=False,
            )

            # Increment rate limit counter
            cache.set(cache_key, email_count + 1, 3600)  # Expires in 1 hour

            return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)