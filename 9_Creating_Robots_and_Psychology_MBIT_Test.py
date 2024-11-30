from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # for expilicit waiting time
from selenium.webdriver.support.ui import Select   # for choosing drop-down Lists

print("***Creating_Robots_and_Psychology_Test:**** :", "\n")
"site_psychology_test: https://esanj.ir/"

# MBIT Test Page:
url = "https://esanj.ir/category/personality-tests"
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(url)
# driver.maximize_window()

# To prevent repetition WebDriverWait:
waits = WebDriverWait(driver,20)

# go to "تست هاي روان شناختي"part:
"""<h2 class="dv-test-card-title">تست شخصیت شناسی MBTI </h2>"""
MBTI = waits.until(EC.element_to_be_clickable((By.LINK_TEXT, "تست شخصیت شناسی MBTI"))).click()


# کلیک روی دکمه شروع آزمون بر اساس Copy CSS Selector
# start_exam_button_selector = "#view-exam-ctn > div > div.col-12.col-lg-3.mb-3.mt-3.mt-md-0 > div > div > div.d-flex.flex-column.justify-content-between.align-items-center.w-100.h-100 > a.dv-start-exam-btn.mb-4.exam-start-btn"
# start_exam_button = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, start_exam_button_selector)))
# start_exam_button.click()
# driver.implicitly_wait(10)

# کلیک روی دکمه شروع آزمون بر اساس Copy Xpath
start_exam_button_Xpath = '//*[@id="view-exam-ctn"]/div/div[4]/div/div/div[2]/a[1]'
start_exam_button = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, start_exam_button_Xpath))).click()
# driver.implicitly_wait(10)

# مكان يابي ليست كشويي جنسيت :
free_interpretation_Xpath = '//*[@id="free-card"]/center[2]'
free_interpretation = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, free_interpretation_Xpath))).click()


"""**Drop Down Lists**"""

# انتخاب ليست كشويي جنسيت:
"""<span class="select2-selection__rendered" id="select2-gender-container" role="textbox" aria-readonly="true" title="جنسیت"><span class="select2-selection__placeholder">جنسیت</span></span>"""
Genist_My_CSS_Selector = "//span[@id='select2-gender-container']/span[@class='select2-selection__placeholder']"
Genist = waits.until(EC.element_to_be_clickable(By.XPATH, Genist_My_CSS_Selector)).click()

# انتخاب مرد يا زن در ليست كشويي:
drop_Genist = Select(Genist)
"""<li class="select2-results__option select2-results__option--selectable select2-results__option--selected" id="select2-gender-result-vor4-مرد" role="option" data-select2-id="select2-data-select2-gender-result-vor4-مرد" aria-selected="false">مرد</li>"""
drop_Genist_My_CSS_Selector = "//li[@id='select2-gender-result-vor4-مرد']"
drop_Genist.until(EC.element_to_be_clickable(By.XPATH, Genist_My_CSS_Selector)).click()

# انتخاب ليست كشويي سال تولد:
"""<span class="select2-selection__placeholder">سال تولد</span>"""
Age_dropdown_My_CSS_Selector = "//span[@class='select2-selection__placeholder' and text()='سال تولد']"
Age = waits.until(EC.element_to_be_clickable(By.XPATH, Age_dropdown_My_CSS_Selector)).click()
drop_Age = Select(Age)



# وارد کردن سال تولد در کادر جستجوی لیست کشویی
year = "1359"  # یا هر سال دیگری که کاربر وارد می‌کند

Number_Age_selector = "//input[@class='select2-search__field' and @role='searchbox']"
Age_search_box = waits.until(EC.visibility_of_element_located((By.XPATH, Number_Age_selector)))
Age_search_box.send_keys(year)  # سال تولد مورد نظر را وارد کنید

# ساختن XPath به صورت پویا بر اساس سال وارد شده
year_option_xpath = f"//li[contains(@class, 'select2-results__option') and text()='{year}']"
year_option = waits.until(EC.element_to_be_clickable((By.XPATH, year_option_xpath))).click()

# كليك روي دكمه شروع آزمون:
"""<button class="dv-start-form-button w-100">شروع آزمون رایگان</button>"""
Start_Button_Test_My_CSS_Selector = "//[class='dv-start-form-button w-100']"
Start_Button = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Start_Button_Test_My_CSS_Selector ))).click()

# از طريق حلقه به هر سوال، پاسخ صحيح را يك بار اولي و يا بار دومي ميگيريم
i=1
while i <= 10 :
    if i % 2 == 0:
        answer_test_even = waits.until(EC.element_to_be_clickable((By.XPATH, "//lable[@for = 'answer-1' ]"))).click()
    elif i % 2 != 0:
        answer_test_odd = waits.until(EC.element_to_be_clickable((By.XPATH, "//lable[@for = 'answer-2' ]"))).click()
    i += 1


















"""***اگر خواستيم جز به جز وارد سايت شويم:***"""

# url = "https://google.com/"
# # driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.get(url)
# # driver.maximize_window()

# # To prevent repetition WebDriverWait:
# waits = WebDriverWait(driver,20)

# # find search box and write our text for search in search box:
# google_searchbox = waits.until(EC.element_to_be_clickable((By.NAME,"q")))
# #write our text for search in search box
# google_searchbox.send_keys('تست روانشناسي'+Keys.ENTER)

# # enter to the site:
# """<a jsname="UWckNb" href="https://esanj.ir/" data-ved="2ahUKEwjZhs3Yt8KJAxW2_7sIHdO5CB4QFnoECBkQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://esanj.ir/&amp;ved=2ahUKEwjZhs3Yt8KJAxW2_7sIHdO5CB4QFnoECBkQAQ"><br><h3 class="LC20lb MBeuO DKV0Md"><span dir="rtl">ای سنج: سامانه تست های روانشناسی (ارزیابی آنلاین)</span></h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="H9lube"><div class="eqA2re NjwKYd Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAdCAMAAAD8QJ61AAAASFBMVEVHcExnkoh/gYCAgICAgICBf4CAgICAgICBf4CAgICAgICAgIB+gYAmvJ0suZspu5wovJwpu5xPppEovJxukYdjmYsqupsmuZwHhoqqAAAAGHRSTlMAFWosmNf/gKxG8MFZaov/7KpxzJdLRywgIOC1AAABWklEQVR4AXWSh5bFEBBApzBqhGdX/v9PV2J5/erc4ygDTyARMXyFlRajxbovy9aLCIVehQhvOCtemUsIRosmfF4O4g2DuwS7pV5r87judYROHELac7kFUbAg4dFOoZO0hoWS0RrxS6jBr2Ng0FOQGCQM4ce7KbAP70K+CS1BzBR8F/RtP7ndT0ni5lkehE0CrjPym3Bdg2HgNS7BLaEqmadce9lL8L+p1JwzCc0zKmRHxgZ/CaKtMhSbEzvPvhjCwg8hyANPwnxgdWIuCN3oqBOLcOfY4JlIYB6FVuAJI5Y9/y+VkhDSAUeDdmBCssjiYApbLbki7A1SxbrhftgAUaxxQ+i0XGEKqQshAAfv3YyIkste6t7r/cz5ILGkvMF/oeW0bSW1VHrTcznAaB8IWA8h5VThBYYHjr2mraGj34ZAriFGJhed6+P5BDUXijE2jI4P7j1m7r1T+APhVRTfmg5ZKgAAAABJRU5ErkJggg==" style="height:18px;width:18px" alt="" data-csiid="W50oZ5ntFbb_7_UP0_Oi8AE_2" data-atf="1"></div></span><div class="CA5RN"><div><span class="VuuXrf"><span dir="rtl">ای سنج</span></span></div><div class="byrV5b"><cite class="tjvcx GvPZzd dTxz9 cHaqb" role="text">https://esanj.ir</cite></div></div></div></div><span jscontroller="IX53Tb" jsaction="rcuQ6b:npT2md" style="display:none"></span></a>"""
# copy_selector = """#rso > div:nth-child(1) > div > div > div > div.kb0PBd.A9Y9g.jGGQ5e > div > div > span > a"""
# my_own_selector_esanj = "a[href='https://esanj.ir/']"
# esnanj_site = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR,my_own_selector_esanj))).click()

# # Login to the site:
# phone_input_selector = ".dv-login-button"
# phone_number = "09123456789"

# phone_input = waits.until(EC.visibility_of_element_located((By.CSS_SELECTOR, phone_input_selector)))
# phone_input.send_keys(phone_number)

# # کلیک روی دکمه ورود
# login_button_selector = "button.dv-login-from-btn.dv-welcome-btn"  # کلاس‌های دکمه ورود
# login_button = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_button_selector)))
# login_button.click() # وارد كردن توكن ورودي

# # go to "تست هاي روان شناختي"part:
# """<a href="https://esanj.ir/category/personality-tests" class="dv-exam-category-parent  ms-3 ms-md-0 mb-md-3 h-100">..."""
# my_own_selector2 = "a[href='https://esanj.ir/category/personality-tests']"
# MBTI_Page = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, my_own_selector2))).click()

# Xpath_char = '/html/body/main/div[3]/div/div[4]/div/a[1]'
# MBTI_Page = driver.find_element(By.XPATH, Xpath_char)
# MBTI_Page.click()