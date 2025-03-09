import Foundation

let numCase = Int(readLine()!)!
var arr2D : [[Int]] = Array(repeating: Array(repeating: 0,count:2 ), count: 41)

arr2D[0] = [1,0]
arr2D[1] = [0,1]
arr2D[2] = [1,1]

for i in 3..<41 {
    arr2D[i][0] = arr2D[i-1][0] + arr2D[i-2][0]
    arr2D[i][1] = arr2D[i-1][1] + arr2D[i-2][1]
}

for _ in 0..<numCase {
    let target = Int(readLine()!)!
    print(arr2D[target][0], arr2D[target][1])
}