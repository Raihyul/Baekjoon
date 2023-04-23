// https://www.acmicpc.net/problem/1874

// const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const input = require("fs")
  .readFileSync("1874_test.txt")
  .toString()
  .split("\n");

const [n, ...progression] = input;
열;
function stackProgression(n, progression) {
  const stack = [1];
  const answer = ["+"];
  let num = 2;
  for (const progressionNumber of progression) {
    while (1) {
      if (stack.slice(-1)[0] == progressionNumber) {
        answer.push("-");
        stack.pop();
        break;
      }
      if (num > n) {
        console.log("NO");
        return;
      }
      answer.push("+");
      stack.push(num++);
    }
  }
  console.log(answer.join("\n"));
}

progression.pop();

stackProgression(n, progression);
