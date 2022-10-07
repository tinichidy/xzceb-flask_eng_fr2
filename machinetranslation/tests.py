import unittest

from mymodule import frenchToEnglish, englishToFrench

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 2 is given as input the output is 4.
        

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when 2 is given as input the output is 4.
    
unittest.main()
