# Generated by Django 4.1.1 on 2022-10-06 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
