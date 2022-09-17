"""test_city Module."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Defines tests for the methods in City."""

    def setUp(self):
        """Create some City objects for testing purposes."""
        self.c1 = City()

    def test_init(self):
        """Test that a new object is initialized correctly."""
        # check City is subclass of BaseModel
        self.assertTrue(issubclass(City, BaseModel))

        self.assertIsInstance(self.c1, City)

        # test that a newly created object has the correct attributes
        attrs = {
            "name": str,
            "state_id": str
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.c1, a_name))
            self.assertIsInstance(getattr(self.c1, a_name, None), a_type)