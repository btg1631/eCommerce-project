from gatheringdatas import get_data

data_dict ={
    # 'bread_1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000554515588&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%9A%B0%EC%9C%A0%EC%8B%9D%EB%B9%B5&srchPgNo=1&src_area=ssglist'
    # ,'bread_2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000295016111&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%B0%EC%9C%A0%EC%8B%9D%EB%B9%B5&srchPgNo=1&src_area=ssglist'
    # ,'bread_3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000005273664&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%B0%EC%9C%A0%EC%8B%9D%EB%B9%B5&srchPgNo=1&src_area=ssglist'
    # ,'bread_4' : 'https://www.ssg.com/item/itemView.ssg?itemId=2097001137963&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%B0%EC%9C%A0%EC%8B%9D%EB%B9%B5&srchPgNo=1&src_area=ssglist'
    #'water_1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000015330775&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%AC%BC%20500&srchPgNo=1&src_area=ssglist'
    # ,'water_2' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000007021910&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%AC%BC%20500&srchPgNo=1&src_area=ssglist'
    # ,'water_3' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000010034011&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%AC%BC&srchPgNo=1&src_area=ssglist&advertBidId=1006501887&advertExtensTeryDivCd=10'
    # ,'yogurt_1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000028430818&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%94%EA%B1%B0%ED%8A%B8%20450g&srchPgNo=1&src_area=ssglist'
    # ,'yogurt_2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000344353935&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%9A%94%EA%B1%B0%ED%8A%B8%20450g&srchPgNo=1&src_area=ssglist'
    # ,'yogurt_3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000541620861&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%94%EA%B1%B0%ED%8A%B8%20450g&srchPgNo=1&src_area=ssglist'
    # ,'cheese_1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000060094510&siteNo=6001&salestrNo=2037'
    # ,'cheese_2' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006822795&siteNo=6001&salestrNo=2037'
    # ,'cheese_3' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000007334695&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%B2%B4%EB%8B%A4%EC%B9%98%EC%A6%88&srchPgNo=1&src_area=ssglist'
    # ,'milk_1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000525619966&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%B0%EC%9C%A0%201l&srchPgNo=1&src_area=ssglist'
    #,'milk_2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000277628967&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%9A%B0%EC%9C%A0%201l&srchPgNo=1&src_area=ssglist'
    'milk_3' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006615475&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%9A%B0%EC%9C%A0%201000ml&srchPgNo=1&src_area=ssglist'
}

for k,v in data_dict.items():
    get_data(k,v)
    pass