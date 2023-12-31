# Generated by Django 4.2.7 on 2023-12-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0045_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Theatre', models.CharField(max_length=1000)),
                ('Date', models.DateTimeField()),
                ('MovieName', models.CharField(max_length=1000)),
                ('ShowTime', models.TimeField()),
                ('HallNumber', models.IntegerField()),
                ('SeatType', models.CharField(max_length=1000)),
                ('TicketPrice', models.IntegerField()),
            ],
        ),
    ]
