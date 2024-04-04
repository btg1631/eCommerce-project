# eCommerce-project (댓글 감성분석)

## 1. 프로젝트 소개

여느때 처럼 쇼핑을 하고있던 '요한'은 상품을 구매하기 위한 정보를 얻기 위해 댓글을 살펴보던 중 평소에 배웠던 감성분석이 불현듯 떠올랐다. 

배달어플 등에서 별점 조작이나 댓글 알바 같은 내용들이 많아서 구매에는 댓글을 완전히 믿지 말라는것을 알고 있었기 때문에 딥러닝을 통한 감성분석과 댓글 알바를 걸러낼 수 있는 방법이 있지 않을까 생각했다.

또, 한국 자연어 처리의 더불어 고객의 감성을 분석할 수 있다면 커머스뿐만 아니라 많은 방면에서 활용할 수 있을 것이라는 생각이 들었기 때문에 프로젝트를 진행해 보기로 마음먹었다.

### 팀원 소개
|이름|||
|--|--|--|
|박요한|||
|장영지|||
|김유진|||

## 2. 데이터 수집

대상 사이트 : SSG [https://www.ssg.com/]

대상 카테고리 : 식품

<table>
    <tr>
    <td>담당</td>
    <td>품목</td>
    <td>코드</td>
    </tr>
  <tr>
    <td rowspan="5">박요한</td>
    <td>비빔면</td>
    <td rowspan="5"><a href="./docs/selenium/yohan/gathering.py">gathering.py</a></td>
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