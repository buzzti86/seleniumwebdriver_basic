import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"
    _submit_search = "search-course-button"
    _course = "//div[contains(text(),'JavaScript for beginners')]"
    _all_courses = ""
    _enroll_button = "enroll-button-top"
    _use_another = "//button[contains(text(),'Use another card')]"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = ""
    _cc_cvv = ""
    _submit_enroll = ""
    _enroll_error_message =  ""

    def enterCourse(self, name):
        self.selectCourseToEnroll(name)
        searchedCourse = "//div[contains(text(),'" + name + "')]"
        self.elementClick(searchedCourse, "xpath")
        self.elementClick(self._enroll_button)


    def selectCourseToEnroll(self, fullCourseName):
        self.sendKeys(fullCourseName, self._search_box)
        self.elementClick(self._submit_search)

    def enterCardNum(self, num):
        self.sendKeys(num,self._cc_num, "xpath")

    def enterCardExp(self, exp):
        print()

    def enterCardCVV(self, cvv):
        print()

    def clickEnrollSubmitButton(self):
        print()

    def enterCreditCardInformation(self, num, exp, cvv):
        print()
        #call all three enter methods

    def enrollCourse(self, num="", exp="", cvv=""):
        self.webScroll("down")
        self.elementClick(self._use_another, "xpath")

    def allCourses(self):
        self.getUrl("https://letskodeit.teachable.com/courses")

    def verifyUseAnotherShown(self):
        result = self.isElementPresent(self._use_another,
                                       locatorType="xpath")
        return result