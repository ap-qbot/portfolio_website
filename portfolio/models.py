from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    display_order = models.IntegerField(default=0)  # For ordering categories

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['display_order']  # Default ordering

    def __str__(self):
        return self.name


class Project(models.Model):
    objects = None
    BUTTON_CHOICES = (
        ('demo', 'Demo'),
        ('video', 'Video'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)

    # New fields for button configuration
    button_type = models.CharField(max_length=5, choices=BUTTON_CHOICES, blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True, help_text="URL for Demo button")
    youtube_video_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="YouTube video ID (e.g., dQw4w9WgXcQ from https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category__display_order', '-created_at']

    def __str__(self):
        return self.title