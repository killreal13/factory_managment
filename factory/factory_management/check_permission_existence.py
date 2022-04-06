from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class PermissionChecker:
    permission_codename: str
    permission_name: str

    def __init__(self, name, codename):
        self.permission_codename = codename
        self.permission_name = name

    def check(self, model_name):
        try:
            Permission.objects.get(name=self.permission_name)
        except Exception:
            content_type = ContentType.objects.get_for_model(model_name)
            Permission.objects.create(
                codename=self.permission_codename,
                name=self.permission_name,
                content_type=content_type
            )
        finally:
            permission = Permission.objects.get(name='Can use APIs')
            return permission
