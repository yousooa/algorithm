// 실패율: https://school.programmers.co.kr/learn/courses/30/lessons/42889

// 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
// N: 전체 스테이지 개수
// stages: 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
// 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
// 각 자연수: 사용자가 현재 도전 중인 스테이지의 번호
// N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자
// 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록
// 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0

// 내 풀이
function solution(N, stages) {
  let answer = [];
  let fail = [];
  let currentStage = 1;
  while (currentStage <= N) {
    const noClear = stages.filter((stage) => stage === currentStage).length;
    const clear = stages.filter((stage) => stage >= currentStage).length;
    fail.push([noClear / clear, currentStage]);
    currentStage++;
  }
  fail.sort((a, b) => b[0] - a[0]);
  console.log(fail);
  fail.forEach((ele) => answer.push(ele[1]));
  return answer;
}

// for문이 더 시간 단축
function solution(N, stages) {
  let answer = [];
  let fail = [];
  for (let i = 1; i <= N; i++) {
    const noClear = stages.filter((stage) => stage === i).length;
    const curr = stages.filter((stage) => stage >= i).length;
    fail.push([i, noClear / curr]);
  }
  fail.sort((a, b) => {
    return b[1] - a[1];
  });
  fail.forEach((ele) => answer.push(ele[0]));
  return answer;
}

// fail.sort((a, b) => {
//   return b[1] - a[1];
// });
// 실패율이 같다면 stage는 오름차순으로 정렬 -> 이 경우 실패율만 비교해도 stage 오름차순은 저절로 배열
