from rest_framework.permissions import BasePermission

class AddedBy(BasePermission):
    message = "You are not the owner of this Item"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.added_by == request.user:
            return True
        return False