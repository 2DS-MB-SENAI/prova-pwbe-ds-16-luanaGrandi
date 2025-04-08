from django.shortcuts import render
from .models import Servico, Agendamento
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ServicoSerializers, AgendamentoSerializers

# serviços
@api_view(['GET'])
def read_servicos(request):
    servico = Servico.objects.all()
    serializer = ServicoSerializers(servico, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def detalhes_servicos(request, pk):
    try:
        servico = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
       return Response({'Erro': 'servico não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServicoSerializers(servico)
    return Response(serializer.data)


@api_view(['POST']) #criar
def create_servicos(resuest):
    if resuest.method == 'POST':
        serializer = ServicoSerializers(data = resuest.data, many=isinstance(resuest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# agendamentos

@api_view(['GET'])
def read_agendamentos(request):
    agendamentos = Servico.objects.all()
    serializer = AgendamentoSerializers(agendamentos, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def detalhes_agendametos(request, pk):
    try:
        agendamentos = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:
       return Response({'Erro': 'agendamento não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendamentoSerializers(agendamentos)
    return Response(serializer.data)

@api_view(['POST']) #criar
def create_agendamentos(resuest):
    if resuest.method == 'POST':
        serializer = AgendamentoSerializers(data = resuest.data, many=isinstance(resuest.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)