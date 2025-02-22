# Generated by Django 3.0.3 on 2020-06-23 05:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo_heritage', '0007_auto_20200623_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='a_fb',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='a_insta',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist_work',
            name='w_id',
            field=models.UUIDField(default=uuid.UUID('b4086a8d-b3df-421d-8e14-db43a63e70f1'), editable=False, primary_key=True, serialize=False),
        ),
    ]
