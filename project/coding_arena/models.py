import uuid
from django.db import models
from django.utils import timezone

# Create your models here.

class Gamer(models.Model):
    name = models.CharField(max_length=200)
    # user_id = models.CharField)
    user_id = models.UUIDField(max_length=100, blank=True, null=True, unique=True, default=uuid.uuid4)
    prog_lang = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name

class Challenge(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=False, null=False)
    createdBy = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    dateTimeCreated = models.DateTimeField(default=timezone.now)


class Invite(models.Model):
    ACCEPTED = 'A'
    REJECTED = 'R'
    PENDING = 'P'
    STATUS_CHOICES = [
        (ACCEPTED, 'A'),
        (REJECTED, 'R'),        
		(PENDING, 'P'),
    ]
    
    challengeID = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    dateTimeCreated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)



