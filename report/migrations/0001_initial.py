# Generated by Django 4.1.7 on 2023-03-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('iswp', models.BooleanField(default=False)),
                ('search_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
