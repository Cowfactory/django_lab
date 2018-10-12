from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):
    LEVEL = (
        (1, 'Fundamental Awareness'),
        (2, 'Novice'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    )
    description = models.CharField(max_length=100)
    skill_level = models.IntegerField(
        choices=LEVEL,
        default=LEVEL[2]
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
