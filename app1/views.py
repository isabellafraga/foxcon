from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from app1.forms import FormCliente, FormFuncionario, FormFornecedor, FormProduto, EventForm, CommentForm, FormOrcamento, \
    FormMeta
from app1.models import Funcionario, Cliente, Fornecedor, Produto, Event, Comment, Orcamento, Metas
from app1.serializers import CommentSerializer, EventSerializer, OrcamentoSerializer
from app1.services import split_str_date

ITEMS_PER_PAGE = 5
FIRST_PAGE = 1


# PÁGINA PRINCIPAL INDEX
# ----------------------------------------------
def indexx(request):
    return render(request, 'app3/index.html')


# PÁGINA PRINCIPAL MANUTENÇÃO
# ----------------------------------------------
def manutencao(request):
    return render(request, 'app3/manutencao.html')


# PÁGINA PRINCIPAL LOGIN
# ----------------------------------------------
def loginn(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('app1:indexx'))
            else:
                return HttpResponse("Sua Conta Não Esta Ativa.")
        else:
            print("Alguém Tentou Fazer Login e Falhou")
            print("Foi Usado userName: {} e senha: {}".format(usuario, senha))
            return HttpResponse("O Login ou Senha Está Incorreto.")

    else:
        return render(request, 'app3/login.html', {})


# PÁGINA PRINCIPAL LOGOUT
# ----------------------------------------------
@login_required
def logoutt(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


# PÁGINA CADASTRO FUNCIONARIO
# ----------------------------------------------

def funcionario(request):
    if request.method == 'POST':
        form = FormFuncionario(request.POST)

        if form.is_valid():
            usuario = User()
            usuario.first_name = form.cleaned_data['first_name']
            usuario.last_name = form.cleaned_data['last_name']
            usuario.email = form.cleaned_data['email']
            usuario.username = form.cleaned_data['username']
            usuario.password = form.cleaned_data['password']

            usuario.save()
            usuario.set_password(usuario.password)
            usuario.save()

            func = Funcionario()
            func.CPF = form.cleaned_data['CPF']
            func.nascimento = form.cleaned_data['nascimento']
            func.telefone = form.cleaned_data['telefone']
            func.endereco = form.cleaned_data['endereco']
            func.CTPS = form.cleaned_data['CTPS']
            func.cargo = form.cleaned_data['cargo']

            func.usuario = usuario
            func.save()
            return HttpResponseRedirect(reverse('app1:lista_funcionarios'))

    else:
        form = FormFuncionario()

    return render(request, 'app3/funcionario/cadastra.html', {'form': form, })


# PÁGINA PRINCIPAL FUNCIONARIO
# ----------------------------------------------

class IndexFuncionarioTemplateView(TemplateView):
    template_name = "app3/funcionario/principal.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioListView(ListView):
    template_name = "app3/funcionario/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "app3/funcionario/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("app1:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "app3/funcionario/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("app1:lista_funcionarios")


##################################################################################

# PÁGINA PRINCIPAL CLIENTE
# ----------------------------------------------

class IndexClienteTemplateView(TemplateView):
    template_name = "app3/cliente/principal.html"


# LISTA DE CLIENTE
# ----------------------------------------------

class ClienteListView(ListView):
    template_name = "app3/cliente/lista.html"
    model = Cliente
    context_object_name = "clientes"


# CADASTRAMENTO DE CLIENTE
# ----------------------------------------------

class ClienteCreateView(CreateView):
    template_name = "app3/cliente/cadastra.html"
    model = Cliente
    form_class = FormCliente
    success_url = reverse_lazy("app1:lista_clientes")


# ATUALIZAÇÃO DE CLIENTE
# ----------------------------------------------

class ClienteUpdateView(UpdateView):
    template_name = "app3/cliente/atualiza.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("app1:lista_clientes")


# EXCLUSÃO DE CLIENTE
# ----------------------------------------------

class ClienteDeleteView(DeleteView):
    template_name = "app3/cliente/exclui.html"
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy("app1:lista_clientes")


##################################################################################

# PÁGINA PRINCIPAL FORNECEDOR
# ----------------------------------------------

class IndexFornecedorTemplateView(TemplateView):
    template_name = "app3/fornecedor/principal.html"


# LISTA DE FORNECEDOR
# ----------------------------------------------

class FornecedorListView(ListView):
    template_name = "app3/fornecedor/lista.html"
    model = Fornecedor
    context_object_name = "fornecedores"


# CADASTRAMENTO DE FORNECEDOR
# ----------------------------------------------

class FornecedorCreateView(CreateView):
    template_name = "app3/fornecedor/cadastra.html"
    model = Fornecedor
    form_class = FormFornecedor
    success_url = reverse_lazy("app1:lista_fornecedores")


# ATUALIZAÇÃO DE FORNECEDOR
# ----------------------------------------------

class FornecedorUpdateView(UpdateView):
    template_name = "app3/fornecedor/atualiza.html"
    model = Fornecedor
    fields = '__all__'
    context_object_name = 'fornecedor'
    success_url = reverse_lazy("app1:lista_fornecedores")


# EXCLUSÃO DE FORNECEDOR
# ----------------------------------------------

class FornecedorDeleteView(DeleteView):
    template_name = "app3/fornecedor/exclui.html"
    model = Fornecedor
    context_object_name = 'fornecedor'
    success_url = reverse_lazy("app1:lista_fornecedores")


##################################################################################

# LISTA DE PRODUTO
# ----------------------------------------------

class ProdutoFuncionarioListView(ListView):
    template_name = "app3/produto/listafuncionario.html"
    model = Produto
    context_object_name = "produtos"


# PÁGINA PRINCIPAL PRODUTO
# ----------------------------------------------

class IndexProdutoTemplateView(TemplateView):
    template_name = "app3/fornecedor/principal.html"


# LISTA DE PRODUTO
# ----------------------------------------------

class ProdutoListView(ListView):
    template_name = "app3/produto/lista.html"
    model = Produto
    context_object_name = "produtos"


# CADASTRAMENTO DE PRODUTO
# ----------------------------------------------

class ProdutoCreateView(CreateView):
    template_name = "app3/produto/cadastra.html"
    model = Produto
    form_class = FormProduto
    success_url = reverse_lazy("app1:lista_produtos")


# ATUALIZAÇÃO DE PRODUTO
# ----------------------------------------------

class ProdutoUpdateView(UpdateView):
    template_name = "app3/produto/atualiza.html"
    model = Produto
    fields = '__all__'
    context_object_name = 'produto'
    success_url = reverse_lazy("app1:lista_produtos")


# EXCLUSÃO DE PRODUTO
# ----------------------------------------------

class ProdutoDeleteView(DeleteView):
    template_name = "app3/produto/exclui.html"
    model = Produto
    context_object_name = 'produto'
    success_url = reverse_lazy("app1:lista_produtos")


##################################################################################

class OrcamentoViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza os eventos da agenda como uma API REST.
    """

    queryset = Orcamento.objetos.all()
    serializer_class = OrcamentoSerializer

    permission_classes = (IsAuthenticated,)

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza os eventos da agenda como uma API REST.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Disponibiliza os eventos da agenda como uma API REST.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("event__id",)

    permission_classes = (IsAuthenticated,)


# PÁGINA PRINCIPAL AGENDA
# ----------------------------------------------
@login_required
def agenda(request):
    """
    Exibe a página principal da aplicaão.
    """
    context = {
        "hide_new_button": True,
        "priorities": Event.priorities_list,
        "today": localdate(),
    }

    return render(request, "app3/agenda/agenda.html", context)


@login_required
def all(request):
    """
    Exibe todas os eventos consolidados em uma única página, recebe o
    número da página a ser visualizada via GET.
    """

    page = request.GET.get("page", FIRST_PAGE)
    paginator = Paginator(Event.objects.all(), ITEMS_PER_PAGE)
    total = paginator.count

    try:
        events = paginator.page(page)
    except InvalidPage:
        events = paginator.page(FIRST_PAGE)

    context = {
        "events": events,
        "total": total,
        "priorities": Event.priorities_list,
        "today": localdate(),
    }

    return render(request, "app3/agenda/events.html", context)


@login_required
def day(request, year: int, month: int, day: int):
    """
    Visualização dos eventos de um determinado dia, recebe a data em
    formato ano/mês/dia como parâmetro.
    """

    day = datetime(year, month, day)
    filted_events = Event.objects.filter(
        date="{:%Y-%m-%d}".format(day)
    ).order_by("-priority", "event")

    context = {
        "today": localdate(),
        "day": day,
        "events": filted_events,
        "next": day + timedelta(days=1),
        "previous": day - timedelta(days=1),
        "priorities": Event.priorities_list,
    }

    return render(request, "app3/agenda/day.html", context)


@login_required
def delete(request, id: int):
    """
    Apaga um evento específico, se o evento não existir resultará em
    erro 404, se algo errado ocorrer retornará a página de erro.
    """
    event = get_object_or_404(Event, id=id)
    (year, month, day) = split_str_date("{:%Y-%m-%d}".format(event.date))

    if event.delete():
        return redirect("app1:agenda-events-day", year=year, month=month, day=day)
    else:
        return server_error(request, "ops_500.html")


@login_required
def edit(request):
    """
    Edita o conteúdo de um evento, recebendo os dados enviados pelo
    formulário, validando e populando em um evento já existente.
    """
    form = EventForm(request.POST)

    if form.is_valid():
        event = get_object_or_404(Event, id=request.POST["id"])
        event.date = form.cleaned_data["date"]
        event.hora = form.cleaned_data["hora"]
        event.event = form.cleaned_data["event"]
        event.priority = form.cleaned_data["priority"]
        event.save()
        (year, month, day) = split_str_date("{:%Y-%m-%d}".format(event.date))
        return redirect("app1:agenda-events-day", year=year, month=month, day=day)
    else:
        return bad_request(request, None, "ops_400.html")


@login_required
def new(request):
    """
    Recebe os dados de um novo evento via POST, faz a validação dos dados
    e aí insere na base de dados.
    """
    form = EventForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        # e uso a data enviada pelo formulário para o redirecionamento.
        year, month, day = split_str_date(request.POST["date"])

        return redirect("app1:agenda-events-day", year=year, month=month, day=day)
    else:
        return bad_request(request, None, "ops_400.html")


def show(request, id: int):
    """
    Visualização de um determinado evento e de seus comentários, recebe
    o 'id' do evento. Caso seja acessado via POST insere um novo comentário.
    """
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("app1:agenda-events-show", id=id)

    context = {
        "event": event,
        "comments": Comment.objects.filter(event=id).order_by("-commented"),
        "hide_new_button": True,
        "priorities": Event.priorities_list,
        "today": localdate(),
    }

    return render(request, "app3/agenda/show.html", context)


##################################################################################

# LISTA DE ORÇAMENTO
# ----------------------------------------------

class OrcamentoListView(ListView):
    template_name = "app3/orcamento/lista.html"
    model = Orcamento
    context_object_name = "orcamentos"


# PÁGINA PRINCIPAL ORÇAMENTO
# ----------------------------------------------

class IndexOrcamentoTemplateView(TemplateView):
    template_name = "app3/orcamento/principal.html"


# CADASTRAMENTO DE ORÇAMENTO
# ----------------------------------------------

class OrcamentoCreateView(CreateView):
    template_name = "app3/orcamento/cadastra.html"
    model = Orcamento
    form_class = FormOrcamento
    success_url = reverse_lazy("app1:lista_orcamentos")


# ATUALIZAÇÃO DE ORÇAMENTO
# ----------------------------------------------

class OrcamentoUpdateView(UpdateView):
    template_name = "app3/orcamento/atualiza.html"
    model = Orcamento
    fields = '__all__'
    context_object_name = 'orcamento'
    success_url = reverse_lazy("app1:lista_orcamentos")


# EXCLUSÃO DE ORÇAMENTO
# ----------------------------------------------

class OrcamentoDeleteView(DeleteView):
    template_name = "app3/orcamento/exclui.html"
    model = Orcamento
    context_object_name = 'orcamento'
    success_url = reverse_lazy("app1:lista_orcamentos")


##################################################################################

# LISTA DE META
# ----------------------------------------------

class MetaListView(ListView):
    template_name = "app3/meta/lista.html"
    model = Metas
    context_object_name = "metas"


# PÁGINA PRINCIPAL META
# ----------------------------------------------

class IndexMetaTemplateView(TemplateView):
    template_name = "app3/meta/principal.html"


# CADASTRAMENTO DE META
# ----------------------------------------------

class MetaCreateView(CreateView):
    template_name = "app3/meta/cadastra.html"
    model = Metas
    form_class = FormMeta
    success_url = reverse_lazy("app1:lista_metas")


# ATUALIZAÇÃO DE META
# ----------------------------------------------

class MetaUpdateView(UpdateView):
    template_name = "app3/meta/atualiza.html"
    model = Metas
    fields = '__all__'
    context_object_name = 'meta'
    success_url = reverse_lazy("app1:lista_metas")


# EXCLUSÃO DE META
# ----------------------------------------------

class MetaDeleteView(DeleteView):
    template_name = "app3/meta/exclui.html"
    model = Metas
    context_object_name = 'meta'
    success_url = reverse_lazy("app1:lista_metas")
