# Generated by Django 4.1 on 2022-12-23 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seek', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]