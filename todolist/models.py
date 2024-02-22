from django.db import models


class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)

    "function which will create the represnt. of the text field."
    def __str__(self):
        return self.text




