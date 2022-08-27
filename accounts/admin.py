import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm,CustomUserChangeForm
from accounts.models import CustomerUser
# Register your models here.

 
class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomerUser
    list_display = ['email', 'username', 'age', 'is_staff', ] 
    fieldsets = (
        ('General' , {'fields':['email', 'username',  'is_staff', ]}),
        ('age',{'fields': ['age']})
        )
    
    # fieldsets = (
    #     ('General',
    #      {'fields': ['name_product', 'brand', 'descriptions']}),
    #     ('Info', {'fields': ['price', 'number_store', 'category', 'status', 'discount']}),
    #     ('Image', {'fields': ['image']})
    # )
    list_filter = ['email', 'username', 'age', 'is_staff']
    search_fields = ['email', 'username', 'age', 'is_staff']
    # add_fieldsets = UserAdmin.add_fieldsets + ( # new
    # (None, {'fields': ('age',)}),
    # )
    
admin.site.register(CustomerUser,CustomerUserAdmin)