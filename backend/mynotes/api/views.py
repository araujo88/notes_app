from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import NoteSerializer
from notes.models import Note

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/notes'},
        {'GET':'/api/note/id'},
        {'POST':'/api/notes/create-note'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def createNote(request):
    data = request.data
    #current_user = request.user
    body = data['body']
    updated = data['updated']
    note = Note.objects.create(body=body, updated=updated)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)