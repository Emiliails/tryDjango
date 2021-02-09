import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.

# Here we have created a django.test.
# TestCase subclass with a method that creates a Question instance with a pub_date in the future.
# We then check the output of was_published_recently() - which ought to be False.

# manage.py test polls looked for tests in the polls application
# it found a subclass of the django.test.TestCase class
# it created a special database for the purpose of testing
# it looked for test methods - ones whose names begin with test
# in test_was_published_recently_with_future_question
# it created a Question instance whose pub_date field is 30 days in the future
# … and using the assertIs() method,
# it discovered that its was_published_recently() returns True, though we wanted it to return False
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
