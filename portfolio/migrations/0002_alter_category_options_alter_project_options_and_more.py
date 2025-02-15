# Generated by Django 4.2.17 on 2025-01-29 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['display_order'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['category__display_order', '-created_at']},
        ),
        migrations.AddField(
            model_name='category',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.category'),
        ),
    ]
