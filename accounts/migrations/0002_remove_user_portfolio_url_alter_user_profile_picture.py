# Generated by Django 5.0.6 on 2025-06-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='portfolio_url',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]
