#coding=utf-8

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = '192.168.86.101:5555'
desired_caps['appPackage'] = 'com.cnblogandroid'
desired_caps['appActivity'] = '.MainActivity'
desired_caps['sessionOverride'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#press 'myclass' button
time.sleep(5)
driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/\
	android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/\
	android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup[1]/\
	android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()

#press '山东理工大学' button
time.sleep(5)
driver.find_element_by_xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

#press the 'all homework' button
time.sleep(5)
driver.find_element_by_xpath('//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()

#press 'New Homework' button
time.sleep(5)
driver.find_element_by_xpath('//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()

#fill the 'homework title' box
time.sleep(5)
homeworkTitleBox = driver.find_element_by_xpath("//android.widget.EditText[@content-desc='HomeworkPost_homeworkTitle']")
homeworkTitleBox.send_keys('auto test homework 1')

#fill the content box 
time.sleep(5)
contentBox = driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/\
	android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.EditText[2]')
contentBox.send_keys('auto test add homework 20171107')

#press the 'post' button
time.sleep(5)
driver.find_element_by_xpath('//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]').click()