from django.db.models import PROTECT
from django.db.models import ProtectedError
from rest_framework import parsers
from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from uccaApp.util.exceptions import DependencyFailedException
from uccaApp.util.functions import has_permissions_to
from uccaApp.filters.projects_filter import ProjectsFilter
from uccaApp.serializers import ProjectSerializer
from uccaApp.models.Projects import Projects

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    filter_class = ProjectsFilter

    def get_queryset(self):
        if has_permissions_to(self.request.user.id, 'view_projects'):
            return self.queryset
        else:
            raise PermissionDenied

    def create(self, request, *args, **kwargs):
        if has_permissions_to(self.request.user.id, 'add_projects'):
            ownerUser = self.request.user
            request.data['created_by'] = ownerUser
            return super(self.__class__, self).create(request)
        else:
            raise PermissionDenied

    def destroy(self, request, *args, **kwargs):
        if has_permissions_to(self.request.user.id, 'delete_projects'):
            try:
                return super(self.__class__, self).destroy(request)
            except ProtectedError:
                raise DependencyFailedException
        else:
            raise PermissionDenied


    def update(self, request, *args, **kwargs):
        if has_permissions_to(self.request.user.id, 'change_projects'):
            return super(self.__class__, self).update(request)
        else:
            raise PermissionDenied
