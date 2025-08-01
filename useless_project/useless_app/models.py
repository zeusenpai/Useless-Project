from django.db import models

class GeneratedThought(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Thought at {self.created_at:%Y-%m-%d %H:%M}"
