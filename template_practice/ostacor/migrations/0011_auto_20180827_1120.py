# Generated by Django 2.1 on 2018-08-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostacor', '0010_auto_20180827_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage_latest_story',
            old_name='brief_short_desc',
            new_name='one_liner_desc',
        ),
        migrations.RenameField(
            model_name='homepage_latest_story',
            old_name='one_liner_recipie_name',
            new_name='one_title',
        ),
        migrations.AlterField(
            model_name='homepage_food_locus_story',
            name='one_title',
            field=models.CharField(max_length=75),
        ),
    ]
