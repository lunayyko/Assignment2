from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from music_streaming.models import Album
from music_streaming.serializers import AlbumSerializer


class AlbumViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        """
        POST /albums/

        data params
        - name(required)
        """
        name = request.data.get('name')
        if name is None:
            return Response({'error': 'name field is required.'}, status=status.HTTP_400_BAD_REQUEST)
        album = Album(name=name).save()
        rtn = AlbumSerializer(album).data
        return Response(rtn, status=status.HTTP_201_CREATED)

    def list(self, request):
        """
        GET /albums/

        """
        pass

    def retrieve(self, request, pk):
        """
        GET /albums/{album_id}/
        """
        pass

    def partial_update(self, request, pk):
        """
        PATCH /albums/{album_id}/
        """
        pass

    def destroy(self, request, pk):
        """
        DELETE /albums/{album_id}/
        """
        pass

    @action(detail=True, methods=['GET'])
    def songs(self, request, pk):
        """
        GET /albums/{album_id}/songs/
        """
        album = Album.nodes.get_or_none(uuid=pk)
        if album is None:
            return Response({'error': 'DoesNotExist'})
        songs = album.song.all()
        pass

