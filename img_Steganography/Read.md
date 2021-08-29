이미지 스테가노 그래피를 간단하게 해보았습니다
make_SampleImg.py에서 자신의 이미지 경로를 path변수에 넣은 뒤 실행시키면
변조시킬 비트와 색을 숫자로 입력 받아 그에 맞는 색과 비트만 전부 0으로 바꾼뒤 after.png라는 이름으로 저장합니다.

recover_Img_Steganography.py에서는 확인하고 싶은 이미지의 경로에 맞게 path 변수를 설정해줍니다.
그리고 실행시키면 0번 비트부터 7번 비트와 RGB색상의 값을 차례대로 확인하여 0이 아닌 부분만 검정색
그외는 하얀색으로 채워 (색상)(비트).png의 형태로 저장 해줍니다.

변조시킨 후 복구 한 빨강 0 비트
![RED0](https://user-images.githubusercontent.com/54605549/131254728-dfe75cad-6169-411a-9410-2f6607272236.png)

변조시킨 후 복구 한 초록 0 비트
![GREEN0](https://user-images.githubusercontent.com/54605549/131254726-b2b8cade-8d62-43a6-830b-04edd1c29261.png)

변조시킨 후 복구 한 파랑 0 비트
![BLUE0](https://user-images.githubusercontent.com/54605549/131254724-016f0093-b081-4c06-bcf6-9ea3840d5d45.png)

변조시킨 후 복구 한 빨강 1번 비트
![RED1](https://user-images.githubusercontent.com/54605549/131254723-084f9794-2e69-4884-9240-32967399ca09.png)
