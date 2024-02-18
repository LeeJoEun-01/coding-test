//
//  main.swift
//  SelfNumber_4673
//
//  Created by 이조은 on 2022/09/16.
//

import Foundation

var result = Array(repeating: true, count: 10001)

for i in 0...10000{
    let target = selfNumber(num: i)
    if target <= 10000 {
        result[target] = false
    }
}

for j in 0...10000{
    if result[j] == true {
        print(j)
    }
}

//셀프넘버인지 판별하는 함수
func selfNumber(num: Int) -> Int{
    var number = num
    var total = num
    while(number != 0) {
        total += number%10
        number = number/10
    }
    return total
}

