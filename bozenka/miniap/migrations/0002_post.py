# Generated by Django 5.0.1 on 2024-01-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='x', max_length=200)),
                ('title', models.CharField(default='x', max_length=200)),
                ('post', models.CharField(default='x', max_length=200)),
            ],
        ),
    ]
