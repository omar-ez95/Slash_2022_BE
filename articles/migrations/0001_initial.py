# Generated by Django 3.2.3 on 2022-09-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('describtion', models.TextField(blank=True, max_length=150, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]