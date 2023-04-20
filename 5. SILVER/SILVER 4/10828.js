const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const input = fs.readFileSync("10828_test.txt").toString().split("\n");

/*
// 시간초과
const stack = [];

for (let i = 1; i <= input[0]; i++) {
  if (input[i].match(/push \d+/g)) {
    const number = input[i].split(" ")[1];
    stack.push(number);
  } else {
    switch (input[i]) {
      case "pop":
        if (!stack.length) {
          console.log(-1);
          break;
        }
        console.log(stack.pop());
        break;
      case "size":
        console.log(stack.length);
        break;
      case "empty":
        console.log(stack.length ? 0 : 1);
        break;
      case "top":
        if (!stack.length) {
          console.log(-1);
          break;
        }
        console.log(stack[stack.length - 1]);
        break;
    }
  }
}

 */

/*
// 시간 초과
const stack = [];
let num = 0;

for (let i = 1; i <= input[0]; i++) {
  if (input[i].match(/push \d+/g)) {
    const number = input[i].split(" ")[1];
    stack.push(number);
    num++;
  } else {
    switch (input[i]) {
      case "pop":
        if (!num) {
          console.log(-1);
          break;
        }
        console.log(stack.pop());
        num--;
        break;
      case "size":
        console.log(num);
        break;
      case "empty":
        console.log(num ? 0 : 1);
        break;
      case "top":
        console.log(!num ? -1 : stack[num - 1]);
        break;
    }
  }
}
*/

/*
// 시간 초과
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let count = 0;
let stack = [];
let stackNum = 0;

rl.on("line", (input) => {
  // console.log(`Recived : ${input}`);
  if (count === 0) {
    count = parseInt(input) + 1;
  }
  count -= 1;

  if (input.match(/push \d+/g)) {
    const number = input.split(" ")[1];
    stack.push(number);
    stackNum++;
  } else {
    switch (input) {
      case "pop":
        if (!stackNum) {
          console.log(-1);
          break;
        }
        console.log(stack.pop());
        stackNum--;
        break;
      case "size":
        console.log(stackNum);
        break;
      case "empty":
        console.log(stackNum ? 0 : 1);
        break;
      case "top":
        console.log(!stackNum ? -1 : stack[stackNum - 1]);
        break;
    }
  }

  if (count === 0) {
    rl.close();
  }
});
*/

/*
// 시간 초과
const [n, ...commands] = input;

function solution(n, commands) {
  const stack = [];
  let num = 0;
  // let answer = "";

  for (let i = 0; i < n; i++) {
    const command = commands[i].split(" ")[0];

    switch (command) {
      case "push":
        const pushNum = commands[i].split(" ")[1];
        stack.push(pushNum);
        num++;
        break;
      case "pop":
        if (!num) {
          console.log(-1);
          break;
        }
        console.log(stack.pop());
        num--;
        break;
      case "size":
        console.log(num);
        break;
      case "empty":
        console.log(num ? 0 : 1);
        break;
      case "top":
        console.log(!num ? -1 : stack[num - 1]);
        break;
    }
  }
}

solution(n, commands);
*/

const [n, ...commands] = input;

function solution(n, commands) {
  const stack = [];
  let num = 0;
  let answer = "";

  for (let i = 0; i < n; i++) {
    const command = commands[i].split(" ")[0];

    switch (command) {
      case "push":
        const pushNum = commands[i].split(" ")[1];
        stack.push(pushNum);
        num++;
        break;
      case "pop":
        if (!num) {
          answer += "-1 ";
          break;
        }
        answer += stack.pop() + " ";
        num--;
        break;
      case "size":
        answer += num + " ";
        break;
      case "empty":
        answer += (num ? 0 : 1) + " ";
        break;
      case "top":
        answer += (!num ? -1 : stack[num - 1]) + " ";
        break;
    }
    console.log(commands[i], num, stack);
  }
  console.log(answer.replaceAll(" ", "\n"));
}

solution(n, commands);
