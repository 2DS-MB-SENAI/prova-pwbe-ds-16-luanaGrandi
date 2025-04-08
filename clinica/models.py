from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=24)
    crm = models.CharField(max_length=34)
    email = models.EmailField(max_length=34)
    escolha_especialidade =(
        ('Pediatra', 'Pediatra'),
        ('Clinico Geral', 'Clinico Geral'),
        ('Ortopedista', 'Ortopedista'),
        ('Cirurgião', 'Cirurgião' ),
        ('CAR', 'Cardiologistas'),
    )
    especialidade = models.CharField(max_length=15, choices=escolha_especialidade)

    REQUIRED_FIELDS = ['nome', 'crm','especialidade']

    def __str__(self):
        return self.nome
    

class Consulta(models.Model):
    paciente = models.CharField(max_length=30)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    escolha_status = (
        ('Agendaado', 'Agendado'),
        ('Realizado', 'Realizado'),
        ('Cancelado', 'cancelado'),
    )
    status =  models.CharField(max_length=10, choices=escolha_status)

    def __str__(self):
        return self.paciente
    
