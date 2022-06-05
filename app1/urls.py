
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from app1.views import IndexFuncionarioTemplateView, FuncionarioListView, FuncionarioUpdateView, \
    FuncionarioDeleteView, IndexClienteTemplateView, ClienteCreateView, ClienteListView, ClienteUpdateView, \
    ClienteDeleteView, IndexFornecedorTemplateView, FornecedorCreateView, FornecedorListView, FornecedorUpdateView, \
    FornecedorDeleteView, IndexProdutoTemplateView, ProdutoCreateView, ProdutoListView, ProdutoUpdateView, \
    ProdutoDeleteView, ProdutoFuncionarioListView, IndexOrcamentoTemplateView, OrcamentoCreateView, \
    OrcamentoListView, OrcamentoUpdateView, OrcamentoDeleteView, IndexMetaTemplateView, MetaCreateView, MetaListView, \
    MetaUpdateView, MetaDeleteView

from django.urls import path, include
from . import views
from .api import EventViewSet, CommetViewSet, OrcamentoViewSet

api_router = routers.DefaultRouter()
api_router.register(r"event", EventViewSet)
api_router.register(r"comment", CommetViewSet)
api_router.register(r"orcamento", OrcamentoViewSet)

router = routers.DefaultRouter()
router.register(r"events", views.EventViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"orcamento", views.OrcamentoViewSet)

app_name = 'app1'

urlpatterns = [
    path('login', views.loginn, name='login'),
    path('logout', views.logoutt, name='logout'),
    path('indexx', views.indexx, name='indexx'),
    path('manutencao', views.manutencao, name='manutencao'),
    path('funcionario/cadastrar/', views.funcionario, name="cadastra_funcionario"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api/", include(api_router.urls)),
    path("agenda", views.agenda, name="agenda-events"),
    path("all", views.all, name="agenda-events-all"),
    path("<int:id>", views.show, name="agenda-events-show"),
    path("<int:year>/<int:month>/<int:day>", views.day, name="agenda-events-day"),
    path("new", views.new, name="agenda-events-new"),
    path("delete/<int:id>", views.delete, name="agenda-events-delete"),
    path("edit", views.edit, name="agenda-events-edit"),



    # GET /
    path('principalfuncionario/', IndexFuncionarioTemplateView.as_view(), name="principalfuncionario"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),

    # GET/POST /funcionario/{pk}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    # GET/POST /funcionarios/excluir/{pk}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),

######################################################################################################

    # GET /
    path('principalcliente/', IndexClienteTemplateView.as_view(), name="principalcliente"),

    # GET /cliente/cadastrar
    path('cliente/cadastrar', ClienteCreateView.as_view(), name="cadastra_cliente"),

    # GET /clientes
    path('clientes/', ClienteListView.as_view(), name="lista_clientes"),

    # GET/POST /cliente/{pk}
    path('cliente/<pk>', ClienteUpdateView.as_view(), name="atualiza_cliente"),

    # GET/POST /cliente/excluir/{pk}
    path('cliente/excluir/<pk>', ClienteDeleteView.as_view(), name="deleta_cliente"),

######################################################################################################

    # GET /
    path('principal/fornecedor/', IndexFornecedorTemplateView.as_view(), name="principalfornecedor"),

    # GET /forncedor/cadastrar
    path('fornecedor/cadastrar', FornecedorCreateView.as_view(), name="cadastra_fornecedor"),

    # GET /fornecedores
    path('fornecedores/', FornecedorListView.as_view(), name="lista_fornecedores"),

    # GET/POST /fornecedor/{pk}
    path('fornecedor/<pk>', FornecedorUpdateView.as_view(), name="atualiza_fornecedor"),

    # GET/POST /fornecedor/excluir/{pk}
    path('fornecedor/excluir/<pk>', FornecedorDeleteView.as_view(), name="deleta_fornecedor"),

######################################################################################################

    # GET /
    path('principal/fornecedor/', IndexProdutoTemplateView.as_view(), name="principalproduto"),

    # GET /produto/cadastrar
    path('produto/cadastrar/', ProdutoCreateView.as_view(), name="cadastra_produto"),

    # GET /produtos
    path('produtos/', ProdutoListView.as_view(), name="lista_produtos"),

# GET /produtos
    path('produtos/funcionario/', ProdutoFuncionarioListView.as_view(), name="lista_produtos_funcionario"),

    # GET/POST /produto/{pk}
    path('produto/<pk>', ProdutoUpdateView.as_view(), name="atualiza_produto"),

    # GET/POST /produto/excluir/{pk}
    path('produto/excluir/<pk>', ProdutoDeleteView.as_view(), name="deleta_produto"),

######################################################################################################
######################################################################################################

    # GET /
    path('principal/orcamento/', IndexOrcamentoTemplateView.as_view(), name="principalorcamento"),

    # GET /orcamento/cadastrar
    path('orcamento/cadastrar/', OrcamentoCreateView.as_view(), name="cadastra_orcamento"),

    # GET /orcamentos
    path('orcamentos/', OrcamentoListView.as_view(), name="lista_orcamentos"),

    # GET/POST /orcamento/{pk}
    path('orcamento/<pk>', OrcamentoUpdateView.as_view(), name="atualiza_orcamento"),

    # GET/POST /orcamento/excluir/{pk}
    path('orcamento/excluir/<pk>', OrcamentoDeleteView.as_view(), name="deleta_orcamento"),

######################################################################################################

######################################################################################################

    # GET /
    path('principal/meta/', IndexMetaTemplateView.as_view(), name="principalmeta"),

    # GET /meta/cadastrar
    path('meta/cadastrar/', MetaCreateView.as_view(), name="cadastra_meta"),

    # GET /metas
    path('metas/', MetaListView.as_view(), name="lista_metas"),

    # GET/POST /meta/{pk}
    path('meta/<pk>', MetaUpdateView.as_view(), name="atualiza_meta"),

    # GET/POST /meta/excluir/{pk}
    path('meta/excluir/<pk>', MetaDeleteView.as_view(), name="deleta_meta"),


]


