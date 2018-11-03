//: [Previous](@previous)


/*:

 # Quick Sort

 ### Runtime:
 - Best: O(NlogN)
 - Average: O(NlogN)
 - Worst: O(N^2)

 ### Memory:
 - O(logN)

 ```swift

 var items = [6, 2, 7, 4, 5, 10]
 items.quickSort() // in place sorting
 let sortedItems = items.quickSorted() // return sorted array

 ```

 */


extension Array where Element : Comparable {

    private func partition(_ array: inout [Element], left: Int, right: Int) -> Int {
        var left = left
        var right = right

        let pivot = array[(left + right)/2]
        while left <= right {

            while pivot > array[left] {
                left += 1
            }

            while pivot < array[right] {
                right -= 1
            }

            if left <= right {
                array.swapAt(left, right)
                left += 1
                right -= 1
            }
        }
        return left - 1
    }


    private func quickSort(_ array: inout [Element], left: Int, right: Int) {
        let index = partition(&array, left: left, right: right)
        if left < index {
            quickSort(&array, left: left, right: index)
        }

        if right > index + 1 {
            quickSort(&array, left: index + 1, right: right)
        }
    }

    public mutating func quickSort() {
        quickSort(&self, left: 0, right: count - 1)
    }

    public func quickSorted() -> [Element] {

        var elements = self
        elements.quickSort()
        return elements
    }

    var isSorted: Bool {
        if self.isEmpty {
            return true
        }

        for i in 1..<count {
            if self[i - 1] > self[i] {
                return false
            }
        }

        return true
    }
}

public func quickSortUsingFilter<Element: Comparable>(_ array: [Element]) -> [Element] {
    if array.count > 1 {
        let pivot = array[array.count / 2]
        return quickSortUsingFilter(array.filter({ $0 < pivot })) +
            array.filter({ $0 == pivot }) +
            quickSortUsingFilter(array.filter({ $0 > pivot }))
    }
    return array
}

var items = (0...20).map ({ _ in Int.random(in: Range(uncheckedBounds:  (-1000, 1000))) })
items.shuffle()
print("Array to be sorted => ", items)

items.quickSort()
print("Sorted in place    => ", items)
assert(items.isSorted)

print("-----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.quickSorted()
print("Sorted in place    => ", sortedItems)
assert(sortedItems.isSorted)

print("-----")
items.shuffle()

print("Array to be sorted => ", items)
let sortedItems1 = quickSortUsingFilter(items)
print("Sorted in place    => ", sortedItems1)
assert(sortedItems1.isSorted)



//: [Next](@next)

