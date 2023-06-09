# Generated by Django 4.1.3 on 2023-05-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
#course için database 
    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('imageurl', models.CharField(blank=True, max_length=50)),
                ('date', models.DateField()),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
