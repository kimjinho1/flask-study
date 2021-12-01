# flask static 파일 관리

## 그냥 프로젝트 안에다 static 폴더를 만들면 된다

**아래와 같은 방식으로 css를 로드해도 되지만**  
`<link rel="stylesheet" href="{{ url_for= "/static/css/style.css">`

**flask의 url_for 함수를 사용하는 것을 권장한다.**  
**-> static 폴더의 경로가 수정된 경우, html에서 일일히 경로를 수정하는 것을 방지해줌.**  
`<link rel="stylesheet" href="{{ url_for("static", filename="css/style.css") }}">`
