def get_data(database_name,url):
    # * 웹 크롤링 동작
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    import time
    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities
    # mongodb 연결
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database[database_name]
    # - 주소 입력
    browser.get(url)
    time.sleep(2)
    # - 정보 획득
    from selenium.webdriver.common.by import By
    # 상품명
    try:   # 상품명  h2 > span > span
        element_title = browser.find_element(by=By.CSS_SELECTOR, value="h2 > span > span")
        title = element_title.text
    except:
        title = None
    # 할인가 (현재가격 - 행사 시 행사가격, 행사 아닐시 현재가격)
    try:  # 할인가  span.cdtl_new_price.notranslate > em
        element_price = browser.find_element(by=By.CSS_SELECTOR, value="span.cdtl_new_price.notranslate > em")
        price = element_price.text.replace(',','')
    except:
        price = None
    # 원가 ( 원래 가격, 행사 미진행시 Nan)
    try:   # 원가  span.cdtl_old_price > em
        element_oldprice = browser.find_element(by=By.CSS_SELECTOR, value="span.cdtl_old_price > em")
        oldprice = element_oldprice.text.replace(',','')
        oldprice = oldprice.replace('원','')
        oldprice = int(oldprice)
        event = True
    except:
        oldprice = None
        event = False
    # 리뷰 클릭
    button = browser.find_element(by=By.CSS_SELECTOR, value="div.cdtl_review_wrap > dl > dd > div > a")
    button.click()
    time.sleep(1)
    # 페이지네이션 전체 선택자
    pagination_selector = "#comment_navi_area > div > a"

    # 다음 페이지 버튼 선택자
    next_page_button_selector = ".rvw_btn_next"
    flag = False
    while True:
        try:
            for j in range(0, 10):
                try:
                    if j != 0:
                        buttons = browser.find_element(By.CSS_SELECTOR, value=f'#comment_navi_area > div > a:nth-child({j+1})')
                        
                        buttons.click()
                        time.sleep(1)
                except:
                    flag = True
                    break

                # 리뷰 전체  #item_rvw_list > li
                element_bundle_review = browser.find_elements(By.CSS_SELECTOR, value="#item_rvw_list > li")
                for i in element_bundle_review:
                    # 댓글 아이디  a > div > div.rvw_item_info > div.rvw_item_label.rvw_item_user_id
                    try:
                        element_id = i.find_element(by=By.CSS_SELECTOR, value="a > div > div.rvw_item_info > div.rvw_item_label.rvw_item_user_id")
                        id = element_id.text
                    except:
                        id = None
                    # 댓글 날짜  a > div > div.rvw_item_info > div.rvw_item_label.rvw_item_date
                    try:
                        element_date = i.find_element(by=By.CSS_SELECTOR, value="a > div > div.rvw_item_info > div.rvw_item_label.rvw_item_date")
                        date = element_date.text
                    except:
                        date = None
                    # 댓글 별점  a > div > div.rvw_item_info > div.rvw_item_label.rvw_item_rating > span
                    try:
                        element_rating = i.find_element(by=By.CSS_SELECTOR, value="a > div > div.rvw_item_info > div.rvw_item_label.rvw_item_rating > span")
                        rating = element_rating.text
                    except:
                        rating = None
                    # 댓글 내용  div.rvw_expansion_panel_head > a > div > p
                    try:
                        element_comments = i.find_element(by=By.CSS_SELECTOR, value="div.rvw_expansion_panel_head > a > div > p")
                        comments = element_comments.text
                    except:
                        comments = None
                    # MongoDB에 저장
                    collection.insert_one({"merchTitle": title, "merchPrice": int(price), "merchOld": oldprice, "merchEvent": event, "textName": id, "textDate": date, "textLevel": int(rating), "textContent": comments})
                    # print("merchTitle:{}, merchPrice:{}, merchOld:{}, merchEvent:{}".format(title, price, oldprice, event))
                    # print("textName:{}, textDate:{}, textLevel:{}, textContent:{}".format(id, date, rating, comments))

            else:
                button = browser.find_element(By.CSS_SELECTOR, value=next_page_button_selector)
                button.click()
                time.sleep(1)
            if flag:
                break
        except:
            break
    # 브라우저 종료
    browser.quit()