from django.db import models

# Create a structure for wiki titles and body

class Wiki_page(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()

  def __str__(self): 
        return self.title 

