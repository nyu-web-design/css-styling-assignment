"""
Tests for CSS styles across a few pages.

Selenium webdriver for Chrome (a.k.a. the file named chromedriver) must be installed in either:
- in the same directory as chrome.exe on Windows (e.g. C:\Program Files\Google\Chrome\Application)
- in a directory that is included in the PATH on Mac OS X (e.g. /usr/local/bin)
"""

import pytest
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Tests:

  @pytest.fixture(scope="class")
  def settings(self):
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class", )
  def driver(self, settings):
    """
    Pop open a web browser and make it available to the tests.
    """

    # set up the fixture
    driver = webdriver.Chrome()
    driver.get(settings["site_url"]) # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_global_p_styles(self, driver, settings):
    """
    Check that paragraphs across all pages have non-default styles.
    """
    pages = ['about_me.html', 'more_about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      elems = driver.find_elements_by_tag_name("p")
      for elem in elems:
        # check for non-default-font
        assert elem.value_of_css_property('font-family') != 'Times'

  def test_global_h_styles(self, driver, settings):
    """
    Check that headings h1, h2, and h3 across all pages have non-default styles.
    """
    pages = ['about_me.html', 'more_about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      elems = driver.find_elements_by_css_selector("h1, h2, h3")
      for elem in elems:
        # check for non-default-font
        assert elem.value_of_css_property('font-family') != 'Times'

  def test_global_a_styles(self, driver, settings):
    """
    Check that links across all pages have non-default styles for their various states.
    """
    pages = ['index.html', 'about_me.html', 'more_about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      elems = driver.find_elements_by_tag_name("a")
      for elem in elems:
        # check default colors
        default_text_color = elem.value_of_css_property('color')
        default_bg_color = elem.value_of_css_property('background-color')
        # check hover colors
        ActionChains(driver).move_to_element(elem).pause(0).perform()  # move cursor there
        hover_text_color = elem.value_of_css_property('color')
        hover_bg_color = elem.value_of_css_property('background-color')
        # check for non-default-font
        assert (default_bg_color != hover_bg_color) or (default_text_color != hover_text_color)
        
  def test_section_padding_styles(self, driver, settings):
    """
    Check that sections have padding on all sides.
    """
    pages = ['about_me.html', 'more_about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      elems = driver.find_elements_by_css_selector("section")
      for elem in elems:
        # check for non-default-font
        padding = elem.value_of_css_property('padding')
        assert padding and padding != ''

  def test_section_margin_styles(self, driver, settings):
    """
    Check that sections have bottom margins.
    """
    pages = ['about_me.html', 'more_about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      elems = driver.find_elements_by_css_selector("section")
      for elem in elems:
        # check for non-default-font
        margin = elem.value_of_css_property('margin-bottom')
        assert margin and margin != ''

  def test_section_border_styles(self, driver, settings):
    """
    Check that sections have some kind of borders.
    """
    pages = ['about_me.html', 'more_about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      elems = driver.find_elements_by_css_selector("section")
      for elem in elems:
        # check for non-default-font
        bt = elem.value_of_css_property('border-top')
        bb = elem.value_of_css_property('border-bottom')
        bl = elem.value_of_css_property('border-left')
        br = elem.value_of_css_property('border-right')
        ba = elem.value_of_css_property('border')
        assert (bt or bb or bl or br or ba) and (bt != '' or bb != '' or bl != '' or br != '' or ba != '')

  def test_section_ids(self, driver, settings):
    """
    Check that the two required sections have ids
    """
    pages = ['about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      # look for the ids on each required section
      elem1 = driver.find_element_by_css_selector("section#my_background")
      elem2 = driver.find_element_by_css_selector("section#my_interests")
      assert elem1 and elem2

  def test_section_backgrounds(self, driver, settings):
    """
    Check that sections have background colors or background-images.
    """
    pages = ['about_me.html']
    for page in pages:
      # check each page individually
      url = "{}/{}".format(settings["site_url"], page)
      driver.get(url)
      # look for the background settings of each of the two required sections
      elem1 = driver.find_element_by_css_selector("section#my_background")
      elem1bgimg = elem1.value_of_css_property('background-image')
      elem1bgcolor = elem1.value_of_css_property('background-color')
      assert elem1 and (elem1bgimg != '' or elem1bgcolor != '')

      elem2 = driver.find_element_by_css_selector("section#my_interests")
      elem2bgimg = elem2.value_of_css_property('background-image')
      elem2bgcolor = elem2.value_of_css_property('background-color')
      assert elem2 and (elem2bgimg != '' or elem2bgcolor != '')

