from selenium import webdriver  # selenium 의 webdriver 를 사용 하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time     # 페이지 로딩을 기다리는 데에 사용할 time 모듈 import

print('1. 카운터픽 검색')
print('2. 전적 검색')
print('3. 종료')
selectMenu=input('메뉴 선택 (1,2,3) : ')

if selectMenu==1:
    query_txt = input('상대 챔피언을 입력하세요 :')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://lol.ps/')  # 크롬 드라이버에 url 주소 넣고 실행
    time.sleep(1) # 로딩 기다리기

    search_box = driver.find_element(By.XPATH, r'//*[@id="default-search"]')   # 검색창의 html 상의 이름
    search_box.click() # 검색창 클릭
    search_box.send_keys(query_txt + Keys.ENTER) # 챔피언 검색창에 입력하고 엔터 입력
    time.sleep(1) # 로딩 기다리기

    counterpick1_xpath = driver.find_element(By.XPATH, r'//*[@id="content-container"]/div[1]/section[3]/div/div[1]/div/a[1]')
    counterpick1 = counterpick1_xpath.text # 카운터픽 1위의 이름,게임수,승률을 counterpick1에 저장
    counterpick2_xpath = driver.find_element(By.XPATH, r'//*[@id="content-container"]/div[1]/section[3]/div/div[1]/div/a[2]')
    counterpick2 = counterpick2_xpath.text # 카운터픽 2위의 이름,게임수,승률을 counterpick1에 저장
    counterpick3_xpath = driver.find_element(By.XPATH, r'//*[@id="content-container"]/div[1]/section[3]/div/div[1]/div/a[3]')
    counterpick3 = counterpick3_xpath.text # 카운터픽 3위의 이름,게임수,승률을 counterpick1에 저장

    print('---------------------------------------')
    print(query_txt + '을(를) 상대하기 쉬운 챔피언은')
    print('1. '+counterpick1)
    print('2. '+counterpick2)
    print('3. '+counterpick3+" 입니다. ")
    print('---------------------------------------')

elif selectMenu==2:
    query_txt = input('닉네임을 입력하세요 :')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://lol.ps/')  # 크롬 드라이버에 url 주소 넣고 실행
    time.sleep(1) # 로딩 기다리기

    search_box = driver.find_element(By.XPATH, r'//*[@id="default-search"]')   # 검색창의 html 상의 이름
    search_box.click() # 검색창 클릭
    search_box.send_keys(query_txt + Keys.ENTER) # 챔피언 검색창에 입력하고 엔터 입력
    time.sleep(1) # 로딩 기다리기

    myScore1_xpath= driver.find_element(By.XPATH, r'//*[@id="capture"]/div[2]')
    myScore1=myScore1_xpath.text
    print(myScore1)

#elif selectMenu==3: