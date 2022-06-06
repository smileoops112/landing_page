from django.contrib import admin
from .models import StatusCms, Order, CommentCms


class CommentAdmin(admin.StackedInline):

    model = CommentCms
    fields = ('comment_dt', 'comment')
    readonly_fields = ('comment_dt',)
    extra = 1


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone',)
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 5
    list_max_show_all = 50
    fields = ('id', 'order_dt', 'order_status', 'order_name', 'order_phone')
    readonly_fields = ('order_dt', 'id')
    inlines = [CommentAdmin,]


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCms)
admin.site.register(CommentCms)
