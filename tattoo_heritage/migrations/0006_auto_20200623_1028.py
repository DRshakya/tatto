# Generated by Django 3.0.3 on 2020-06-23 04:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tattoo_heritage', '0005_artist_work'),
    ]

    operations = [
        migrations.DeleteModel(
            name='gallery2',
        ),
        migrations.DeleteModel(
            name='gallery3',
        ),
        migrations.DeleteModel(
            name='gallery4',
        ),
        migrations.AlterField(
            model_name='artist_work',
            name='w_id',
            field=models.UUIDField(default=uuid.UUID('2a57df3a-78c8-4118-8a7c-38d7cb49e2cf'), editable=False, primary_key=True, serialize=False),
        ),
    ]
