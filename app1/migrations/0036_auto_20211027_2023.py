# Generated by Django 3.1.3 on 2021-10-27 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_auto_20201204_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.cliente'),
        ),
        migrations.AddField(
            model_name='event',
            name='hora',
            field=models.CharField(choices=[('8:00', '8:00'), ('8:30', '8:30'), ('9:00', '9:00'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00')], max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='orcamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.orcamento'),
        ),
    ]
