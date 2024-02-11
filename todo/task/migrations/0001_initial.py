# Generated by Django 4.2.7 on 2024-02-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=65, verbose_name='CONTENT')),
                ('status', models.BooleanField(choices=[(True, 'Done'), (False, 'In-Progress')], default=False, verbose_name='STATUS')),
                ('deadline', models.DateField(verbose_name='DEADLINE')),
            ],
        ),
    ]