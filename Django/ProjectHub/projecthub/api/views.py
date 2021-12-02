from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Projects, Tag


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Projects.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Projects.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)
