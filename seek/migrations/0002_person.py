# Generated by Django 4.1 on 2022-12-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seek', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('present_address', models.CharField(max_length=1000)),
                ('about', models.CharField(max_length=1000)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('nid_number', models.IntegerField()),
                ('person_image', models.ImageField(upload_to='static/seek/images/')),
                ('nid_image', models.ImageField(upload_to='static/seek/images/')),
                ('fingerprint_image', models.ImageField(upload_to='static/seek/images/')),
                ('date', models.DateField()),
            ],
        ),
    ]
