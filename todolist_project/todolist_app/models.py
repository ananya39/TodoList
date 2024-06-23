from django.db import models
class TodoItem(models.Model):
     date = models.DateField()
     time = models.TimeField()
     notes = models.TextField()
     completed=models.BooleanField(default=False)

     def __str__(self):
        return f"{self.date} {self.time} - {self.notes}"

