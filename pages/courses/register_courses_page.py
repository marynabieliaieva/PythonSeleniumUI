import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"
    _search_button = "search-course-button"
    _course = "course-listing-title"
    _all_courses = ""
    _enroll_button = "enroll-button-top"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _cc_country = "country_code_credit_card-cc"
    _cc_postal_code = "postal"
    _cc_agreeded = "agreed_to_terms_checkbox"
    _submit_enroll = "confirm-purchase"
    _successfull_message = "message"



    # card number = 9879 5435 1321 2132
    # date = 10/25
    # cvc = 125
    # country = albania
    # postal code = 1231654


    def enterCourseToEnroll(self, fullCourseName):
        self.clear(self._search_box)
        self.sendKeys(fullCourseName, self._search_box)
        self.elementClick(self._search_button)

    def clickToFindedCourse(self):
        self.elementClick(self._course, locatorType="class")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button)

    def enterCardNum(self, num):
        self.clear(self._cc_num)
        self.sendKeys(num, self._cc_num, locatorType="name")

    def enterCardExp(self, exp):
        self.clear(self._cc_exp)
        self.sendKeys(exp, self._cc_exp, locatorType="name")

    def enterCardCVV(self, cvv):
        self.clear(self._cc_cvv)
        self.sendKeys(cvv, self._cc_cvv, locatorType="name")

    def selectCardCountry(self, country):
         self.select(country, self._cc_country)

    def enterCardPostalCode(self, postalCode):
        self.clear(self._cc_postal_code)
        self.sendKeys(postalCode, self._cc_postal_code, locatorType="name")

    def clickAgreemetnCheckBox(self):
        self.elementClick(self._cc_agreeded)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll)

    def enterCreditCardInformation(self, num, exp, cvv, country, postalCode):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.selectCardCountry(country)
        self.enterCardPostalCode(postalCode)
        self.clickAgreemetnCheckBox()
        self.clickEnrollSubmitButton()


    def enrollCourse(self, fullCourseName="", num="", exp="", cvv="", country="", postalCode=""):
        self.enterCourseToEnroll(fullCourseName)
        self.clickToFindedCourse()
        self.clickEnrollButton()
        self.enterCreditCardInformation(num, exp, cvv, country, postalCode)

    def verifyEnrollFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Payment is not success')]",
                                       locatorType="xpath")
        return result

