'''PROJECT06 압축파일 암호 푸는 프로그램
압축파일의 암호를 푸는 프로그램을 만들어 봅니다. 번호를 생성하고 암호화된 압축파일에 대입해서 암호를 푸는 방식입니다.'''
import itertools
import zipfile

def un_zip(password_string, minLen, maxLen, zFile): # 패스워드 문자열, 비밀번호 최소길이, 최대길이, 집 파일
    for len in range(minLen, maxLen+1):
        to_attempt = itertools.product(password_string, repeat =len)
        for attempt in to_attempt:
            password = ''.join(attempt)
            print(password)
            try: # 비밀번호가 맞으면 try 실행 
                zFile.extractall(pwd = password.encode())
                print(f"비밀번호는 {password}입니다.");
                return 1
            except: # 비밀번호가 틀리면 오류가 발생하여 except를 실행
                pass

password_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
zFile =zipfile.ZipFile(r'project06_password.zip') #비밀번호가 입력된 압축파일의 경로를 입력하여 불러옴
minLen = 1
maxLen = 5

unzip_result = un_zip(password_string, minLen, maxLen, zFile)

if unzip_result ==1:
    print("암호 찾기에 성공하였습니다.")
else:
    print("암호 찾기에 실패하였습니다.")