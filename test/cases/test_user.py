import unittest


class TestUser(unittest.TestCase):
    def setUp(self):  # 执行每个测试用例前都执行
        print('start')

    def tearDown(self):  # 执行每个测试用例后都执行
        print('end')

    def test_create_user(self):
        pass

    def test_update_user(self):
        pass

    def test_remove_user(self):
        pass


if __name__ == '__main__':
    unittest.main()