// 11. 기초 - 조건/선택 실행 구조

// [65] 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
const num65 = prompt("정수 3개를 입력하세요").split(" ");
for (let i = 0; i < 3; i++) {
  if (Number(num65[i]) % 2 === 0) {
    console.log(Number(num65[i]));
  }
}

// [66] 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
const num66 = prompt("정수 3개를 입력하세요").split(" ");
for (let i = 0; i < 3; i++) {
  if (Number(num66[i]) % 2 === 0) {
    console.log("even");
  } else {
    console.log("odd");
  }
}

// [67] 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
const num67 = prompt("정수를 입력하세요");
if (num67 > 0) {
  console.log("plus");
} else {
  console.log("minus");
}
if (num67 % 2 == 0) {
  console.log("even");
} else {
  console.log("odd");
}

/* [68] 점수(정수, 00~100)를 입력받아 평가를 출력해보자.
평가기준) A : 90~100 | B : 70~89 | C : 40~69 | D : 0~39
*/
const score68 = prompt("점수를 입력하세요");
if (score68 >= 90 && score68 <= 100) {
  console.log("A");
} else if (score68 >= 70 && score68 <= 89) {
  console.log("B");
} else if (score68 >= 40 && score68 <= 69) {
  console.log("C");
} else {
  console.log("D");
}

/* [69] 평가를 문자(A, B, C, D)로 입력받아 내용을 다르게 출력해보자.
A : best!! | B : good!! |C : run! |D : slowly~ | 나머지 문자들 : what?
*/
const char69 = prompt("평가를 입력하세요");
if (char69 == "A") {
  console.log("best!!");
} else if (char69 == "B") {
  console.log("good!!");
} else if (char69 == "C") {
  console.log("run!");
} else if (char69 == "D") {
  console.log("slowly~");
} else {
  console.log("what?");
}

switch (char69) {
  case "A":
    console.log("best!!");
    break;
  case "B":
    console.log("good!!");
    break;
  case "C":
    console.log("run!");
    break;
  case "D":
    console.log("slowly~");
    break;
  default:
    console.log("what?");
}

/* 70. 월이 입력될 때 계절의 이름이 출력되도록 해보자.
winter : 12, 1, 2 | spring : 3, 4, 5 | summer : 6, 7, 8 | fall : 9, 10, 11
*/
const season = prompt("월을 입력하세요");
if (season == "12" || season == "1" || season == "2") {
  console.log("winter");
} else if (season == "3" || season == "4" || season == "5") {
  console.log("spring");
} else if (season == "6" || season == "7" || season == "8") {
  console.log("summer");
} else if (season == "9" || season == "10" || season == "11") {
  console.log("fall");
} else {
  console.log("1~12 중 하나를 입력하세요");
}

switch (season) {
  case "12":
  case "1":
  case "2":
    console.log("winter");
    break;
  case "3":
  case "4":
  case "5":
    console.log("spring");
    break;
  case "6":
  case "7":
  case "8":
    console.log("summer");
    break;
  case "9":
  case "10":
  case "11":
    console.log("fall");
    break;
  default:
    console.log("1~12 중 하나를 입력하세요");
}
