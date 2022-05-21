from django.db import models

# Create your models here.
class BlogComment(models.Model):
    """ORM for Comments on WebSite(BlogSiteV2) or author"""

    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.email}'