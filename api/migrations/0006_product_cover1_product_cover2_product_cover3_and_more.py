# Generated by Django 4.1.4 on 2022-12-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_productimages_options_alter_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover1',
            field=models.ImageField(default='', upload_to='product_covers/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cover2',
            field=models.ImageField(default=1, upload_to='product_covers/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cover3',
            field=models.ImageField(default='1', upload_to='product_covers/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='cover4',
            field=models.ImageField(default=1, upload_to='product_covers/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductImages',
        ),
    ]
