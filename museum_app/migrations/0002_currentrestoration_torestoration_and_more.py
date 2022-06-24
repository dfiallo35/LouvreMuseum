# Generated by Django 4.0.4 on 2022-06-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentRestoration',
            fields=[
            ],
            options={
                'verbose_name': 'Artwork Currently Under Restoration',
                'verbose_name_plural': 'Artworks Currently Under Restoration',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('museum_app.restoration',),
        ),
        migrations.CreateModel(
            name='ToRestoration',
            fields=[
            ],
            options={
                'verbose_name': 'Artwork to Restoration',
                'verbose_name_plural': 'Artworks to Restoration',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('museum_app.artwork',),
        ),
        migrations.AlterModelOptions(
            name='restoration',
            options={'get_latest_by': 'date_time', 'ordering': ['-date_time'], 'verbose_name': 'Restoration', 'verbose_name_plural': 'Restorations'},
        ),
        migrations.AlterField(
            model_name='restoration',
            name='restoration_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Restoration Type'),
        ),
    ]