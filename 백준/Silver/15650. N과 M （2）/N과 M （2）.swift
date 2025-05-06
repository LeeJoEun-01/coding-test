let inputs = readLine()!.split(separator: " ").map { Int($0)! }
let N = inputs[0]
let M = inputs[1]

var ans: Array<Int> = []

func backTracking(_ start: Int) {
    if ans.count == M {
        print(ans.map{ String($0+1) }.joined(separator: " "))
        return
    }
    
    for i in start..<N {
        ans.append(i)
        backTracking(i+1)
        ans.removeLast()
    }
}

backTracking(0)