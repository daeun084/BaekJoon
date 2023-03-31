import Foundation
let input = readLine()!.components(separatedBy: " ").map{ Int(String($0))! }
let n = input[0]
let m = input[1]

var Arr = [Int](1...n)

for i in (1...m){

    let tmp_arr = readLine()!.components(separatedBy: " ").map{ Int(String($0))!}
    let a = tmp_arr[0] - 1
    let b = tmp_arr[1] - 1
    
    var tmp: Int
    tmp = Arr[a]
    Arr[a] = Arr[b]
    Arr[b] = tmp
    
}

for i in (0...n-1){
    print(Arr[i], terminator:" ")
}