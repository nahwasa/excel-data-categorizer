# excel-data-categorizer
친구 요청으로 만든 액셀파일 읽어 '구분' 칼럼 기준으로 시트를 만든 후 모든 데이터를 분류한 새로운 액셀파일을 만드는 무언가.

예를들어서 input.xlsx파일이
|이름|구분|직업|
|황세영|구분A|개발자|
|홍길동|구분A|의사|
|권시윤|구분B|개발자|

라고 하면, result.xlsx 파일에는 '구분A'와 '구분B' 시트가 있고,
'구분A' 시트에는
|이름|구분|직업|
|황세영|구분A|개발자|
|홍길동|구분A|의사|

'구분B' 시트에는
|이름|구분|직업|
|권시윤|구분B|개발자|

가 들어있음.
