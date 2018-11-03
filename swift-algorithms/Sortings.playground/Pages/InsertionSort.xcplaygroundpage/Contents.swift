//: [Previous](@previous)

/*:

 # Insertion Sort

 ### Runtime:
 - Best: O(N)
 - Average: O(N^2)
 - Worst: O(N^2)

 ### Memory:
 - O(1)

 ```swift

 var items = [6, 2, 7, 4, 5, 10]
 items.insertionSort() // in place sorting
 let sortedItems = items.insertionSorted() // return sorted array

 ```

 */

extension Array where Element : Comparable {

    public mutating func insertionSort() {

        for i in 1..<count {
            let item = self[i]
            var j = i
            while j > 0 && item < self[j - 1] {
                self[j] = self[j - 1]
                j -= 1
            }
            self[j] = item
        }
    }

    public func insertionSorted() -> [Element] {
        var elements = self
        elements.insertionSort()
        return elements
    }
}

var items = [6, 2, 7, 4, 5, 10]
items.shuffle()
print("Array to be sorted => ", items)

items.insertionSort()
print("Sorted in place    => ", items)

print("----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.insertionSorted()
print("Sorted in place    => ", sortedItems)




//: [Next](@next)
