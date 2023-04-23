// const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const input = require("fs")
  .readFileSync("9012_test.txt")
  .toString()
  .split("\n");

const strings = input.slice(1);

const result = strings.map((string) => {
  let left = 0;
  for (const bracket of string) {
    if (bracket === "(") left += 1;
    else left -= 1;
    if (left < 0) return "NO";
  }
  if (left == 0) return "YES";
  return "NO";
});

result.pop();

console.log(result.join("\n"));
