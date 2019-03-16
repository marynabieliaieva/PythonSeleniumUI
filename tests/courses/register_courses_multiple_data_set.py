from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.TostStatus import TostStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TostStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "1220", "444", "12345"),
          ("Learn Python 3 from scratch", "3334 5678 9012 3456", "1320", "555", "54321"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccZip):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=ccZip)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        self.driver.find_element_by_link_text("All Courses").click()
