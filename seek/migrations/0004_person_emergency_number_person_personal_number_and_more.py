# Generated by Django 4.1 on 2023-02-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seek', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='emergency_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='personal_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='relative_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
