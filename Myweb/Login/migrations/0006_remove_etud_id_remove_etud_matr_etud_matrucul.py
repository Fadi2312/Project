# Generated by Django 4.1.7 on 2023-04-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_etud_matr_alter_etud_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etud',
            name='id',
        ),
        migrations.RemoveField(
            model_name='etud',
            name='matr',
        ),
        migrations.AddField(
            model_name='etud',
            name='matrucul',
            field=models.CharField(default=1, max_length=12, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
