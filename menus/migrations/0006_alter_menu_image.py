# Generated by Django 5.1 on 2024-12-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_alter_menu_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
