# Generated by Django 4.2.7 on 2023-12-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0046_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Date',
            field=models.DateField(),
        ),
    ]
