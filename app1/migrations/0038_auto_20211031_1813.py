# Generated by Django 3.1.3 on 2021-10-31 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_auto_20211027_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date', 'hora', '-priority', 'event')},
        ),
        migrations.RemoveField(
            model_name='event',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='event',
            name='orcamento',
        ),
    ]
