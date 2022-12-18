import unittest
from fib import get_fib_number_at_pos, get_fib_seq, fib


class TEST(unittest.TestCase):
    def test_Pos9(self):
        self.assertEqual(34, get_fib_number_at_pos(9))

    def test_SeqOf5(self):
        self.assertEqual([1, 1, 2, 3, 5], get_fib_seq(5))

    def test_LenSeqOf10(self):
        self.assertEqual(10, len(get_fib_seq(10)))

if __name__ == "__main__":
    unittest.main()