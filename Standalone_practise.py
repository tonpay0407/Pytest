'''Selenium practise commands'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Study\\Drivers\\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
'''
#Selecting radio button
driver.find_element_by_css_selector("input[value='radio2']").click()
driver.implicitly_wait(10)
#Selecting Suggestion box
driver.find_element_by_xpath("//input[@type='text']").send_keys('Ind')
names = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/div")
for i in names:
    if i.text == 'India':
        i.click()
#Selecting value from dropdown
sel = Select(driver.find_element_by_id('dropdown-class-example'))
sel.select_by_visible_text('Option2')
driver.implicitly_wait(5)
#selecting value from checkbox
driver.find_element_by_xpath("//input[@id='checkBoxOption3']").click()
#moving focus to a new window
driver.find_element_by_xpath("//button[@id='openwindow']").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(10)
#driver.switch_to.window(driver.window_handles[0])
#print(driver.title)

#movig focus to new tab

driver.find_element_by_xpath("//a[@id='opentab']").click()
driver.implicitly_wait(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

#handeling alerts

driver.find_element_by_css_selector("input[id='name']").send_keys('Ragul')
driver.find_element_by_css_selector("input[value='Alert']").click()
alert = driver.switch_to.alert
assert 'Ragul' in alert.text
alert.accept()
'''
#handeling webtable
#getting total number of rows
rows = driver.find_elements_by_xpath("//div[@class='tableFixHead']/table/tbody/tr")
print(len(rows))


#getting total number of columns
columns = driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr/td")
print(len(columns))

#getting headers
headers = driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr[1]/th")
for name in headers:
    print(name.text)

#Getting all values from table
columns_in_row = driver.find_elements_by_xpath("//table[@name='courses']/tbody/tr[2]/td")
for i in range(2,len(rows)+1):
    for j in range(1,len(columns_in_row)):
        d = driver.find_element_by_xpath("//table[@name='courses']/tbody/tr["+str(i)+"]/td["+str(j)+"]")
        print(d.text)


new_cols = driver.find_elements_by_xpath("//div[@class='tableFixHead']/table/tbody/tr[1]/td")
for i in new_cols:
    print(i.text)

#Mouse hover and action chains:

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//button[@id='mousehover']")).perform()
action.move_to_element(driver.find_element_by_link_text("Top")).click().perform()






