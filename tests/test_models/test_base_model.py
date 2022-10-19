"""test_base_model Module."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Defines tests for the methods in BaseModel."""

    def setUp(self):
        """Create some BaseModel objects for testing purposes."""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_init(self):
        """Test that new object attributes are initialized correctly."""
        # test that objects are instances of the class
        self.assertIsInstance(self.bm1, BaseModel)

        # test that a newly created object has the correct attributes
        attrs = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime
        }

        for a_name, a_type in attrs.items():
            self.assertTrue(hasattr(self.bm1, a_name))
            self.assertIsInstance(getattr(self.bm1, a_name, None), a_type)

        # test that id attributes of 2 differet objects are different
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_init_kwargs(self):
        """Test initialization of BaseModel object using kwargs."""
        pass

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        bm2_class_name = type(self.bm2).__name__
        bm2_id = getattr(self.bm2, "id", None)
        bm2_dict = self.bm2.__dict__

        s_bm2 = f"[{bm2_class_name}] ({bm2_id}) {bm2_dict}"

        # check that the string representation of the object is correct
        self.assertEqual(str(self.bm2), s_bm2)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        bm1_dict = self.bm1.to_dict()

        self.assertEqual(bm1_dict["__class__"], type(self.bm1).__name__)

        for attr in ["created_at", "updated_at"]:
            dt = datetime.strptime(bm1_dict[attr], '%Y-%m-%dT%H:%M:%S.%f')
            self.assertEqual(dt, getattr(self.bm1, attr, None))

    def test_save(self):
        """Test the save method of BaseModel."""
        import os

        fp = storage._FileStorage__file_path

        # remove the json file
        try:
            os.remove(fp)
        except Exception:
            pass

        self.assertFalse(os.path.exists(fp))

        dt_before = self.bm2.updated_at

        # saving should create a new file and change updated_at
        self.bm2.save()
        self.assertTrue(os.path.exists(fp))

        dt_after = self.bm2.updated_at
        self.assertNotEqual(dt_before, dt_after)

        try:
            os.remove(fp)
        except Exception:
            pass