from django.db import models

class Post(models.Model):
    STATUS_CHOICES=(
        ('pub', 'published'),
        ('drf','draft'),
    )
    title= models.CharField(max_length=50)
    text= models.TextField()
    author= models.ForeignKey("auth.User",on_delete=models.CASCADE)
    date_time_created= models.DateTimeField( auto_now_add=True)
    date_time_modified= models.DateTimeField(auto_now=True)
    status=models.CharField(choices=STATUS_CHOICES, max_length=50)

    def __str__(self):
        return self.title
    