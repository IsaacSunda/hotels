from django.db import models

from accounts.models import Person

# from django.contrib.auth.base_user import AbstractBaseUser




Rooms = (
    ("room1", "Single"),
    ("room2", "Double"),
    ("room3", "Triple"),
    ("room4", "Quad"),
    ("room5", "Deluxe"),
    ("room6", "Studio"),
    ("room7", "King"),
    ("room8", "Queen"),
    ("room9", "Executive"),
    ("room10", "Royal"),
    ("room11", "presidential")
)


class Room(models.Model):
    room = models.CharField(max_length=20, default="room2", choices=Rooms)
    days = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.room + " for " + str(self.person)


class Billing(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    room = models.OneToOneField(Room, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField()


    def __str__(self):
        return self.person

    def caculate(self, Room, Billing):
        if Room.room == "room1" "single":
            var = Billing.amount == Room.days * 2000
        return var == self.amount