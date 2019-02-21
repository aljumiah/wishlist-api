# Generated by Django 2.1.5 on 2019-02-20 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_favoriteitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favoriteitem',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
        migrations.AlterField(
            model_name='favoriteitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
