# Generated by Django 4.1 on 2024-05-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]