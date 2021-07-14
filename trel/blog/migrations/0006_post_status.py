# Generated by Django 3.2.4 on 2021-07-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'In progress'), (3, 'In QA'), (4, 'Ready'), (5, 'Done')], default=1),
        ),
    ]