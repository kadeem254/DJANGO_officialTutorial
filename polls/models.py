import datetime

from django.db import models
from django.utils import timezone

# Question Model - Holds a question that can be raised and can have multiple
# choices which can be voted for.
class Question( models.Model ):
    question_text = models.CharField( max_length=255 )
    pub_date = models.DateTimeField( "date published" )

    def __str__(self):
        return self.question_text
    
    # method to check if question was posted in the last 24 hrs.
    def was_published_recently( self ):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice Model - Holds a single choice to a question, can recieve votes.
class Choice( models.Model ):
    question = models.ForeignKey( Question, on_delete=models.CASCADE )
    choice_text = models.CharField( max_length=255 )
    votes = models.IntegerField( default=0 )

    def __str__(self):
        return self.choice_text