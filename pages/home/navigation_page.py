import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = "//a[@class='navbar-brand header-logo']"
    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_settings_icon = "//img[@class='gravatar']"


    def navigateToAllCourses(self):
        self.elementClick(locator=self._logo, locatorType="xpath")
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._logo, locatorType="xpath")
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToAllPractice(self):
        self.elementClick(locator=self._logo, locatorType="xpath")
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSetting(self):
        self.elementClick(locator=self._logo, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)



