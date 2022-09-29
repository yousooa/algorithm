// https://school.programmers.co.kr/learn/courses/30/lessons/12915
// 힌트
// true - false = 1 / false - true = -1
function solution(strings, n) {
  strings.sort((a, b) => {
    const aString = a[n];
    const bString = b[n];
    if (aString !== bString) {
      return (aString > bString) - (aString < bString);
    } else {
      return (a > b) - (a < b);
    }
  });
  return strings;
}

// 다른 사람 풀이
// 힌트
// localeCompare: 문자열과 문자열 비교
console.log('a'.localeCompare('b')); // -1
console.log('b'.localeCompare('a')); // 1
console.log('a'.localeCompare('a')); // 0

const list = [1, 2, 3, 4];
list.push(5);
console.log(list); // [ 1, 2, 3, 4, 5 ]
list.pop();
console.log(list);