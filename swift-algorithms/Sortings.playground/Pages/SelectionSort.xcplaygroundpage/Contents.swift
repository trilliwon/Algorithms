//: [Previous](@previous)

/*:

 # Selection Sort

 ### Runtime:
 - Best: O(N^2)
 - Average: O(N^2)
 - Worst: O(N^2)

 ### Memory:
 - O(1)

 ```swift

 var items = [6, 2, 7, 4, 5, 10]
 items.selectionSort() // in place sorting
 let sortedItems = items.selectionSorted() // return sorted array

 ```

 */

extension Array where Element : Comparable {

    public mutating func selectionSort() {

        for i in 0..<count {
            var minIndex = i

            for j in (i + 1)..<count {
                if self[minIndex] > self[j] {
                    minIndex = j
                }
            }

            swapAt(minIndex, i)
        }
    }

    public func selectionSorted() -> [Element] {
        var elements = self
        elements.selectionSort()
        return elements
    }
}

var items = [6, 2, 7, 4, 5, 10]
items.shuffle()
print("Array to be sorted => ", items)

items.selectionSort()
print("Sorted in place    => ", items)

print("----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.selectionSorted()
print("Sorted in place    => ", sortedItems)




//: [Next](@next)
