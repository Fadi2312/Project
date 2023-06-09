# Generated by Django 4.1.7 on 2023-03-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiologiesC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.CharField(max_length=70)),
                ('Modul', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=70)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MathC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.CharField(max_length=70)),
                ('Modul', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=70)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SionceMatiereC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.CharField(max_length=70)),
                ('Modul', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=70)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SionceTechnologiesC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.CharField(max_length=70)),
                ('Modul', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=70)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SportC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.CharField(max_length=70)),
                ('Modul', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=70)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
