from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view,APIView
from api.serializers import ProjectSerializer,ProfileSerializer

from awwards.models import Profile, Project

@api_view(['GET', 'POST'])
def get_projects_data(request):
    
    method = request.method
    if method == 'GET':
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)
    elif method == 'POST':
        serializers  = ProjectSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def get_profiles_data(request):

    
    method = request.method
    if method == 'GET':
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)
    elif method == 'POST':
        serializers  = ProfileSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



# getting single items

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer