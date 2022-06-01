from django.contrib import admin
from .models import StatusCms, Order, CommentCms


admin.site.register(Order)
admin.site.register(StatusCms)
admin.site.register(CommentCms)
