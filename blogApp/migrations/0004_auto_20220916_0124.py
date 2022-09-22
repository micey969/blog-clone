# Generated by Django 3.2.5 on 2022-09-16 01:24

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_auto_20220915_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2022, 9, 16, 1, 24, 23, 132380, tzinfo=utc))),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 1, 24, 23, 131846, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogApp.post'),
        ),
    ]
