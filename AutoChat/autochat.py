from selenium import webdriver 
import time
user=''
password=''
message = 'Ôi cái làng Dầu của tôi! Vẫn cái phong vị ngọt ngào của lúa non đồng nội. Vẫn con đường gạch đá xanh rơn. Bầu trời cao thẳm, rộng bao la, vương chút nắng xuống mái đình cổ kính. Tôi đã yêu và yêu biết nhường nào cái mảnh đất này, nơi tôi sinh ra và lớn lên. Bọn giặc đáng khinh kia đã tàn nơi đây. Làng Dầu không còn như ngày tôi phải rời làng đi tản cư nữa. Nhưng giờ trở lại, lòng tôi vẫn thế, vẫn vẹn nguyên không hề thay đổi. Trong tôi có cái gì nao nao rất lạ. Một cảm giác nhớ nhớ, xen một chút thương, pha đôi sự tự hào.'
with open('user.input','r') as fileInp:
    user = fileInp.readline().strip('\n')
    password = fileInp.readline().strip('\n')

#mở trình duyệt
driver = webdriver.Edge(executable_path="D:\File\CodePyThon\ProjectPy\AutoChat\msedgedriver.exe")
driver.get('https://www.messenger.com/')
time.sleep(2)

#nhập user và pass
try:
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[6]').send_keys(user)
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[7]').send_keys(password)
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/div[1]/button').click()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div[1]/div/a/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div').send_keys(message)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div').click()
except:
    print('Có lỗi rồi đại ca!')
