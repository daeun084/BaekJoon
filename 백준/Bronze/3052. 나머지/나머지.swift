import Foundation

var integerSet: Set<Int> = Set<Int>()

for i in (1...10){
    let n = (Int)(readLine()!)!
    integerSet.insert(n%42)
}
print(integerSet.count)