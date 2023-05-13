# Generated by Django 4.1.3 on 2022-12-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_borrowlist_pieces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine', models.IntegerField()),
                ('return_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='borrowlist',
            name='fine',
        ),
        migrations.AddField(
            model_name='borrowlist',
            name='returned',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]