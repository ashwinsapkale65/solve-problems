# Generated by Django 4.0.6 on 2022-08-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolhome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentregistrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('class1', models.CharField(max_length=122)),
                ('div', models.CharField(max_length=122)),
                ('roll', models.CharField(max_length=122)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
