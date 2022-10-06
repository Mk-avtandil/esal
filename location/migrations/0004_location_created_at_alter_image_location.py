# Generated by Django 4.1.1 on 2022-10-05 11:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_region_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='location.location'),
        ),
    ]