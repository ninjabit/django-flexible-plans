from django.contrib import admin
import swapper


class CustomerAdmin(admin.ModelAdmin):
    """
        Use it in your app.
    """

    list_display = ('user',)
    # list_filter = ('status', 'created_on', 'paid_on')
    search_fields = ('user', )
    # raw_id_fields = ('order', )


admin.site.register(swapper.load_model('flexible_plans', 'Customer'), CustomerAdmin)
