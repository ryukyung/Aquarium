'''PROJECT04 QR코드 생성기
QR코드를 자동으로 생성하는 프로그램을 만들어봅니다.
'''
import qrcode 

file_path = r'week1\project04.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path= 'week1\\' + qr_data + '.png'
        qr_img.save(save_path)