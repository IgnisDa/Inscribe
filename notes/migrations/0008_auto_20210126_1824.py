# Generated by Django 3.1.5 on 2021-01-26 12:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0007_merge_20210124_1331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted_on']},
        ),
    ]
