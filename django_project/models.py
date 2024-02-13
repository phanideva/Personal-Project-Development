from django.db import models

class PathConfig(models.Model):
    name = models.CharField(max_length=255, unique=True)
    output_directory = models.CharField(max_length=1024, help_text="Directory for storing Excel files")

    def __str__(self):
        return self.name
