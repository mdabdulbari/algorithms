import unittest


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):
    if node is None or node.next is None:
        raise ValueError
    node.val = node.next.val
    node.next = node.next.next


class TestSuite(unittest.TestCase):

    def test_delete_node(self):

        # make linkedlist 1 -> 2 -> 3 -> 4
        head = Node(1)
        curr = head
        for i in range(2, 6):
            curr.next = Node(i)
            curr = curr.next

        # node3 = 3
        node3 = head.next.next

        # after delete_node => 1 -> 2 -> 4
        delete_node(node3)

        curr = head
        self.assertEqual(1, curr.val)

        curr = curr.next
        self.assertEqual(2, curr.val)

        curr = curr.next
        self.assertEqual(4, curr.val)

        curr = curr.next
        self.assertEqual(5, curr.val)

        tail = curr
        self.assertIsNone(tail.next)

        self.assertRaises(ValueError, delete_node, tail)
        self.assertRaises(ValueError, delete_node, tail.next)


if __name__ == '__main__':

    unittest.main()