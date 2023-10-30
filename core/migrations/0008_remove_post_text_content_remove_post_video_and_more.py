# Generated by Django 4.0.4 on 2023-10-30 14:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_text_content_post_video_alter_post_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_image.jpg', null=True, upload_to='post_images'),
        ),
    ]
