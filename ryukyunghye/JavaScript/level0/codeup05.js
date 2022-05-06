// 5. 기초 - 산술 연산

// [38, 39] 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
const num38 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num38[0]) + Number(num38[1]));

// [40] 입력된 정수의 부호를 바꿔 출력해보자.
const num40 = prompt("정수를 입력하세요");
console.log(Number(-num40));

// [41] 영문자 1개를 입력받아 그 다음 문자를 출력해보자. 영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음문자는 '1'이다.
const char41 = prompt("영문자를 입력하세요");
const num41 = char41.charCodeAt();
console.log(String.fromCharCode(num41 + 1));

// [42] 정수 2개(a,b)를 입력받아 a를 b로 나눈 몫을 출력해보자.
const num42 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num42[0] / Number(num42[1])));

// [43] 정수 2개(a, b)를 입력받아 a를 b로 나눈 나머지를 출력해보자.
const num43 = prompt("정수 2개를 입력하세요").split(" ");
console.log(Number(num43[0] % Number(num43[1])));

// [44] 정수를 1개 입력받아 1만큼 더해 출력해보자.
const num44 = prompt("정수를 입력하세요");
console.log(Number(num44) + 1);

// [45] 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자. (실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)
const num45 = prompt("정수를 입력하세요").split(" ");
console.log(Number(num45[0]) + Number(num45[1]));
console.log(Number(num45[0]) - Number(num45[1]));
console.log(Number(num45[0]) * Number(num45[1]));
console.log(Number(num45[0]) / Number(num45[1]));
console.log(Number(num45[0]) % Number(num45[1]));
console.log((Number(num45[0]) / Number(num45[1])).toFixed(2));

// [46] 정수 3개를 입력받아 합과 평균을 출력해보자.
const num46 = prompt("정수 3개를 입력하세요").split(" ");
console.log(Number(num46[0]) + Number(num46[1]) + Number(num46[2]));
console.log((Number(num46[0]) + Number(num46[1]) + Number(num46[2])) / 3);
