from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow read-only for everyone; write only if request.user is the owner.
    Works for Post (author) and Comment (author).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # obj has .author in both Post and Comment
        return getattr(obj, 'author', None) == request.user
