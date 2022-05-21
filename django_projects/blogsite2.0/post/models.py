from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import CustomUser as User

from taggit.managers import TaggableManager

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self)\
            .get_queryset().filter(status="published")


class Post(models.Model):
    """ORM for Aricele table in databse"""

    # Core settings
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    # Choices for status column
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255, unique_for_date="publish")
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    photo = models.ImageField(upload_to="images/", blank=True,)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='draft',
        max_length=250,
    )

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "main:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )


class PostComment(models.Model):
    """ORM for comments on posts"""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user_name = models.CharField(max_length=80)
    user_email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.username} on {self.post}'


class PostLike(models.Model):
    """ORM for Likes on post"""

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user_name = models.CharField(max_length=80)
    liked = models.BooleanField(default=False)
    creted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Like by {self.user_name} on {self.post}'
