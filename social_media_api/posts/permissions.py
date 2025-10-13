from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission: only the author can edit/delete.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # For Post and Comment, check `author` attribute
        return getattr(obj, "author", None) == request.user
