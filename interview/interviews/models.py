"""Interview models."""
import datetime

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Quiz(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=datetime.timedelta(hours=1))


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.PROTECT)
    question = models.TextField()
    # TODO (ghunkins): navigate database to Postgres
    # and implement ArrayField
    # instead just store and split via '|'
    answer_choices = models.CharField(max_length=1000)
    correct_answer = models.IntegerField()
    answer = models.IntegerField(null=True, blank=True, default=None)


