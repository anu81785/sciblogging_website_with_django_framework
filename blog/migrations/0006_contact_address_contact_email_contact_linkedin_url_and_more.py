# Generated by Django 4.1 on 2023-02-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_about_id_alter_contact_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='linkedin_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
