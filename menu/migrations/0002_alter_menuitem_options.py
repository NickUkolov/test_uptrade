# Generated by Django 4.1.4 on 2022-12-28 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['name'], 'verbose_name': 'menu position', 'verbose_name_plural': 'menu positions'},
        ),
    ]
