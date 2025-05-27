
let inputs = readLine()!.split(separator: " ").map{ Int($0)!}
let N = inputs[0]
let M = inputs[1]

var ans: Array<Int> = []

func backTracking() {
    if ans.count == M {
        print(ans.map{String($0)}.joined(separator: " "))
        return
    }
    for i in 1..<N+1 {
        if ans.contains(i) == false {
            ans.append(i)
            backTracking()
            ans.removeLast()
        }
    }
}

backTracking()
