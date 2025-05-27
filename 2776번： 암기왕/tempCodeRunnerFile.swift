for i in 0..< arrM.count {
  if arrN[index] == arrM[i] {
    print(1)
  } else if arrN[index] < arrM[i] {
    while index < arrN.count {
      index += 1
      if arrN[index] >= arrM[i] {
        break
      }
    }
  } else {
    print(0)
  }

}