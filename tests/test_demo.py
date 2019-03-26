from lino.utils.pythontest import TestCase


class TestCase(TestCase):

    def test_demo(self):
        self.run_django_manage_test('lino_weleup/demo')
