from django.contrib.auth.mixins import UserPassesTestMixin

class ReceptonistPassesTestMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_employee and self.request.user.is_receptonist