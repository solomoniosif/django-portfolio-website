from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    src_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    tools = models.ForeignKey(Tool, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
