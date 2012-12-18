from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from relationships.forms import RelationshipStatusAdminForm
from relationships.models import Relationship, RelationshipStatus

class RelationshipInline(admin.TabularInline):
    model = Relationship
    raw_id_fields = ('from_user', 'to_user')
    fk_name = 'from_user'
    readonly_fields = ('to_user', 'status', 'last_contacted_at')
    exclude = ('weight', 'site')

    def queryset(self, request):
        qs = super(RelationshipInline, self).queryset(request)
        qs = qs.select_related('from_user', 'to_user', 'status')
        return qs

    def has_add_permission(self, request):
        return False


class UserRelationshipAdmin(UserAdmin):
    inlines = (RelationshipInline,)


class RelationshipStatusAdmin(admin.ModelAdmin):
    form = RelationshipStatusAdminForm

admin.site.unregister(User)
admin.site.register(User, UserRelationshipAdmin)
admin.site.register(RelationshipStatus, RelationshipStatusAdmin)
