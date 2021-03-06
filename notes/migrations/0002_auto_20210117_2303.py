# Generated by Django 3.1.5 on 2021-01-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(help_text='Main body of the note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='draft',
            field=models.BooleanField(default=False, help_text='Whether the note is a to be saved as a draft or published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='hidden',
            field=models.BooleanField(default=False, help_text='Whether the file will be hidden'),
        ),
        migrations.AlterField(
            model_name='note',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time the note was published at'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(help_text='The title of the note', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='The date and time the note was updated at'),
        ),
    ]
