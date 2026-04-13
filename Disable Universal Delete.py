Add this to last line of smcapp1 admin.py

# ----------------------------------------------------------
# Disable delete actions globally (Sweeet)
# ----------------------------------------------------------
from django.contrib import admin

# Disable "Delete selected" safely
if 'delete_selected' in admin.site._actions:
    admin.site.disable_action('delete_selected')

# Disable delete permission everywhere
def no_delete_permission(self, request, obj=None):
    return False

admin.ModelAdmin.has_delete_permission = no_delete_permission
