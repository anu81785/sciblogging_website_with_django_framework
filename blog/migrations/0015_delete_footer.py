# Generated by Django 4.1 on 2023-02-23 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_footer_remove_contact_footer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Footer',
        ),
    ]
