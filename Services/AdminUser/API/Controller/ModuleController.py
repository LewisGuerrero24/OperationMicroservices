from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uuid import UUID
from ..Serializer.Module.ModuleSerializer import ModuleSerializer
from ..Serializer.Module.ModuleSerializerUnique import ModuleSerializerUnique
from Application.Services.Module_Services import Module_Services
from Infrastructure.Adapters.ModuleRepositoryI import ModuleRepositoryImpl
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ModuleListController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._module_service = Module_Services(ModuleRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene todos los modulos",
        responses={200: ModuleSerializer(many=True)}
    )
    def get(self, request):
        modules = self._module_service.list_all()
        serialized_modules = ModuleSerializer(modules, many=True)
        return Response(serialized_modules.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ModuleSerializerUnique,
        operation_description="Crea un nuevo modulo",
        responses={201: ModuleSerializerUnique, 400: "Datos inválidos"}
    )
    def post(self, request):
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            module_data = serializer.validated_data
            module = self._module_service.create(module_data)
            return Response(ModuleSerializer(module).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModuleDetailController(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._module_service = Module_Services(ModuleRepositoryImpl())

    @swagger_auto_schema(
        operation_description="Obtiene un modulo por ID",
        responses={200: ModuleSerializer(), 404: "modulo no encontrado"}
    )
    def get(self, request, module_id):
        try:
            module = self._module_service.get(module_id)
            return Response(ModuleSerializer(module).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=ModuleSerializerUnique,
        operation_description="Actualiza un modulo existente",
        responses={200: ModuleSerializerUnique, 400: "Datos inválidos", 404: "modulo no encontrado"}
    )
    def put(self, request, module_id):
        serializer = ModuleSerializerUnique(data=request.data)
        if serializer.is_valid():
            module_data = serializer.validated_data
            try:
                module = self._module_service.update(module_id, module_data)
                return Response(ModuleSerializer(module).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Elimina un modulo por ID",
        responses={
            204: "modulo eliminado",
            400: "No se pudo eliminar el modulo",
            404: "modulo no encontrado"
        }
    )
    def delete(self, request, module_id):
        try:
            result = self._module_service.delete(module_id)
            if result:
                return Response({'message': 'modulo eliminado'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'No se pudo eliminar el modulo'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)