# Generated by Django 4.2.7 on 2023-11-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0035_blog_external_source_alter_blog_demo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ticket_link',
        ),
        migrations.AlterField(
            model_name='blog',
            name='tools',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
