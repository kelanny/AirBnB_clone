import unittest
from models.review import Review

class TestReviewModel(unittest.TestCase):
    def test_review_inherits_from_base_model(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_default_place_id(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_review_default_user_id(self):
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_review_default_text(self):
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
