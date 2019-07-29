import unittest
import app

# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_if_it_runs_to_the_end(self):
    self.assertEqual(app.unittest(["California", "Nevada", "Illinois", "New York", "Maine"],["Nevada", "Illinois", "New York", "Maine"]), True)
    # self.assertEqual(app.unittest(['seattle', 'chicago', 'anaheim', 'miami'],['chicago', 'anaheim', 'miami']), True)
    # self.assertEqual(app.unittest(['san diego', 'anaheim', 'costa mesa', 'seattle'],['anaheim', 'costa mesa', 'seattle']), True)
    # self.assertEqual(app.unittest(['anaheim', 'buena park', 'cypress', 'fullerton'],['buena park', 'cypress', 'fullerton']), True)

if __name__ == '__main__':
    unittest.main()
