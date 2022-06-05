from django.contrib import admin
from app1.models import Cliente, Funcionario, Fornecedor, Produto, Orcamento, Metas

from .models import Event, Comment


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Cria a classe EventAdmin com os parâmetros de exibição das
    informações do modelo Event dentro da interface de administração."""

    list_display = ("date", "event", "priority", "hora")
    list_display_links = ("event",)
    list_filter = ("date", "priority", "hora")
    list_editable = ("priority",)
    search_fields = ("event", "date", "hora")


admin.site.register(Comment)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Orcamento)
admin.site.register(Metas)


