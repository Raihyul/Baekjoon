// https://www.acmicpc.net/problem/1406

// const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const input = require("fs")
  .readFileSync("10845_test.txt")
  .toString()
  .trim()
  .split("\n");
const [n, ...progress] = input;

function solution(n, progress) {
  const queue = [];
  let num = 0;
  let answer = "";

  for (const order of progress) {
    switch (order) {
      case "pop":
        if (num == 0) {
          answer += "-1\n";
          break;
        }
        answer += queue.shift() + "\n";
        num--;
        break;
      case "size":
        answer += num + "\n";
        break;
      case "empty":
        answer += num ? "0\n" : "1\n";
        break;
      case "front":
        if (num == 0) {
          answer += "-1\n";
          break;
        }
        answer += queue[0] + "\n";
        break;
      case "back":
        if (num == 0) {
          answer += "-1\n";
          break;
        }
        answer += queue[num - 1] + "\n";
        break;
      default:
        queue.push(order.split(" ")[1]);
        num++;
        break;
    }
  }
  console.log(answer);
}

solution(n, progress);
