# Generated by Django 4.2.4 on 2023-09-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Msg',
        ),
    ]
