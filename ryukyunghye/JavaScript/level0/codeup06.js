// 6. 기초 - 비트 시프트 연산

// [47] 정수 1개를 입력받아 2배 곱해 출력해보자.
const num47 = prompt("정수를 입력하세요");
console.log(Number(num47) << 1);

// [48] 정수 2개(a,b)를 입력받아 a를 2(b 제곱)배 곱한 값으로 출력해보자. (a*2(b제곱))
const num48 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num48[0]) << Number(num48[1]));
