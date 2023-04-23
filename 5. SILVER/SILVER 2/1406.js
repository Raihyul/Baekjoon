// https://www.acmicpc.net/problem/1406

// const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const input = require("fs")
  .readFileSync("1406_test.txt")
  .toString()
  .trim()
  .split("\n");
const [sentence, n, ...progress] = input;

// 시간초과
// function solution(sentence, n, ...progress) {
//   let length = sentence.length;
//   let cursor = length - 1;
//
//   for (let i = 0; i < n; i++) {
//     switch (progress[i]) {
//       case "L":
//         if (cursor == -1) break;
//         cursor--;
//         break;
//       case "D":
//         if (cursor == length - 1) break;
//         cursor++;
//         break;
//       case "B":
//         if (cursor == -1) break;
//         sentence = sentence.slice(0, cursor) + sentence.slice(cursor + 1);
//         cursor--;
//         length--;
//         break;
//       default:
//         sentence =
//           sentence.slice(0, cursor + 1) +
//           progress[i].split(" ")[1] +
//           sentence.slice(cursor + 1);
//         cursor++;
//         length++;
//         break;
//     }
//   }
//
//   console.log(sentence);
// }

// 시간초과
// function solution(sentence, n, ...progress) {
//   let answer = sentence.split("");
//   let cursor = sentence.length - 1;
//
//   for (const order of progress) {
//     switch (order) {
//       case "L":
//         if (cursor == -1) break;
//         cursor--;
//         break;
//       case "D":
//         if (cursor == sentence.length - 1) break;
//         cursor++;
//         break;
//       case "B":
//         if (cursor == -1) break;
//         answer.splice(cursor, 1);
//         cursor--;
//         break;
//       default:
//         answer.splice(cursor + 1, 0, order.split(" ")[1]);
//         cursor++;
//         break;
//     }
//   }
//   console.log(answer.join(""));
// }

function solution(sentence, n, ...progress) {
  const leftStack = sentence.split("");
  const rightStack = [];

  for (const order of progress) {
    switch (order) {
      case "L":
        if (!leftStack.length) break;
        rightStack.push(leftStack.pop());
        break;
      case "D":
        if (!rightStack.length) break;
        leftStack.push(rightStack.pop());
        break;
      case "B":
        if (!leftStack.length) break;
        leftStack.pop();
        break;
      default:
        leftStack.push(order.split(" ")[1]);
        break;
    }
  }
  console.log(leftStack.join("") + rightStack.reverse().join(""));
}

solution(sentence, n, ...progress);

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const l = input[0].split("");
const r = [];

for (let i = 2; i < 2 + Number(input[1]); i++) {
  input[i][0] == "L" && l.length && r.push(l.pop());
  input[i][0] == "B" && l.length && l.pop();
  input[i][0] == "D" && r.length && l.push(r.pop());
  input[i][0] == "P" && l.push(input[i][2]);
}
console.log([...l, ...r.reverse()].join(""));
