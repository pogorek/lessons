# Generated by Django 4.0.1 on 2022-01-18 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
