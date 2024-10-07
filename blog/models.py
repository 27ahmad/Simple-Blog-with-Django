from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically format content here
        if self.content:
            self.content = self.format_content(self.content)
        super().save(*args, **kwargs)

    def format_content(self, content):
        if content:
            paragraphs = content.split('\n')
            return ''.join(f'<p>{para.strip()}</p>' for para in paragraphs if para.strip())
        return content


    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    
