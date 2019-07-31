import unittest
import app

# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_if_it_runs_to_the_end(self):
    # self.assertEqual(app.testing_address(["California", "Nevada", "Illinois", "New York", "Maine"],["Nevada", "Illinois", "New York", "Maine"]), True)
    # self.assertEqual(app.testing_address(['seattle', 'chicago', 'anaheim', 'miami'], ['chicago', 'anaheim', 'miami']), True)
    # self.assertEqual(app.testing_address(['san diego', 'anaheim', 'costa mesa', 'seattle'], ['anaheim', 'costa mesa', 'seattle']), True) #bad apple
    self.assertEqual(app.testing_address(['anaheim', 'buena park', 'cypress', 'fullerton'], ['buena park', 'cypress', 'fullerton']), True) #bad apple
    self.assertEqual(app.testing_address(["California", "Nevada", "Illinois", "New York", "Washington", "Maine"], ["Nevada", "Illinois", "New York", "Washington", "Maine"]), True) #bad apple
    self.assertEqual(app.testing_address(["California", "Montana", "Wyoming", "Idaho", "Texas", "Florida", "Maine"], ["Montana", "Wyoming", "Idaho", "Texas", "Florida", "Maine"]), True)

if __name__ == '__main__':
    unittest.main()