# Generated by Django 3.2.8 on 2021-10-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='invited_by',
            field=models.CharField(default='faxriyor', max_length=200),
        ),
    ]