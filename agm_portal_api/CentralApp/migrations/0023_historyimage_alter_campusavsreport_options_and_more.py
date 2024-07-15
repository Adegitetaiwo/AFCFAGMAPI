# Generated by Django 4.0.5 on 2024-07-15 08:31

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentralApp', '0022_alter_campusavsreport_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusOrSchoolAcronym', models.CharField(max_length=50)),
                ('picture', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='report_images/')),
            ],
            options={
                'verbose_name_plural': 'Campus AVS Historical Pictures',
            },
        ),
        migrations.AlterModelOptions(
            name='campusavsreport',
            options={'verbose_name_plural': 'Campus AVS Report'},
        ),
        migrations.AlterModelOptions(
            name='reportimage',
            options={'verbose_name_plural': 'Campus AVS Report Images'},
        ),
        migrations.AlterField(
            model_name='campusavs',
            name='coordinator_picture',
            field=models.ImageField(blank=True, upload_to='campus_avs_images_cord/'),
        ),
        migrations.AlterField(
            model_name='campusavs',
            name='flyer',
            field=models.ImageField(blank=True, upload_to='campus_avs_images/'),
        ),
        migrations.AlterField(
            model_name='campusavs',
            name='secretary_picture',
            field=models.ImageField(blank=True, upload_to='campus_avs_images_sect/'),
        ),
    ]
