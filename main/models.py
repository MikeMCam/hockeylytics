from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('feedback-detail', kwargs={'pk': self.pk})


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


# Team roster
class PlayerList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField()
    leave_date = models.DateTimeField()


class Match(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    homeTeam = models.ForeignKey(Team, null=True, related_name='home_team', on_delete=models.CASCADE)
    awayTeam = models.ForeignKey(Team, null=True, related_name='away_team', on_delete=models.CASCADE)
    homeGoals = models.IntegerField(default=0)
    homePoints = models.IntegerField(default=0)
    awayGoals = models.IntegerField(default=0)
    awayPoints = models.IntegerField(default=0)


class Stats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

    FORWARD = 'FWD'
    DEFENSE = 'DEF'
    CENTER = 'CNT'
    GOALIE = 'GOL'
    POSITION_CHOICES = [
        (FORWARD, 'Forward'),
        (DEFENSE, 'Defense'),
        (CENTER, 'Center'),
        (GOALIE, 'Goalie'),
    ]
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        default=FORWARD,
    )

    goals = models.IntegerField(blank=True)
    points = models.IntegerField(blank=True)
    fow = models.IntegerField(blank=True)
    fol = models.IntegerField(blank=True)
    ppg = models.IntegerField(blank=True)
    shg = models.IntegerField(blank=True)
    assists = models.IntegerField(blank=True)
    foPercent = models.FloatField(blank=True)
    shootingPercent = models.FloatField(blank=True)
    toi = models.IntegerField(blank=True)
    sog = models.IntegerField(blank=True)
    fow = models.IntegerField(blank=True)
    pim = models.IntegerField(blank=True)
