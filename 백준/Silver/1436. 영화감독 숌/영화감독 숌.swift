import Foundation

let target = Int(readLine()!)
var num : Int = 666
var count = 0

for i in 666...10000000 {
    var n = i
    
    while n >= 666 {
        if n % 1000 == 666 {
            count += 1
            break
        }
        n /= 10
    }
    
    if count == target {
        print(i)
        break
    }
}