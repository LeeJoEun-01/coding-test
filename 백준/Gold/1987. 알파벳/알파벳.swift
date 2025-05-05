import Foundation

let inputs = readLine()!.split(separator: " ").map { Int($0)! }
let R = inputs[0]
let C = inputs[1]

var board = [[Int]]()
for _ in 0..<R {
    board.append(readLine()!.map { Int($0.asciiValue! - 65) })  // A=0, B=1로 숫자화
}

let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]
var maxN = 0

// 방문한 알파벳을 비트마스크로 표현
func backTracking(_ x: Int, _ y: Int, _ bitmask: Int, _ count: Int) {
    maxN = max(maxN, count)

    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]

        if nx >= 0 && nx < R && ny >= 0 && ny < C {
            let nextAlpha = board[nx][ny]
            if bitmask & (1 << nextAlpha) == 0 {  // 방문 안했다면
                backTracking(nx, ny, bitmask | (1 << nextAlpha), count + 1)
            }
        }
    }
}

let startAlpha = board[0][0]
backTracking(0, 0, 1 << startAlpha, 1)
print(maxN)