// 4. 기초 - 출력 변환

//31. 10진수를 입력받아 8진수로 출력해보자
const num31 = prompt("10진수를 입력하세요");
const Num31 = parseInt(num31);
console.log(Num31.toString(8));
// .toString(2|8|16) : 해당 진수로 변환

// [32] 10진수를 입력받아 16진수로 출력해보자.
const num32 = prompt("10진수를 입력하세요");
const Num32 = parseInt(num32);
console.log(Num32.toString(16));

// [33] 10진수를 입력받아 16진수로 출력해보자. 16진수(대문자)로 출력한다.
const num33 = prompt("10진수를 입력하세요");
const Num33 = parseInt(num33);
console.log(Num33.toString(16).toUpperCase());

//[34] 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
const num34 = prompt("8진수를 입력하세요");
const Num34 = parseInt(num34, 8);
console.log(Num34);

// [35] 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
const num35 = prompt("16진수를 입력하세요");
const Num35 = parseInt(num35, 16).toString(8);
console.log(Num35);

// [36] 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
const num36 = prompt("영문자를 입력하세요");
console.log(num36.charCodeAt());

// [37] 10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
const num37 = prompt("정수를 입력하세요");
console.log(String.fromCharCode(num37));
