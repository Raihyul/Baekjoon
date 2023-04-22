const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const input = fs.readFileSync("9093_test.txt").toString().split("\n");

const [n, ...sentences] = input;

function solution(n, sentences) {
  const answer = [];
  for (const sentence of sentences) {
    const reversed = [];
    for (const word of sentence.split(" ")) {
      let reversedWord = "";
      for (let i = 0; i < word.length; i++) {
        reversedWord += word[word.length - 1 - i];
      }
      reversed.push(reversedWord);
    }
    answer.push(reversed.join(" "));
  }
  console.log(answer.join("\n"));
}

solution(n, sentences);
