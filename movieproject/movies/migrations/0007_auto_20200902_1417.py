# Generated by Django 3.1 on 2020-09-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20200902_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumb',
            field=models.ImageField(blank='True', upload_to=''),
        ),
    ]
