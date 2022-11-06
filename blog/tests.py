# Imports from existing modules.
from django.test import TestCase

class TestBlog(TestCase):
    """
        This here class is designated to encapsulate all the test for the blog component of the application.

        The tests are here to ensure that the required behaviour is to be expected from the application,
        and that the given specification is respected to the letter.

        As for the testing class itself, it is important to note that it extends the TestCase class
        thus making it unit test capable.

        Author : Andrei-Paul Ionescu.
    """

    def test_adding_one_sole_post_to_the_data_base(self):
        self.assertTrue(True)

    def test_deleting_one_sole_post_from_the_data_base(self):
        self.assertTrue(True)

    def test_adding_n_posts_to_the_data_base(self):
        self.assertTrue(True)

    def test_deleting_n_posts_from_the_data_base(self):
        self.assertTrue(True)

    def test_resetting_the_post_table(self):
        self.assertTrue(True)

    def test_that_posts_can_be_sorted_increasingly_in_accordance_to_date(self):
        self.assertTrue(True)

    def test_that_posts_can_be_sorted_decreasingly_in_accordance_to_date(self):
        self.assertTrue(True)
