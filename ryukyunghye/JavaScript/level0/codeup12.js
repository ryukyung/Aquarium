// 12. 기초 - 반복 실행 구조

// [71, 73] 정수가 순서대로 입력된다.(단, 개수는 알 수 없다) 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
const num71 = prompt("정수를 입력하세요").split(" ");
for (let i = 0; i < num71.length; i++) {
  if (num71[i] == 0) {
    break;
  }
  console.log(num71[i]);
}

// [72] n개의 정수가 순서대로 입력된다.(단, n의 최대 개수는 알 수 없다,) n개의 입력된 정수를 순서대로 출력해보자.
const n = prompt("n을 입력하세요");
const num72 = prompt("정수를 입력하세요").split(" ");
for (let i = 0; i < n; i++) {
  console.log(num72[i]);
}

// [74] 정수(1~100) 1개가 입력되었을 때 카운트다운을 출력해보자. 입력_5, 출력_5 4 3 2 1
const num74 = prompt("정수를 입력하세요");
for (let i = Number(num74); i > 0; i--) {
  console.log(i);
}

// [75] 정수(1~100) 1개가 입력되었을 때 카운트다운을 출력해보자. 입력_5, 출력_4 3 2 1 0
const num75 = prompt("정수를 입력하세요");
for (let i = Number(num75); i >= 0; i--) {
  console.log(i);
}

// [76] 영문자(a~z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자. 입력_f, 출력_a b c d e f
const char76 = prompt("영문자를 입력하세요");
const num76 = char76.charCodeAt();
for (let i = 97; i <= num76; i++) {
  console.log(String.fromCharCode(i));
}

// [77] 정수(0~100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자. 입력_4, 출력_0 1 2 3 4
const num77 = prompt("정수를 입력하세요");
for (let i = 0; i <= num77; i++) {
  console.log(i);
}
