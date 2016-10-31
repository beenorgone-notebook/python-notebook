import unittest
import two_arrays

class KnownValues(unittest.TestCase):
   input_file = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-roxetta_code/two_arrays_input1.txt'
   output_file = '/home/beenorgone/Documents/gDrive/Self-learning/Themes/Python/python_practices-roxetta_code/two_arrays_output1.txt'

   def test_two_arrays_know_values(self):
       input_path = self.input_file
       result = two_arrays.two_arrays(input_path)
       with open(self.output_file) as output:
           self.assertEqual(output.read(), result)

if __name__ == '__main__':
   unittest.main()
