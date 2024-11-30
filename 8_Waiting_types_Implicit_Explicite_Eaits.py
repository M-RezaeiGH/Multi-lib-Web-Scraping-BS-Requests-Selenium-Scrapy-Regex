from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # for wxpilicit waiting time
from selenium.webdriver.common.keys import Keys

print("***Waiting_types_Implicit_Explicite_Waits:**** :", "\n")

url = "https://google.com/"
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(url)
# driver.maximize_window()

# find search box and write our text for search in search box:
# google_searchbox = driver.find_element(By.NAME,"q").send_keys('python')
google_searchbox = driver.find_element(By.NAME,"q")

"***Implicit_Waiting_types_:****"
driver.implicitly_wait(10)

#write our text for search in search box
google_searchbox.send_keys('python')



# find enter key(Google search key) by Xpath:
"""<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button" tabindex="0" type="submit" data-ved="0ahUKEwj3vZrxqMKJAxVXUqQEHVygIccQ4dUDCB0">"""
Xpath_Google_search_key = "//input[@class='gNO89b']"
google_searchbox.click(Xpath_Google_search_key) 



# Define XPath for the target element
"""<a jsname="UWckNb" href="https://www.python.org/" data-ved="2ahUKEwjhoOXk2cCJAxWxRqQEHdcULvwQFnoECAsQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;opi=89978449&amp;url=https://www.python.org/&amp;ved=2ahUKEwjhoOXk2cCJAxWxRqQEHdcULvwQFnoECAsQAQ"><br><h3 class="LC20lb MBeuO DKV0Md">Welcome to Python.org</h3><div class="notranslate HGLrXd NJjxre iUh30 ojE3Fb"><div class="q0vns"><span class="DDKf1c"><div class="eqA2re UnOTSe Vwoesf" aria-hidden="true"><img class="XNo5Ab" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAjVBMVEVHcEw3apI/c5s8daJIibxDg7U/fq89eqssbqNkk7uXs8s5dqc2cqKdiDRFgrLj6O3///8tZpYOVZZAfa4zbp0waZkHQIj842n23GJJh7j+6G7/6HL/5Wr/4mL61Un/31r/3FHfuzjqxDv/52z/6Gz/2Ujrykj/1T30zT45cqDsxTj92Ej/0zL745v76baPv6cfAAAALHRSTlMAIERq/f///9b////+E43//1d7nv//aqaJxvH////X//82ScvU/1v/uLFt70uptdUAAAELSURBVHgBZdJFAoQwDEDRjDvu7g73P96kwenfPqjD2ul8wc4n4Ltcb9fb7Xa/P54cn6+v92iPz/d3QOEmSu872ecrc/gWX5N9FQ7vGBmPZ5VipmlblEcYEU03TNO0fmT2FaOF0n8MHdd1HZqNiBkhGkPP8y1E3hDR/ADgxJt+ZhaGPzjzpphkUQwyIdpTmZJNJLQoAXky2UqzMR8NKcoTOKMhGqlL0WzM8jyP4XRn9i22FpGVP4AnTWjNNFtZVuyW0Qi93W9lmQBW4yYQ97+xHyl8O7I1/lZQDRbDmkUWtqyy2QDhvIEy6nhEIuuloTtiMVnHMIFD1bSBLu8q4CqCkgoK3rBfnCTxD9b+IVgs9hMsf3IAAAAASUVORK5CYII=" style="height:26px;width:26px" alt="" data-csiid="rLQnZ-GaD7GNkdUP16m44Q8_2" data-atf="1"></div></span><div class="CA5RN"><div><span class="VuuXrf">Python.org</span></div><div class="byrV5b"><cite class="tjvcx GvPZzd cHaqb" role="text">https://www.python.org</cite></div></div></div></div><span jscontroller="IX53Tb" jsaction="rcuQ6b:npT2md" style="display:none"></span></a>"""
Xpath_char = "//a[@href='https://www.python.org/']"

"approach1: withot waiting time"
# WelcomeText_click = driver.find_element(By.XPATH, Xpath_char)
# WelcomeText_click.click()

"approach2:***with Explicit_Waiting_types_:****"
# Use WebDriverWait to wait until the element is clickable
try:
    WelcomeText_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Xpath_char))
    )
    WelcomeText_click.click()
except Exception as e:
    print("Error:", e)



driver.implicitly_wait(10)
driver.close()





