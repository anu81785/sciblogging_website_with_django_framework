# Generated by Django 4.1 on 2023-02-23 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_footer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]