from django.contrib import admin
from .models import (
    ContactInformation, 
    Education, 
    Skill, 
    Experience, 
    Certification, 
    ResearchExperience, 
    Project, 
    VolunteerExperience, 
    Award, 
    Link
)

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'address', 'professional_summary')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date', 'cgpa')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer')

@admin.register(ResearchExperience)
class ResearchExperienceAdmin(admin.ModelAdmin):
    list_display = ('topic', 'conference', 'publication')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(VolunteerExperience)
class VolunteerExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'description')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
