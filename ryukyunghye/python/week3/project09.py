'''PROJECT09 영어 문서를 한글로 자동번역
영문 내용의 파일을 읽어 한글로 번역하고 새로운 파일로 저장하는 프로그램을 만들어봅니다.'''
from os import linesep
import googletrans

translator = googletrans.Translator() 

read_file_path = r"week3\project09_E.txt"
write_file_path = r"week3\project09_k.txt"

with open(read_file_path, 'r') as f : 
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko') 
    print(result1.text)
    with open(write_file_path,'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')