from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS



class IsOwnerOrAdminOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
            
        if request.method == 'GET':
            return True
            
        return request.user==obj.owner or request.user.is_staff