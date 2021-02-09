/*
Evaluate the score of the parentheses

1. () = 1
2. s1s2 = s1+s2, ()() = 2
3. (s1) = s1*2, (()) = 2, (()()) = 4
*/

const OPEN_PARENS = '(';
const CLOSE_PARENS = ')';

function parenScore(str) {
  let stack = [];

  const sumUpStack = (startVal) => {
    let sPeek = stack[stack.length - 1]
    while (sPeek != null && sPeek !== OPEN_PARENS) {
      startVal += stack.pop();
      sPeek = stack[stack.length - 1]
    }
    return startVal;
  }

  for (let i = 0; i < str.length; i++) {
    let curVal = str[i];
    if (curVal === OPEN_PARENS) { //curVal = '('
      stack.push(curVal);
    } else { // curVal == ')'
      let sVal = stack.pop();
      if (sVal === OPEN_PARENS) {
        // sum up numbers on the top of the stack
        let sumCount = sumUpStack(1);
        stack.push(sumCount);
      } else { // value needs to be multiplied by 2 and added
        let sumCount = sumUpStack(sVal)
        stack.pop();
        let sum = sumUpStack(sumCount * 2);
        stack.push(sum);
      }
    }
  }
  return stack.pop();
}

console.log(parenScore('()()'), 2)
console.log(parenScore('(())()'), 3)
console.log(parenScore('(()())'), 4)
console.log(parenScore('(()(()()))'), 10)
console.log(parenScore('()()((())())'), 8)
console.log(parenScore('()()((())())(()())()(()())'), 17)
