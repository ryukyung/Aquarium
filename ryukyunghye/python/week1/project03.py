'''PROJECT03 텍스트를 음성으로 변환하기
텍스트를 한글 음성으로 변환하고 변환된 파일을 재생하여 출력하는 프로그램을 만들어봅니다.'''
#main03_1 텍스트를 음성으로
from gtts import gTTS # gtts 라이브러리로부터 gTTS 기능만 불러와 사용
from playsound import playsound # playsound 모듈로부터 playsound를 불러와 사용

file_path =r'3. 텍스트를 음성으로 변환\project03.txt'
with open(file_path, 'rt', encoding="UTF8") as f :
    read_file =f.read()

tts = gTTS(text = read_file, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환\project03.mp3")