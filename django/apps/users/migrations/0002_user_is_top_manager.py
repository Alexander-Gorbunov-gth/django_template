# Generated by Django 5.1.2 on 2024-10-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_top_manager',
            field=models.BooleanField(default=False, verbose_name='Топ мэнеджер'),
        ),
    ]