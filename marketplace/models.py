from django.db import models
from django.contrib.auth.models import User

class Artwork(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='artworks/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Commission(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Commission for {self.artwork.title} by {self.requester.username}"
