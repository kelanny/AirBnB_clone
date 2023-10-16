import unittest
from models.state import State

class TestStateModel(unittest.TestCase):
    def test_state_inherits_from_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_default_name(self):
        state = State()
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()

