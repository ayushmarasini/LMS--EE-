# Generated by Django 4.1.3 on 2022-12-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/subcategory/'),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='uploads/components/'),
        ),
    ]
