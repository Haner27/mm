import unittest

from bson import ObjectId

from test.data.common_data import create_int, create_str
from test.data.build_order import Order
from test.data.build_user import User


class TestOder(unittest.TestCase):
    def setUp(self):  # 执行每个测试用例前都执行
        cost = create_int(5)
        order = Order(cost)
        self.order = order
        print('start--->>')

    def tearDown(self):  # 执行每个测试用例后都执行
        print('end<<---')

    def test_create_order(self):
        self.assertEqual(len(self.order.users), 0)
        self.assertEqual(isinstance(self.order.id, ObjectId), True)

    def test_order_add_user(self):
        name = create_str(4)
        age = create_int(2)
        user = User(name=name, age=age)
        pre_user_count = len(self.order.users)
        self.order.add_user(user)
        post_user_count = len(self.order.users)
        self.assertEqual(pre_user_count, post_user_count - 1)

    def test_update_order(self):
        cost = create_int(5)
        self.order.update_cost(cost)
        self.assertEqual(self.order.cost, cost)

    def test_rm_user(self):
        name = create_str(4)
        age = create_int(2)
        user = User(name=name, age=age)
        self.order.users.append(user)
        pre_user_count = len(self.order.users)
        self.order.rm_user(user)
        post_user_count = len(self.order.users)
        self.assertEqual(pre_user_count, post_user_count + 1)


if __name__ == '__main__':
    unittest.main()
