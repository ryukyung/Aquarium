// 7. 기초 - 비교 연산

// [49] 두 정수(a, b)를 입력받아 a가 b보다 크면 1을, a가 b보다 작거나 같으면 0을 출력하는 프로그램을 작성해보자.
const num49 = prompt("정수 2개를 입력하세요").split(" ");
if (Number(num49[0]) > Number(num49[1])) {
  console.log(1);
} else if (Number(num49[0]) <= Number(num49[1])) {
  console.log(0);
}

// [50] 두 정수(a, b)를 입력받아 a와 b가 같으면 1을, 같지 않으면 0을 출력하는 프로그램을 작성해보자.
const num50 = prompt("정수 2개를 입력하세요").split(" ");
if (Number(num50[0]) === Number(num50[1])) {
  console.log(1);
} else if (Number(num50[0]) != Number(num50[1])) {
  console.log(0);
}

// [51] 두 정수(a, b)를 입력받아 b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자
const num51 = prompt("정수 2개를 입력하세요").split(" ");
if (Number(num51[0]) > Number(num51[1])) {
  console.log(1);
} else {
  console.log(0);
}

// [52] 두 정수(a, b)를 입력받아 a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자
const num52 = prompt("정수 2개를 입력하세요").split(" ");
if (Number(num52[0]) != Number(num52[1])) {
  console.log(1);
} else {
  console.log(0);
}
