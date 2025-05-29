from django.db import migrations
from core.utils import unique_slug_generator

def fix_empty_slugs(apps, schema_editor):
    Course = apps.get_model('course', 'Course')
    for course in Course.objects.filter(slug=''):
        # Generate slug from title and code to ensure uniqueness
        base_slug = f"{course.title}-{course.code}".lower()
        # Remove special characters and replace spaces with hyphens
        base_slug = ''.join(c for c in base_slug if c.isalnum() or c == ' ')
        base_slug = base_slug.replace(' ', '-')
        # Ensure uniqueness by adding a number if needed
        slug = base_slug
        counter = 1
        while Course.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        course.slug = slug
        course.save()

class Migration(migrations.Migration):
    dependencies = [
        ('course', '0006_course_summary_uk_course_title_uk_program_summary_uk_and_more'),
    ]

    operations = [
        migrations.RunPython(fix_empty_slugs),
    ] 