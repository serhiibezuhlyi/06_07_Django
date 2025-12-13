from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}: {self.description}"

class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    category = models.ManyToManyField(Category)
    image = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)
    publication_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment to {self.article.title}"
