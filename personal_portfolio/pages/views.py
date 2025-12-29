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
import requests
import xml.etree.ElementTree as ET
import os

def get_latest_youtube_videos(channel_id):
    if not channel_id:
        return []
    
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    try:
        response = requests.get(rss_url, timeout=5)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            ns = {'yt': 'http://www.youtube.com/xml/schemas/2015', 'media': 'http://search.yahoo.com/mrss/', 'atom': 'http://www.w3.org/2005/Atom'}
            videos = []
            for entry in root.findall('atom:entry', ns):
                video_id_elem = entry.find('yt:videoId', ns)
                title_elem = entry.find('atom:title', ns)
                media_group = entry.find('media:group', ns)
                description_elem = media_group.find('media:description', ns) if media_group is not None else None
                
                if video_id_elem is not None and title_elem is not None:
                    videos.append({
                        'youtube_id': video_id_elem.text,
                        'title': title_elem.text,
                        'description': description_elem.text if description_elem is not None else "",
                    })
                
                if len(videos) >= 1: # Limit to 6 videos
                    break
            return videos
    except Exception as e:
        print(f"Error fetching YouTube videos: {e}")
        return []
    return []

# Create your views here.
def home(request):
    qualifications = Qualification.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    personal_info = PersonalInfo.objects.first()
    
    # Try to fetch from YouTube RSS first
    videos = []
    channel_id = personal_info.youtube_channel_id
            
    if channel_id:
        videos = get_latest_youtube_videos(channel_id)
        
    # Fallback to database if no videos found from RSS
    if not videos:
        videos = Video.objects.filter(is_active=True)
    
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
            recaptcha_token = data.get('recaptchaToken')

            if not name or not email or not message:
                return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)
            
            if not recaptcha_token:
                 return JsonResponse({'status': 'error', 'message': 'reCAPTCHA verification failed.'}, status=400)

            # TODO: Verify reCAPTCHA token with Google Enterprise API
            # You need to set up Google Cloud credentials and use the library or REST API
            # For now, we just check if the token is present
            
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