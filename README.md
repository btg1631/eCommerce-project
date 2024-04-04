# eCommerce-project (댓글 감성분석)

## 1. 프로젝트 소개

여느때 처럼 쇼핑을 하고있던 '요한'은 상품을 구매하기 위한 정보를 얻기 위해 댓글을 살펴보던 중 평소에 배웠던 감성분석이 불현듯 떠올랐다. 

배달어플 등에서 별점 조작이나 댓글 알바 같은 내용들이 많아서 구매에는 댓글을 완전히 믿지 말라는것을 알고 있었기 때문에 딥러닝을 통한 감성분석과 댓글 알바를 걸러낼 수 있는 방법이 있지 않을까 생각했다.

또, 한국 자연어 처리의 더불어 고객의 감성을 분석할 수 있다면 커머스뿐만 아니라 많은 방면에서 활용할 수 있을 것이라는 생각이 들었기 때문에 프로젝트를 진행해 보기로 마음먹었다.

### 팀원 소개
|이름|담당|비고|
|--|--|--|
|박요한|설계, 크롤링, 분석, 머신러닝||
|장영지|크롤링||
|김유진|크롤링||

## 2. 전략
### 변인 통제 설정
- 같은 카테고리의 제품 댓글을 수집할 것
- 같은 고객군이 이용하는 용량의 댓글을 수집할 것
    + 예) 200g 만두 -> 비슷한 용량의 만두들로 (한끼 분량의 제품을 사는 고객군)
- 같은 기간 내의 댓글을 분석할 것
- 동일 고객군에 대해 다른 가격의 품목을 수집할 것
- 댓글은 긍정과 부정으로 나눈다. (4,5는 긍정/1,2는 부정)
    + 3은 긍정/부정 데이터를 생성 후 딥러닝을 통한 모델 제작 후 분류한다. 

### 가정
- 비슷한 용량이면 같은 고객군이 이용한다.
- 같은 기간 내에 동일한 고객군이 이용한다.
- 가격의 차이는 고객에게 유의미한 이유로 작용한다.
- 딥러닝 모델은 완벽하다

## 3. 데이터 수집

대상 사이트 : SSG [https://www.ssg.com/]

대상 카테고리 : 식품

---
[데이터 크롤링 코드](./docs/selenium/yohan/gathering.py)

수집 코드 초안 작성 : 장영지

디버깅 및 수정 / 실행 코드 제작 : 박요한

<table>
    <tr>
    <td>담당</td>
    <td>품목</td>
    <td>코드</td>
    </tr>
  <tr>
    <td rowspan="5">박요한</td>
    <td>비빔면</td>
    <td rowspan="5"><a href="./docs/selenium/yohan/gathering.py">gathering.py</a><br>
    <a href="./docs/selenium/yohan/run_gathering.py">run_gathering.py</a>
    </td>
  </tr>
  <tr>
    <td>참기름</td>
  </tr>
  <tr>
    <td>햄</td>
  </tr>
  <tr>
    <td>교자</td>
  </tr>
  <tr>
    <td>토마토 소스</td>
  </tr>
  <tr>
    <td rowspan="5">장영지</td>
    <td>식빵</td>
    <td rowspan="5">내용</td>
  </tr>
  <tr>
    <td>치즈</td>
  </tr>
  <tr>
    <td>우유</td>
  </tr>
  <tr>
    <td>생수</td>
  </tr>
  <tr>
    <td>요거트</td>
  </tr>  <tr>
    <td rowspan="5">김유진</td>
    <td>카놀라유</td>
    <td rowspan="5">내용</td>
  </tr>
  <tr>
    <td>총각김치</td>
  </tr>
  <tr>
    <td>숙주나물</td>
  </tr>
  <tr>
    <td>팬케이크 파우더</td>
  </tr>
  <tr>
    <td>쌀</td>
  </tr>


</table>





- [스케쥴러]('https://docs.google.com/spreadsheets/d/1nxopVWUGgYlj-BUAeGTyQR1V89IP-p7GziXPLiKHoSo/edit#gid=652261404')