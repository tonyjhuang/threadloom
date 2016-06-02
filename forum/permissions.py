from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed on all requests,
        # so always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions for owner only.
        return obj.owner == request.user

class NotAuthenticatedCreateOrReadOnly(permissions.BasePermission):
    """
    Allow non-authenticated POSTs to create objects.
    """
    def has_permission(self, request, view):
        """
        Grant permission if the request is an unauthenticated POST or
        a safe method (GET, HEAD, OPTION).
        """
        return ((not request.user.is_authenticated() and request.method == "POST")
                or (request.method in permissions.SAFE_METHODS))

class IsSameUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed on all requests,
        # so always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only grant write permissions if the target user object
        # is the same as the request user.
        return obj == request.user
