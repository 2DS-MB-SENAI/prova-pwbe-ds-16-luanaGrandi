from rest_framework import serializers
from .models import Servico, Agendamento

class ServicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class AgendamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

    