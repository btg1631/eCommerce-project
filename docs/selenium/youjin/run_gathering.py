from gatheringdatas import get_data

data_dict ={
    'rice1' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006611508&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B0%B1%EB%AF%B810kg&srchPgNo=1&src_area=ssglist'
    , 'rice2' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006610289&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B0%B1%EB%AF%B810kg&srchPgNo=1&src_area=ssglist'
    , 'rice3' : 'https://www.ssg.com/item/itemView.ssg?itemId=2097000314815&siteNo=6001&salestrNo=2449&tlidSrchWd=%EB%B0%B1%EB%AF%B810kg&srchPgNo=1&src_area=ssglist'
    , 'rice4' : 'https://www.ssg.com/item/itemView.ssg?itemId=2097001498019&siteNo=6001&salestrNo=2449&tlidSrchWd=%EB%B0%B1%EB%AF%B810kg&srchPgNo=1&src_area=ssglist'
    , 'rice5' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000019744485&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B0%B1%EB%AF%B810kg&srchPgNo=1&src_area=ssglist'
    , 'kimchi1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000053355587&siteNo=6001&salestrNo=2058&tlidSrchWd=%EC%B4%9D%EA%B0%81%EA%B9%80%EC%B9%98%201.5kg&srchPgNo=1&src_area=ssglist'
    , 'kimchi2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000020869359&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%B4%9D%EA%B0%81%EA%B9%80%EC%B9%98%201.5kg&srchPgNo=1&src_area=ssglist'
    , 'kimchi3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000047906506&siteNo=6001&salestrNo=2058&tlidSrchWd=%EC%B4%9D%EA%B0%81%EA%B9%80%EC%B9%98%201.5kg&srchPgNo=1&src_area=ssglist'
    , 'kimchi4' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000156850771&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%B4%9D%EA%B0%81%EA%B9%80%EC%B9%98%201.5kg&srchPgNo=1&src_area=ssglist'
    , 'pancake_powder1' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006609437&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B6%80%EC%B9%A8%EA%B0%80%EB%A3%A8%201kg&srchPgNo=1&src_area=ssglist'
    , 'pancake_powder2' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000008956834&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B6%80%EC%B9%A8%EA%B0%80%EB%A3%A8%201kg&srchPgNo=1&src_area=ssglist'
    , 'pancake_powder3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000052493818&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B6%80%EC%B9%A8%EA%B0%80%EB%A3%A8%201kg&srchPgNo=1&src_area=ssglist'
    , 'pancake_powder4' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000006613094&siteNo=6001&salestrNo=2058&tlidSrchWd=%EB%B6%80%EC%B9%A8%EA%B0%80%EB%A3%A8%201kg&srchPgNo=1&src_area=ssglist'
    , 'mung_bean_sprouts1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000519624545&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%88%99%EC%A3%BC&srchPgNo=1&src_area=ssglist'
    , 'mung_bean_sprouts2' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000050702898&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%88%99%EC%A3%BC&srchPgNo=1&src_area=ssglist'
    , 'mung_bean_sprouts3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000566216009&siteNo=6001&salestrNo=2058&tlidSrchWd=%EC%88%99%EC%A3%BC&srchPgNo=1&src_area=ssglist'
    , 'mung_bean_sprouts4' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000542517055&siteNo=7009&salestrNo=2449&tlidSrchWd=%EC%88%99%EC%A3%BC&srchPgNo=1&src_area=ssglist'
    , 'canola_oil1' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000041667986&siteNo=6001&salestrNo=2058&tlidSrchWd=%EC%B9%B4%EB%86%80%EB%9D%BC%EC%9C%A0&srchPgNo=1&src_area=ssglist'
    , 'canola_oil2' : 'https://www.ssg.com/item/itemView.ssg?itemId=0000007335664&siteNo=6001&salestrNo=2058&tlidSrchWd=%EC%B9%B4%EB%86%80%EB%9D%BC%EC%9C%A0&srchPgNo=1&src_area=ssglist'
    , 'canola_oil3' : 'https://www.ssg.com/item/itemView.ssg?itemId=1000030953268&siteNo=6001&salestrNo=2058&tlidSrchWd=%EC%B9%B4%EB%86%80%EB%9D%BC%EC%9C%A0&srchPgNo=1&src_area=ssglist'
    , 'canola_oil4' : 'https://www.ssg.com/item/itemView.ssg?itemId=2097001747995&siteNo=6001&salestrNo=2449&tlidSrchWd=%EC%B9%B4%EB%86%80%EB%9D%BC%EC%9C%A0&srchPgNo=1&src_area=ssglist'
}
'''
for k,v in data_dict.items():
    get_data(k,v)
    pass
'''

get_data('pancake_powder1',data_dict.get('pancake_powder1',False))