import Foundation

let input = readLine()!
var numN = Int(input)!

var num5 = 0
var num3 = 0

// numN에서 3을 계속 뺄 때 5의 배수가 되면 stop
// 5의 배수가 되지 않고 남으면 -1 출력
while true {
    if numN%5 == 0 {
        num5 = numN/5
        break
    } else if numN<0{
        num5 = 0
        num3 = -1
        break
    } else {
        numN = numN - 3
        num3 += 1
    }
}

print(num3+num5)