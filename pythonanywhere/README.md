# pythonanywhere

## pythonanywhere 사이트에서 flask로 만든 사이트를 쉽게 배포할 수 있다

**1 https://www.pythonanywhere.com 에 접속하여 회원가입 후 로그인**

**2 소스파일을 압축한 다음 아래 그림과 같이 업로드하고, Open Bash console here를 눌러 콘솔창으로 넘어가기**
![image](https://user-images.githubusercontent.com/29765855/145246021-d73c32d3-258f-477c-82c3-a35397527315.png)

**3 압축 해제 -> 가상환경 생성 -> 가상환경에 필요한 라이브러리를 설치**
![image](https://user-images.githubusercontent.com/29765855/145246735-5dd7f448-42b6-47e1-b089-33229cec68c0.png)

**4 Web으로 넘어가 Add a new web app -> Next -> Manual configuration -> Python 3.7 -> Next 순으로 진행**
![image](https://user-images.githubusercontent.com/29765855/145247238-022b060d-ca74-4cb2-93a4-2fbb8aa6444b.png)

**5 그러면 설정이 가능해지는데 소스 코드, 가상환경 경로를 수정해준다**
![image](https://user-images.githubusercontent.com/29765855/145247867-82dca05a-77ee-45f1-817c-91dd65089939.png)

**6 WSGI configuration file을 클릭**
![image](https://user-images.githubusercontent.com/29765855/145248371-86f2c884-21a8-4e1c-b79d-59f1aeb9adb6.png)  

**괄호친 코드를 주석 처리**
![image](https://user-images.githubusercontent.com/29765855/145248516-4561c20e-fff6-4c12-8c77-66efed89a8e8.png)  

**맨 아래 FLASK 부분 아래와 같이 수정하고 Save**
![image](https://user-images.githubusercontent.com/29765855/145248886-f8e6fe5a-5ce3-4ab8-9906-bb4a773b372d.png)

**7 Web으로 넘어와 Reload를 클릭하면 끝이다!**
![image](https://user-images.githubusercontent.com/29765855/145249820-c66d102d-8990-4cbb-86fb-9252e5a79188.png)
