// https://school.programmers.co.kr/learn/courses/30/lessons/81301
let a = 'one4seveneight45';

// 내풀이
function solution(s) {
  const numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];
  let result = [];
  s = s.match(/zero|one|two|three|four|five|six|seven|eight|nine|\d/g);
  s.forEach((element) =>
    numbers.includes(element)
      ? result.push(numbers.indexOf(element))
      : result.push(element)
  );
  return parseInt(result.join(''));
}

// 1)
function solution(s) {
  s = s
    .replace(/zero/g, 0)
    .replace(/one/g, 1)
    .replace(/two/g, 2)
    .replace(/three/g, 3)
    .replace(/four/g, 4)
    .replace(/five/g, 5)
    .replace(/six/g, 6)
    .replace(/seven/g, 7)
    .replace(/eight/g, 8)
    .replace(/nine/g, 9);
  return parseInt(s);
}

// 2)
function solution(s) {
  const numbers = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];
  let answer = s;
  for(let i = 0; i<numbers.length;i++){
    let arr = answer.split(numbers[i]);
    answer = arr.join(i);
  }
  return parseInt(answer);
}