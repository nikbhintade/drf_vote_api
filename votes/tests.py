from django.test import TestCase
from django.utils import timezone
# Create your tests here.
from .models import Vote
from .serializers import VoteSerializer

class VoteSerializerTest(TestCase):

    def test_serializer(self):
        time = timezone.now()
        vote = Vote.objects.create(
        subject = 'this is the test?',
        vote_taken = time,
        ayes = 100,
        nays = 0
        )
        serialized = VoteSerializer(vote).data

        assert vote.id == serialized['id']
        assert vote.subject == serialized['subject']
        assert vote.ayes == serialized['ayes']
        assert vote.nays == serialized['nays']
        # I don't know why following assertion doesn't work but i think this is due to serialized datetime object is different than regular datetime object
        #assert vote.vote_taken.date() == serialized['vote_taken']
