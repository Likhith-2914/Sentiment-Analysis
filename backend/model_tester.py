import unittest
from transformers import pipeline

harsh_classifier = pipeline("sentiment-analysis", model='nvsl/bert-for-harsh')
vulgar_classifier = pipeline("sentiment-analysis", model='nvsl/bert-for-vulgar')
threatening_classifier = pipeline("sentiment-analysis", model='nvsl/bert-for-threatening')

class Tester(unittest.TestCase):

    def test1(self):
        
        text = 'Thank you sir! I am grateful.'
        output = harsh_output = 'NOT_harsh'
        result = harsh_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, harsh_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")
    

    def test2(self):
        
        text = 'hey Stupid. shut up your mouth..'
        output = harsh_output = 'harsh'
        result = harsh_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, harsh_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")
    
    def test3(self):
        
        text = 'Hey rascal., Shut your mouth. You are such a brut'
        output = vulgar_output = 'vulgar'
        result = vulgar_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, vulgar_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")
    
    def test4(self):
        
        text = 'Thank you for the help! Sir'
        output = vulgar_output = 'NOT_vulgar'
        result = vulgar_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, vulgar_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")
    
    def test5(self):
        
        text = 'Bring money, else I will hurt your child.'
        output = threatening_output = 'threatening'
        result = threatening_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, threatening_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")
    
    def test6(self):
        
        text = 'Hey dont worry, I am there for you'
        output = threatening_output = 'NOT_threatening'
        result = threatening_classifier(text)
        label = result[0]['label']

        self.assertEqual(label, threatening_output)
        print('\r', end = '')
        print(f"Expected --> {output}, Predicted --> {label}")

    


if __name__ == '__main__':

    unittest.main()