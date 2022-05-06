// 2. 기초-입출력

// [10] 정수형(int으로 변수를 선언하고 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.
const num10 = prompt("정수를 입력하세요");
const Num10 = parseInt(num10);
console.log(Num10);
console.log(Number(num10));
// parseInt() : 문자열로 된 부분에서 숫자만 뽑아서 변환
// Number() : 문자열 전체가 숫자일 때 소수점까지 숫자타입으로

// [11] 문자형(char)으로 변수를 하나 선언하고 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.
const char11 = prompt("문자를 입력하세요");
console.log(char);

// [12] 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자.
const num12 = prompt("실수를 입력하세요");
const Num12 = parseFloat(num12);
console.log(Num12);
/* 형 변환
    parseInt() : int형으로 변환
    parseFloat() : float형으로 변환
    String(): String형으로 변환
    변수+"" : String형으로 변환*/

// [13] 정수(int) 2개를 입력받아 그대로 출력해보자.(단, 띄어쓰기를 기준으로 입력한다.)
const num13 = prompt("정수 2개를 입력하세요.").split(" ");
console.log(Number(num13[0]), Number(num13[1]));
console.log(typeof Number(num13[0]), typeof Number(num13[1]));

// [14] 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
const char14 = prompt("문자 2개를 입력하세요.").split(" ");
console.log(char14[1], char14[0]);

// [15] 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.
const num15 = prompt("실수를 입력하세요.");
const Num15 = parseFloat(num15);
console.log(Num15.toFixed(3));
/* 소수점 버림, 올림, 반올림 - 정수 반환
    a.ceil() : 소수점 올림
    a.floor() : 소수점 버림
    a.round() : 소수점 반올림
  소수점 처리 - 실수 변환
    a.toFixed(3) : 숫자에서 원하는 소수점 길이만큼 반올림해서 변환
*/

// [16] int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.
const num16 = prompt("정수를 입력하세요.");
const Num16 = parseInt(num16);
console.log(Num16, Num16, Num16);

// [17] 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자. 클론 기호를 기준으로 두 수가 각 변수에 저장된다.
const time17 = prompt("시간을 입력하세요.").split(":");
console.log(`${time17[0]}:${time17[1]}`);

/* [18] 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자
    입력 : 2020.2.9
    출력 : 2020.02.09
    (단, m 혹은 d가 한 자리 수인 경우 앞에 0을 붙여 출력한다.)
*/
const day18 = prompt("년, 월, 일을 입력하세요.").split(".");
if (day18[1].length === 1) {
  day18[1] = "0" + day18[1];
}
if (day18[2].length === 1) {
  day18[2] = "0" + day18[2];
}
console.log(`${day18[0]}.${day18[1]}.${day18[2]}`);

/* [19] 주민번호는 XXXXXX-XXXXXXX로 구성된다. 앞의 6자리는 생년월일이고 뒤 7자리는 성별, 지역, 오류검출코드이다. 주민번호를 입력받아 형태를 바꿔 출력해보자.
    입력 : 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
        123456-7654321
    출력 : '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.
        1234567654321
*/
const number = prompt("주민번호를 입력하세요").split("-");
console.log(`${number[0]}${number[1]}`);

// [20] 1개의 문자열을 입력받아 그대로 출력해보자.
const string20 = prompt("문자열을 입력하세요");
console.log(string20);

// [22] 공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의 단어로 구성되고, 엔터로 끝난다.
const string22 = prompt("문자열을 입력하세요");
console.log(string20);

/* [23] 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
    입력 : 1.435
    출력 : 1
        435
*/
const num23 = prompt("실수를 입력하세요").split(".");
console.log(num23[0]);
console.log(num23[1]);

/* [24] 단어를 1개 입력받는다. 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.(단, 단어의 문자(여엉)를 하나씩 나누어 한 줄에 한 개씩 ''로 묶어서 출력한다.)
    입력 : 'Boy'
    출력 : 'B'
    'o'
    'y'
 */
const string24 = prompt("단어 하나를 입력하세요");
for (let i = 0; i < string24.length; i++) {
  console.log(string24[i]);
}

/* [25] 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
    입력 : 75254
    출력 : [70000]
    [5000]
    [200]
    [50]
    [4]
*/
const num25 = prompt("다섯 자리 정수 하나를 입력하세요");
let count = num25.length - 1;
for (let i = 0; i < num25.length; i++) {
  console.log(num25[i] + "0".repeat(count));
  count -= 1;
}

// [26] 입력되는 시:분:초에서 분만 출력해보자.
const time26 = prompt("시:분:초를 입력하세요").split(":");
console.log(time26[1]);

/* [27] 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다. 
년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력해보자.
(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
 */
const day27 = prompt("년, 월, 일을 입력하세요.").split(".");
if (day27[1].length === 1) {
  day27[1] = "0" + day27[1];
}
if (day27[2].length === 1) {
  day27[2] = "0" + day27[2];
}
console.log(`${day27[2]}-${day27[1]}-${day27[0]}`);
