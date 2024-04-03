from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .models import Actor, Movie, Comment
from .serializers import ActorSerializer, MovieSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer




class MovieActorAPIView(APIView):
    def get(self, request, id):
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)




        return Response(serializer.data, status=status.HTTP_200_OK)




class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'author__first_name', 'imdb']








# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#
#     def post(self, request, *args, **kwargs):
#
#         comment_data = request.data
#         new_comment = Comment.objects.create(**comment_data, user=request.user)
#
#         return Response({"message": "Comment created successfully."}, status=status.HTTP_201_CREATED)
#
#
#     def get(self, request, *args, **kwargs):
#         user_comments = Comment.objects.filter(user=request.user)
#
#         serialized_comments = CommentSerializer(user_comments, many=True).data
#
#         return Response(serialized_comments, status=status.HTTP_200_OK)
#
#
#     def delete(self, request, comment_id, *args, **kwargs):
#         try:
#             comment = Comment.objects.get(id=comment_id, user=request.user)
#         except Comment.DoesNotExist:
#             return Response({"error": "Comment not found or you don't have permission to delete it."},
#                             status=status.HTTP_404_NOT_FOUND)
#
#
#         comment.delete()
#
#         return Response({"message": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
#
#
# class CommentAPIView(APIView):
#
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = [IsAuthenticated,]
#
#     def post(self, request):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, comment_id):
#         try:
#             comment = Comment.objects.get(id=comment_id)
#             comment.delete()
#             return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except Comment.DoesNotExist:
#             return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)



class AddCommentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


