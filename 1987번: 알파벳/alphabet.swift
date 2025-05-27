
let nums = readLine()!.split(separator: " ").map { Int($0)! }
let R = nums[0]
let C = nums[1]
var arr: [[Character]] = []
for _ in 0..<R {
    arr.append(Array(readLine()!))
}

var ans = Set<Character>()
ans.insert(arr[0][0])

var maxN = 0
let dx = [0,0,1,-1]
let dy = [1,-1,0,0]

func backTracking(_ x: Int, _ y: Int, _ n: Int) {
    maxN = max(n,maxN)
    
    for i in 0..<4 {
        let newX = x+dx[i]
        let newY = y+dy[i]
        
        if newX >= 0 && newX < R && newY >= 0 && newY < C {
            if !ans.contains(arr[newX][newY]) {
                ans.insert(arr[newX][newY])
                backTracking(newX, newY, n+1)
                ans.remove(arr[newX][newY])
            }
        }
    }
}

backTracking(0,0,1)
print(maxN)