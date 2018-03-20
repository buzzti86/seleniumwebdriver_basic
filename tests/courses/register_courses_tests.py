from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import Status
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)


    @pytest.mark.run(order=1)
    @data(("JavaScript"), ("Python 3"))
    #@unpack only needed for tupels in @data
    def test_invalidEnrollment(self, courseName):

        self.courses.enterCourse(courseName)
        result = self.courses.verifyUseAnotherShown()
        self.ts.markFinal("test_CreditCardOptionShown", result, "Credit Card Window verification")
        self.courses.allCourses()