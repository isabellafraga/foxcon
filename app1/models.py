from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from libgravatar import Gravatar


# Classe Cliente

class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True)
    sobrenome = models.CharField(max_length=100, blank=False, null=True)
    nascimento = models.DateField(blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    CNPJ = models.CharField(max_length=18, blank=False, null=True)
    telefone = models.CharField(max_length=12, blank=False, null=True)
    endereco = models.CharField(max_length=150, blank=False, null=True)

    objetos = models.Manager()

    def __str__(self):
        return self.nome

# Classe Funcionario
class Funcionario(models.Model):
    CARGO_CHOICES = [
        ["Técnico", "Técnico"],
        ["Vendedor", "Vendedor"],
        ["Gerente", "Gerente"]
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=True)
    CPF = models.CharField(max_length=14, blank=False, null=True)
    nascimento = models.DateField(blank=False, null=True)
    telefone = models.CharField(max_length=14, blank=False, null=True)
    endereco = models.CharField(max_length=150, blank=False, null=True)
    CTPS = models.CharField(max_length=11, blank=False, null=True)
    salario = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=True)
    admissao = models.DateField(auto_now=True, blank=False, null=True)
    cargo = models.CharField(max_length=8, blank=False, choices=CARGO_CHOICES, null=True)

    objetos = models.Manager()

    def __str__(self):
        return self.usuario.first_name

# Classe Fornecedor
class Fornecedor(models.Model):
    CATEGORIA_CHOICES = [
        ["CFTV", "CFTV"],
        ["AL", "Alarme"],
        ["CA", "Controle de Acesso"],
        ["TE", "Telefonia"],
        ["RE", "Redes"],
        ["PE", "Portão Eletrônico"],
    ]
    nome = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    telefone = models.CharField(max_length=14, blank=False, null=True)
    endereco = models.CharField(max_length=150, blank=False, null=True)
    CNPJ = models.CharField(max_length=18, blank=False, null=True)
    categoria = models.CharField(max_length=6, blank=False, choices=CATEGORIA_CHOICES, null=True)

    objetos = models.Manager()

    def __str__(self):
        return self.nome

# Classe Produtos
class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    nomep = models.CharField(max_length=100, blank=False, null=True)
    quantidade = models.DecimalField(max_digits=5,decimal_places=0, blank=False, null=True)
    preco = models.DecimalField(max_digits=15,decimal_places=2, null=True)

    CATEGORIA_CHOICES = [
        ["CFTV", "CFTV"],
        ["AL", "Alarme"],
        ["CA", "Controle de Acesso"],
        ["TE", "Telefonia"],
        ["RE", "Redes"],
        ["PE", "Portão Eletrônico"],
    ]
    categoria = models.CharField(max_length=6, blank=False, choices=CATEGORIA_CHOICES, null=True)

    objetos = models.Manager()

    def __str__(self):
      return self.nomep
# Classe Orçamento
class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True)
    data = models.DateField(null=True)
    CATEGORIA_CHOICES = [
        ["CFTV", "CFTV"],
        ["AL", "Alarme"],
        ["CA", "Controle de Acesso"],
        ["TE", "Telefonia"],
        ["RE", "Redes"],
        ["PE", "Portão Eletrônico"],
    ]
    categoria = models.CharField(max_length=6, blank=False, choices=CATEGORIA_CHOICES, null=True)

    objetos = models.Manager()

    def __str__(self):
        return self.cliente.nome

# Classe Agenda
class Event(models.Model):
    """Classe contendo a agenda propriamente dito, sua data, descrição
    e também prioridade."""
    date = models.DateField(null=True)
    PERIODO_CHOICES = [
        ("8:00", "8:00"), ("8:30", "8:30"), ("9:00", "9:00"), ("9:30", "9:30"), ("10:00", "10:00"), ("10:30", "10:30"),
        ("11:00", "11:00"), ("11:30", "11:30"), ("13:30", "13:30"), ("14:00", "14:00"), ("14:30", "14:30"), ("15:00", "15:00"),
        ("15:30", "15:30"), ("16:00", "16:00"), ("16:30", "16:30"), ("17:00", "17:00"), ("17:30", "17:30"), ("18:00", "18:00"),
    ]
    hora = models.CharField(max_length=18, choices=PERIODO_CHOICES, null=True)
    event = models.CharField(max_length=80, null=True)
    priorities_list = (
        ("0", "Sem prioridade"),
        ("1", "Normal"),
        ("2", "Urgente"),
        ("3", "Muito Urgente"),
    )
    priority = models.CharField(max_length=1, choices=priorities_list, null=True)


    class Meta:
        ordering = ("-date", "hora", "-priority", "event")

    def number_of_comments(self):
        """Retorna a quantidade de comentários dentro de um serviço."""
        return self.comment_event.count()

    @property
    def text_priority(self):
        """ Converte o valor da prioridade no texto correspondente. """
        for k, v in self.priorities_list:
            if k == self.priority:
                return v
        return ""

    def __str__(self):
        return self.event

# Classe Comentários de Serviços
class Comment(models.Model):
    """Comentários efetuados em um determinado serviço."""

    usuario = models.CharField(max_length=100, blank=False, null=True)
    text = models.CharField(max_length=160, null=True)
    commented = models.DateTimeField(default=timezone.now, null=True)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="comment_event", null=True
    )

    class Meta:
        ordering = ("-commented",)

    def __str__(self):
        return "'{}' em {:%c}".format(
            self.text, self.commented
        )



# Classe Metas
class Metas(models.Model):
    MESES_CHOICES = [
        ["Janeiro", "Janeiro"], ["Fevereiro", "Fevereiro"], ["Março", "Março"], ["Abril", "Abril"], ["Maio", "Maio"],
        ["Junho", "Junho"], ["Julho", "Julho"], ["Agosto", "Agosto"], ["Setembro", "Setembro"], ["Outubro", "Outrubro"],
        ["Novembro", "Novembro"], ["Dezembro", "Dezembro"]
    ]
    meses = models.CharField(max_length=10, blank=False, choices=MESES_CHOICES, null=True)
    meta = models.CharField(max_length=150, blank=False, null=True)
    data = models.DateField(blank=False, null=True)
    CARGO_CHOICES = [
        ["Vendedor", "Vendedor"],
        ["Técnico", "Técnico"]
    ]
    cargo = models.CharField(max_length=8, blank=False, choices=CARGO_CHOICES, null=True)
    CONCLUIDA_CHOICES = [
        ["Sim", "Sim"],
        ["Não", "Não"]
    ]
    concluida = models.CharField(max_length=3, choices=CONCLUIDA_CHOICES, blank=False, null=True)

    objetos = models.Manager()

    def __str__(self):
        return self.meta

