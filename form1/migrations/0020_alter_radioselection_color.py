# Generated by Django 4.0.2 on 2024-01-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0019_radioselection_rating_remove_tab_one_model_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radioselection',
            name='color',
            field=models.CharField(choices=[('none', 'None'), ('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], default='none', max_length=5, null=True),
        ),
    ]