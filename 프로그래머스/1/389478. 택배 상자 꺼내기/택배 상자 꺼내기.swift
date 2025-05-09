import Foundation

func solution(_ n: Int, _ w: Int, _ num: Int) -> Int {
    var answer = 0
    let h = (n - 1) / w + 1    // 높이 계산
    var x = 1                  // 상자 번호
    var storage: [[Int]] = []  // 창고
    
    for i in 0..<h {
        var t: [Int] = []
        for _ in 0..<w {
            if x <= n {
                t.append(x)
                x += 1
            } else {
                t.append(0)
            }
        }
        
        if i % 2 == 0 {
            storage.append(t)
        } else {
            storage.append(t.reversed())
        }
    }
    
    for i in 0..<storage.count {
        for j in 0..<storage[0].count {
            if storage[i][j] == num {
                var d = i
                while d < h && storage[d][j] != 0 {
                    answer += 1
                    d += 1
                }
            }
        }
    }
    
    return answer
}