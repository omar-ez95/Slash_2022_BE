# Generated by Django 3.2.3 on 2022-09-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_discource'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
