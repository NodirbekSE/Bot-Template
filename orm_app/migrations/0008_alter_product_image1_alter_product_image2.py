# Generated by Django 5.0.4 on 2024-05-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0007_alter_askuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
