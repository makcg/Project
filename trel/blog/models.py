from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    (1, 'New'),
    (2, 'In progress'),
    (3, 'In QA'),
    (4, 'Ready'),
    (5, 'Done'),
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
