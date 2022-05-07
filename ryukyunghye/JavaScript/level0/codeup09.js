// 9. 기초 - 비트 단위 논리 연산

// [59] 입력된 정수를 비트단위로 참 / 거짓을 바꾼 후 정수로 출력해보자.
const num59 = prompt("정수를 입력하세요");
console.log(~Number(num59));

// [60] 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
const num60 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num60[0]) & Number(num60[1]));

// [61] 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
const num61 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num61[0]) | Number(num61[1]));
console.log(parseInt(num61[0]) | parseInt(num61[1]));

// [62] 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
const num62 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num62[0]) ^ Number(num62[1]));
console.log(parseInt(num62[0]) ^ parseInt(num62[1]));
