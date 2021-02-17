from django.test import TestCase
from desiderata.models import Desiderata
from infra.save_deep import save_deep

class TestDesiderata(TestCase):

    def test_ordering(self):
        desideratas = [
            save_deep(Desiderata.example().with_ordering(9999)), # 0
            save_deep(Desiderata.example().with_ordering(-1)), # 1
            save_deep(Desiderata.example().with_ordering(2).with_name('aaaa')), # 2
            save_deep(Desiderata.example().with_ordering(2).with_name('bbbb')), # 3
            save_deep(Desiderata.example().with_ordering(2).with_name('aaaa')) # 4
        ]

        res = Desiderata.objects.all()

        # 1, 2, 4, 3, 0
        self.assertEqual(desideratas[1], res[0])
        self.assertEqual(desideratas[2], res[1])
        self.assertEqual(desideratas[4], res[2])
        self.assertEqual(desideratas[3], res[3])
        self.assertEqual(desideratas[0], res[4])
        