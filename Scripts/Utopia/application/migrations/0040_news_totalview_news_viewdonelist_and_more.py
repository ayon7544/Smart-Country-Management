# Generated by Django 4.2.5 on 2023-10-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0039_alter_news_newsnumber_alter_news_newstitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='TotalView',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='ViewDoneList',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='NewsTitle',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
