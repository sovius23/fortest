# Generated by Django 4.0.3 on 2022-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_chat_user1_remove_chat_user2_chat_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]