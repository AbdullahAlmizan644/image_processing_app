# Generated by Django 4.1 on 2023-02-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seek', '0005_alter_person_fingerprint_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fingerprint_image',
            field=models.ImageField(upload_to='static/seek/images'),
        ),
        migrations.AlterField(
            model_name='person',
            name='nid_image',
            field=models.ImageField(upload_to='static/seek/images'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_image',
            field=models.ImageField(upload_to='static/seek/images'),
        ),
    ]
