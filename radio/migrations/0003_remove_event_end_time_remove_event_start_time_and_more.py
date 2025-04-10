# Generated by Django 5.1.7 on 2025-04-09 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0002_event_delete_emission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('musique', 'Musique'), ('discussion', 'Discussion'), ('autre', 'Autre')], max_length=100),
        ),
        migrations.CreateModel(
            name='EventInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('recurrence', models.CharField(choices=[('ONCE', 'Ponctuelle'), ('DAILY', 'Quotidienne'), ('WEEKLY', 'Hebdomadaire'), ('MONTHLY', 'Mensuelle')], default='ONCE', max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.event')),
            ],
        ),
    ]
