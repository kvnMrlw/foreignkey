from django.contrib import admin
from .models import Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields = ('criado_por',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.criado_por = request.user
        return super().save_model(request, obj, form, change)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(criado_por=request.user )
    


admin.site.register(Produto, ProdutoAdmin)