from rest_framework import permissions

from django.contrib.auth.models import Group

from apps.human_resource.models import EmploymentInformation
from apps.superadmin.models import *

class CreateUserPermission(permissions.BasePermission):
    """This determines whether a user is authorized to create users depending on their group

    Args:
        permissions ([type]): [description]
    """
    def has_permission(self, request, view):
        if request.user.role.name=="super_admin" or request.user.role.name=="human_resources":
            return True
        else:
            return False

class DeleteUserPermission(permissions.BasePermission):
    """This determines whether a user is authorized to create users depending on their group

    Args:
        permissions ([type]): [description]
    """
    def has_permission(self, request, view):
        if (request.user.role.name=="super_admin" or request.user.role.name=="human_resources") and check_company(request.user.pk,view.request.data['user']):
            if check_rank(request.user.pk,view.request.data['user']):
                return True
            else:
                return False
        else:
            return False

class ChangeRolePermission(permissions.BasePermission):
    """This defines the user with the permission to change another user's role

    Args:
        permissions ([type]): [description]
    """
    def has_permission(self, request, view):
        if request.user.role.name == "super_admin" and check_company(request.user.pk,view.request.data['user']):
            if request.user.pk == int(view.request.data['user']):
                return False
            else:
                return True
        else:
            return False

def check_company(user1,user2):
    """This will check if a two users are in the same company

    Args:
        user1 ([type]): [description]
        user2 ([type]): [description]
    """
    info1 = EmploymentInformation.objects.get(employee = Employee.objects.get(pk=user1))
    info2 = EmploymentInformation.objects.get(employee = Employee.objects.get(pk=user2))

    return info1.company == info2.company

def check_rank(doer,receiver):
    """This will set it such that a user who is not a superadmin cant delete a superadmin

    Args:
        doer ([type]): [description]
        receiver ([type]): [description]
    """
    if Employee.objects.get(pk=receiver).role.name == "super_admin" and Employee.objects.get(pk=doer).role.name != "super_admin":
        return False
    else:
        return True