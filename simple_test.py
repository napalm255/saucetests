from selenium import webdriver
import unittest
import os


"""
Python unittest class which demonstrates creating a webdriver instance using environment variables
populated by the Sauce CI plugins.
"""

class testSauceWrappers(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {}
        desired_capabilities['browserName'] = os.environ['SELENIUM_BROWSER']
        desired_capabilities['version'] = os.getenv('SELENIUM_VERSION', '')
        desired_capabilities['platform'] = os.environ['SELENIUM_PLATFORM']
        command_executor = "http://%s:%s@%s:%s/wd/hub" % (os.environ['SAUCE_USER_NAME'], os.environ['SAUCE_API_KEY'], os.environ['SELENIUM_HOST'], os.environ['SELENIUM_PORT'])
        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=command_executor)


    def test_websites(self):
        driver = self.driver
        driver.get("http://filesync.net")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_filesync")
        driver.get("http://filesync.net/jenkins")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_filesync_jenkins")
        driver.get("http://naponline.net")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_naponline")
        driver.get("http://meaustin.com")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_meaustin")
        driver.get("http://leviathanlegacy.com")
        print "\rSauceOnDemandSessionID=%s job-name=%s" % (self.driver.session_id, "test_leviathanlegacy")
        driver.quit()


if __name__ == "__main__":
    unittest.main()
