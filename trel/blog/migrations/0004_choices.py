# Generated by Django 3.2.4 on 2021-07-06 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_blog_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.post')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'In progress'), (3, 'In QA'), (4, 'Ready'), (5, 'Done')], default=1)),
            ],
            bases=('blog.post',),
        ),
    ]