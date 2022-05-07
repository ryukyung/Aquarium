// 10. 기초 - 삼항 연산

// [63] 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자. 단, 조건문을 사용하지 않고 3항 연산자 'and or'를 사용한다.
const num63 = prompt("정수 2개를 입력하세요").split(" ");
const result63 = Number(num63[0]) > Number(num63[1]) ? num63[0] : num63[1];
console.log(result63);

// [64] 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.(단, 삼항 연산자 이용)
const num64 = prompt("정수 3개를 입력하세요").split(" ");
let result64 = Number(num64[0]) > Number(num64[1]) ? num64[0] : num64[1];
result64 = result64 > Number(num64[2]) ? result64 : num64[2];
console.log(result64);
