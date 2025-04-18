# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .Serializer.UserSerializer import UserSerializer
# from Domain.Models.User import User
# from Application.Services.UserService import UserService
# from Infrastructure.Adapters.UserRepositoryI import UserRepositoryI


# class CreateUserView(APIView):

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user_data = serializer.validated_data
#             repositoryImple =  UserRepositoryI()
#             userService =  UserService(repositoryImple)
#             user = userService.ViewInformation(user_data)
#             # Retornar el objeto de dominio como respuesta
#             #print(""+user.nombre)
#             return Response({
#                 "Se imprimio"
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)