# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

     When young adolescent women subscribe to culturally determined fashion expectations, they run the risk of succumbing to pathogenic dieting methods.
     In the early part of the 21st century, the photographs, stories, and symbols reinforced through advertising, social media, television and film promote the concept of thinness.
     This trope affects a women’s medical wellbeing and can lead to pathogenic eating disorder, most notably anorexia.
     This project examines the triggers within contemporary fashion that de-stabilizes the self-perception of young adolescent women.

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn("Pathogenic Fashion",self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('model.jpg',m.get_attribute('src'))

        # We check here for the title of your home page.
        # uncomment the next lines and change the text when you set your title.
        # put your title in place of "The Title of My Home Page"

        h=self.browser.find_element_by_css_selector('h1')
        self.assertIn("Pathogenic Fashion",h.text)

        # There is an area specified around the computer keyboard.
        # the 'id' of this area is 'keyboard'

        a=self.browser.find_element_by_id('lower')
        a.click()

        h=self.browser.find_element_by_css_selector('h1')
        

if __name__=="__main__":
        unittest.main(warnings="ignore")
