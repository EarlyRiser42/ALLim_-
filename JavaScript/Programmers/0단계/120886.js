function solution(before, after) {
    // 정렬하여 각 인덱스를 비교함
    before = [...before].sort()
    after = [...after].sort()
    return JSON.stringify(before) === JSON.stringify(after) ? 1 : 0
}