from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=50)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(default=1)

    def __str__(self):
        return f"{str(self.room)} - {self.author}"
