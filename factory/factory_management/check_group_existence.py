from django.contrib.auth.models import Group


class GroupChecker:
    group_name: str

    def __init__(self, name):
        self.group_name = name

    def check(self, permission):
        try:
            Group.objects.get(name='Can use APIs')
        except Exception:
            Group.objects.create(name='Can use APIs')
            Group.objects.get(name='Can use APIs').permissions.set([permission,])
        finally:
            group_with_access = Group.objects.get(name='Users with access')
            return group_with_access
