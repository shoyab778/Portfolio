from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('nlp', 'NLP'),
        ('cv', 'Computer Vision'),
        ('dl', 'Deep Learning'),
        ('ml', 'Machine Learning'),
        ('gen', 'Generative AI'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tech_stack = models.CharField(max_length=500, help_text="Comma separated tech stack")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_placeholder = models.CharField(max_length=20, default='#1a1a2e')
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('aiml', 'AI / ML'),
        ('frameworks', 'Frameworks & Libraries'),
        ('tools', 'Tools & DevOps'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="0-100")
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.name} ({self.category})"
