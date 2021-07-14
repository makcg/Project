from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    class Meta:
        db_table = 'auth_userprofile'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="user",
        # executor=models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='executor')
    )

