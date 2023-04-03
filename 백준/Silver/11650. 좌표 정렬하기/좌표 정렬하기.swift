import Foundation
let n = (Int)(readLine()!)!

var arr = [[Int]](repeating:[Int](repeating: 0, count: 2), count:n)

for i in (0...n-1){

    let input = readLine()!.components(separatedBy: " ").map{ Int(String($0))!}
    
    arr[i][0] = input[0]
    arr[i][1] = input[1]
}

arr.sort(by: {$0[0] < $1[0]}) //인덱스 0을 기준으로 오름차순 정렬
arr.sort(by: {$0[0]==$1[0] && $0[1] < $1[1]}) //0인덱스가 동일할 시 인덱스 1을 기준으로 정렬

for i in (0...n-1){
    print(arr[i][0], arr[i][1])
}