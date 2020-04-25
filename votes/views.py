from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from django.shortcuts import redirect
from .models import Vote
from .serializers import VoteSerializer
from rest_framework.renderers import (
    JSONRenderer,
    TemplateHTMLRenderer,
    BrowsableAPIRenderer
    )
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class VoteAPIMixn(object):
    renderer_classes = [
        JSONRenderer,
        TemplateHTMLRenderer,
        ]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_renderers(self):
        renderer_classes = self.renderer_classes
        if self.request.user.is_staff:
            renderer_classes += [BrowsableAPIRenderer]
        return [renderer() for renderer in renderer_classes]

class VoteList(VoteAPIMixn, generics.ListCreateAPIView):
    template_name = 'vote_list.html'



class VoteDetail(VoteAPIMixn, generics.RetrieveUpdateDestroyAPIView):
    template_name = 'vote.html'
