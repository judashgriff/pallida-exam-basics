import unittest
import unique_chars

class Test_unique_chars(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(unique_chars.unique_characters(""), [])

    def test_if_only_same_letters(self):
        self.assertEqual(unique_chars.unique_characters("aaaaaaaa"), ["a"])
        
    def test_if_different_words(self):
        self.assertEqual(unique_chars.unique_characters("these are different words"), ['t', 'h', 'e', 's', 'a', 'r', 'd', 'i', 'f', 'n', 'w', 'o'])
        

if __name__ == "__main__":
    unittest.main()