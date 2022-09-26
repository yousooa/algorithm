function solution(s) {
  var result = '';
  s = s.split(' ');
  for (let word of s) {
    for (let i in word) {
      result += word[i][i % 2 ? 'toLowerCase' : 'toUpperCase']();
    }
    result += ' ';
  }
  return result.slice(0, -1);
}

function solution(s) {
  return s
    .split(' ')
    .map((a) =>
      a
        .split('')
        .map((b, idx) => (idx % 2 ? b.toLowerCase() : b.toUpperCase()))
        .join('')
    )
    .join(' ');
}
