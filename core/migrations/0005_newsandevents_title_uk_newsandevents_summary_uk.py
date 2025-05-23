from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_newsandevents_summary_es_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsandevents',
            name='title_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newsandevents',
            name='summary_uk',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ] 