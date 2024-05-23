from django.contrib import admin
from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from apps.user.choices import UserRanges, UserFacultad, UserPrograma

class UserInformationInline(admin.StackedInline):
    model = UserInformationModel
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_login', 'date_joined', 'information_user_type', 'information_facultad', 'information_programa')
    inlines = [UserInformationInline]

    def information_user_type(self, obj):
        return UserRanges.get_name(obj.information.user_type)
    information_user_type.short_description = 'Rol'

    def information_facultad(self, obj):
        return UserFacultad.get_name(obj.information.user_facultad)
    information_facultad.short_description = 'Facultad'
    
    def information_programa(self, obj):
        return UserPrograma.get_name(obj.information.user_programa)
    information_programa.short_description = 'Programa'

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
