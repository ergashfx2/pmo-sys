# Generated by Django 5.0.6 on 2024-05-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hodimlar', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
