# Generated by Django 4.0.2 on 2024-01-30 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0021_rename_rating_rating_ratings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RadioSelection',
        ),
        migrations.DeleteModel(
            name='rating',
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='check1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='check2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='check3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='color',
            field=models.CharField(choices=[('none', 'None'), ('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], default='none', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='ratings',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='tab_one_model',
            name='city',
            field=models.CharField(choices=[('none', 'None'), ('Delhi', 'Delhi'), ('Gurgaon', 'Gurgaon'), ('Bangalore', 'Bangalore')], default='none', max_length=20, null=True),
        ),
    ]
