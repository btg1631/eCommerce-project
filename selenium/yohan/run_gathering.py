from gathering import get_data

data_dict ={
    'bibim1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000273953360&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%B9%84%EB%B9%94%EB%A9%B4&srchPgNo=1&src_area=ssglist'
    ,'bibim2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000062563614&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%B9%84%EB%B9%94%EB%A9%B4&srchPgNo=1&src_area=ssglist'
    ,'bibim3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000042393832&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%B9%84%EB%B9%94%EB%A9%B4&srchPgNo=1&src_area=ssglist'
    ,'bibim4' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000026240262&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%B9%84%EB%B9%94%EB%A9%B4&srchPgNo=1&src_area=ssglist'
    ,'kyoja1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000025935885&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%A7%8C%EB%91%90&srchPgNo=1&src_area=ssglist'
    ,'kyoja2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000171317834&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%A7%8C%EB%91%90&srchPgNo=1&src_area=ssglist'
    ,'kyoja3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000045103442&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%A7%8C%EB%91%90&srchPgNo=1&src_area=ssglist'
    ,'kyoja4' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000022238876&siteNo=6001&salestrNo=2037&tlidSrchWd=%EB%A7%8C%EB%91%90&srchPgNo=2&src_area=ssglist'
    ,'tomato1' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006609807&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%86%A0%EB%A7%88%ED%86%A0%EC%86%8C%EC%8A%A4&srchPgNo=1&src_area=ssglist'
    ,'tomato2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000005893792&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%86%A0%EB%A7%88%ED%86%A0%EC%86%8C%EC%8A%A4&srchPgNo=1&src_area=ssglist'
    ,'tomato3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000074165963&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%86%A0%EB%A7%88%ED%86%A0%EC%86%8C%EC%8A%A4&srchPgNo=1&src_area=ssglist'
    ,'ham1' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006609258&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%8A%A4%ED%8C%B8&srchPgNo=1&src_area=ssglist'
    ,'ham2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000542161293&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%96%84%20200&srchPgNo=1&src_area=ssglist'
    ,'ham3' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000007165734&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%96%84%20200&srchPgNo=1&src_area=ssglist'
    ,'ham4' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000090095996&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%96%84%20200&srchPgNo=1&src_area=ssglist'
    ,'ham5' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000059351609&siteNo=6001&salestrNo=2037&tlidSrchWd=%ED%96%84%20200&srchPgNo=1&src_area=ssglist'
    ,'oil1' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006609402&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%B0%B8%EA%B8%B0%EB%A6%84&srchPgNo=1&src_area=ssglist'
    ,'oil2' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006869928&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%B0%B8%EA%B8%B0%EB%A6%84&srchPgNo=1&src_area=ssglist'
    ,'oil3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000017291167&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%B0%B8%EA%B8%B0%EB%A6%84&srchPgNo=1&src_area=ssglist'
    ,'oil4' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000038740944&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%B0%B8%EA%B8%B0%EB%A6%84&srchPgNo=1&src_area=ssglist'
    ,'oil5' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000023312813&siteNo=6001&salestrNo=2037&tlidSrchWd=%EC%B0%B8%EA%B8%B0%EB%A6%84&srchPgNo=1&src_area=ssglist'
}

for k,v in data_dict.items():
    get_data(k,v)
    pass