from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.TostStatus import TostStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TostStatus(self.driver)

    def setUp(self):
        self.driver.find_element_by_link_text("All Courses").click()

    @pytest.mark.run(order=1)
    @data(*getCSVData('/Users/Mari/PycharmProjects/letskodeit/testdata.csv'))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccZip):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=ccZip)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")

