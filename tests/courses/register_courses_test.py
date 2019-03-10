from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.login_page import LoginPage
from utilities.TostStatus import TostStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        # self.ts = TostStatus(self.driver)
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.lp.login("test@email.com", "abcabc")
        self.rc.enrollCourse("JavaScript", "9879 5435 1321 2132", "10/25", "125", "Albania", "1231654")
        self.rc.verifyEnrollFailed()





