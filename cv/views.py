# cv/views.py
from django.shortcuts import render
from .models import ContactInformation, Education, Skill, Experience

def cv_view(request):
    contact = ContactInformation.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    return render(request, 'cv/cv_template.html', {
        'contact': contact,
        'education': education,
        'skills': skills,
        'experience': experience,
    })