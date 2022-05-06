// 8. 기초 - 논리 연산

// [53] 1(true, 참) 또는 0(false, 거짓)이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
const num53 = prompt("1 또는 0을 입력하세요");
console.log(!Number(num53));

// [54] 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
const num54 = prompt("1 또는 0을 2번 입력하세요").split(" ");
console.log(Number(num54[0]) && Number(num54[1]));

// [55] 두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
const num55 = prompt("1 또는 0을 2번 입력하세요").split(" ");
console.log(Number(num55[0]) || Number(num55[1]));

// [56] 두 가지 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
const num56 = prompt("1 또는 0을 2번 입력하세요").split(" ");
const a = Number(num56[0]);
const b = Number(num56[1]);
console.log((a && !b) || (!a && b));

// [57] 두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
for (let i = 0; i < 4; i++) {
  const num57 = prompt("1 또는 0을 2번 입력하세요").split(" ");
  const a = Number(num57[0]);
  const b = Number(num57[1]);
  console.log((!a && !b) || (a && b));
}

// [58] 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
for (let i = 0; i < 4; i++) {
  const num58 = prompt("1 또는 0을 2번 입력하세요").split(" ");
  console.log(!(Number(num58[0]) || Number(num58[1])));
}
