from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # For explicit waiting time
from selenium.webdriver.support.ui import Select  # For handling drop-down lists

print("***Creating_Robots_and_Psychology_Test:****", "\n")
# Website for the psychology test: https://esanj.ir/

# MBTI Test Page
url = "https://esanj.ir/category/personality-tests"
driver = webdriver.Chrome()
driver.get(url)
# driver.maximize_window()

# Avoid repetition by using WebDriverWait
waits = WebDriverWait(driver, 20)

# Navigate to the "Personality Tests" section
"""<h2 class="dv-test-card-title">تست شخصیت شناسی MBTI</h2>"""
MBTI = waits.until(EC.element_to_be_clickable((By.LINK_TEXT, "تست شخصیت شناسی MBTI"))).click()

# Click the "Start Test" button using the copied CSS Selector
# start_exam_button_selector = "#view-exam-ctn > div > div.col-12.col-lg-3.mb-3.mt-3.mt-md-0 > div > div > div.d-flex.flex-column.justify-content-between.align-items-center.w-100.h-100 > a.dv-start-exam-btn.mb-4.exam-start-btn"
# start_exam_button = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, start_exam_button_selector)))
# start_exam_button.click()
# driver.implicitly_wait(10)

# Click the "Start Test" button using the copied XPath
start_exam_button_Xpath = '//*[@id="view-exam-ctn"]/div/div[4]/div/div/div[2]/a[1]'
start_exam_button = waits.until(EC.element_to_be_clickable((By.XPATH, start_exam_button_Xpath))).click()
# driver.implicitly_wait(10)

# Locate the free interpretation section
free_interpretation_Xpath = '//*[@id="free-card"]/center[2]'
free_interpretation = waits.until(EC.element_to_be_clickable((By.XPATH, free_interpretation_Xpath))).click()

"""**Drop-Down Lists**"""

# Select the gender drop-down list
"""<span class="select2-selection__rendered" id="select2-gender-container" role="textbox" aria-readonly="true" title="جنسیت"><span class="select2-selection__placeholder">جنسیت</span></span>"""
Gender_CSS_Selector = "//span[@id='select2-gender-container']/span[@class='select2-selection__placeholder']"
Gender = waits.until(EC.element_to_be_clickable((By.XPATH, Gender_CSS_Selector))).click()

# Select male or female in the drop-down list
"""<li class="select2-results__option select2-results__option--selectable select2-results__option--selected" id="select2-gender-result-vor4-مرد" role="option" data-select2-id="select2-data-select2-gender-result-vor4-مرد" aria-selected="false">مرد</li>"""
Gender_Option_XPath = "//li[@id='select2-gender-result-vor4-مرد']"
waits.until(EC.element_to_be_clickable((By.XPATH, Gender_Option_XPath))).click()

# Select the birth year drop-down list
"""<span class="select2-selection__placeholder">سال تولد</span>"""
BirthYear_CSS_Selector = "//span[@class='select2-selection__placeholder' and text()='سال تولد']"
BirthYear = waits.until(EC.element_to_be_clickable((By.XPATH, BirthYear_CSS_Selector))).click()

# Enter the birth year into the search box within the drop-down list
year = "1983"  # Example year input
Year_Input_XPath = "//input[@class='select2-search__field' and @role='searchbox']"
Year_Search_Box = waits.until(EC.visibility_of_element_located((By.XPATH, Year_Input_XPath)))
Year_Search_Box.send_keys(year)  # Input the desired birth year

# Build a dynamic XPath based on the entered year and select it
Year_Option_XPath = f"//li[contains(@class, 'select2-results__option') and text()='{year}']"
waits.until(EC.element_to_be_clickable((By.XPATH, Year_Option_XPath))).click()

# Click the "Start Free Test" button
"""<button class="dv-start-form-button w-100">شروع آزمون رایگان</button>"""
Start_Test_Button_CSS = "//button[@class='dv-start-form-button w-100']"
waits.until(EC.element_to_be_clickable((By.XPATH, Start_Test_Button_CSS))).click()

# Use a loop to answer questions alternatively
i = 1
while i <= 10:
    if i % 2 == 0:
        answer_even = waits.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='answer-1']"))).click()
    else:
        answer_odd = waits.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='answer-2']"))).click()
    i += 1
