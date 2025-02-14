from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, blank=True, null=True, related_name="group_posts")

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title[:10]

    def get_absolute_url(self):
        return reverse("posts:group_posts", kwargs={"slug": self.slug})
