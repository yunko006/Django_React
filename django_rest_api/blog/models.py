from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        """a model manager to query and display only the 
        data which are flagged with the published status"""

        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # protect if someone delete Category it will not delete all the post associated with.
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    # if an user is deleted, it will deleted all his post (not the best one to use here)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # manage if an user wants to published or draft a post 
    status = models.CharField(max_length=10, choices=options, default=published)
    # default manager
    objects = models.Manager()
    # custom manager
    postobjects = PostObjects()

    class Meta:
        # display by default data by published dates by
        ordering = ('-published',)

    def __str__(self):
        return self.title