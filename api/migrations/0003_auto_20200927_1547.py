# Generated by Django 3.1.1 on 2020-09-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200927_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='id',
            field=models.AutoField(auto_created=True, default=121, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='userid',
            field=models.CharField(max_length=10),
        ),
    ]
