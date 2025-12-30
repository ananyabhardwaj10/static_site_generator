import unittest
from extract_title import extract_title

class test_extracting_titles(unittest.TestCase):
    def test_title(self):
        block = '''
# This is a heading. 
## This is another heading.
'''
        mark = extract_title(block)
        self.assertEqual(mark, "This is a heading.")

    def testing_title_extraction(self):
        block = '''
### This is H3. #### This is H4.
# This is H1.
'''