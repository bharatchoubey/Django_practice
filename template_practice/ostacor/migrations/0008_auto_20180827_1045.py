# Generated by Django 2.1 on 2018-08-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostacor', '0007_homepage_about_about_icons'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage_latest_story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_liner_title', models.CharField(max_length=100)),
                ('cover_img_src', models.CharField(max_length=100)),
                ('brief_short_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='homepage_about',
        ),
    ]
