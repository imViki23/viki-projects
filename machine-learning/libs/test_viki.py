# test_my_math_builtin.py
import unittest
import viki as vk

class TestMyMath(unittest.TestCase):
    
    def test_mean(self):
        a = vk.asarray([10, 20, 30])
        self.assertEqual(vk.mean(a), 20.0)

if __name__ == '__main__':
    unittest.main()