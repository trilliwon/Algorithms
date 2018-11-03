//: [Previous](@previous)


/*:
 
 # Merge Sort
 
 ### Runtime:
 - Best: O(NlogN)
 - Average: O(NlogN)
 - Worst: O(NlogN)
 
 ### Memory:
 - O(N)
 
 ```swift
 
 var items = [6, 2, 7, 4, 5, 10]
 items.mergeSort() // in place sorting
 let sortedItems = items.mergeSorted() // return sorted array
 
 ```
 
 */


extension Array where Element : Comparable {

    private func merge(_ array: inout [Element],
                       _ helper: inout [Element],
                       low: Int,
                       middle: Int,
                       high: Int) {
        
        // copy array to helper
        for i in low...high {
            helper[i] = array[i]
        }

        var helperLeft = low
        var helperRight = middle + 1
        var currnet = low

        // loop helper. compare left half and right half
        // small element should be inserted into original array
        while helperLeft <= middle && helperRight <= high {

            if helper[helperLeft] <= helper[helperRight] {
                array[currnet] = helper[helperLeft]
                helperLeft += 1
            } else {
                array[currnet] = helper[helperRight]
                helperRight += 1
            }
            currnet += 1
        }

        let remaining = middle - helperLeft + 1

        for i in 0..<remaining {
            array[currnet + i] = helper[helperLeft + i]
        }
    }

    private func mergeSort(_ array: inout [Element], _ helper: inout [Element], low: Int, high: Int) {
        if low < high {
            let middle: Int = (high + low) / 2
            mergeSort(&array, &helper, low: low, high: middle) // sort left half
            mergeSort(&array, &helper, low: middle + 1, high: high) // sort right half
            merge(&array, &helper, low: low, middle: middle, high: high) // merge
        }
    }

    public mutating func mergeSort() {
        var helper = self
        mergeSort(&self, &helper, low: 0, high: count - 1)
    }
    
    public func mergeSorted() -> [Element] {
        var elements = self
        elements.mergeSort()
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

var items = (0...20).map ({ _ in Int.random(in: Range(uncheckedBounds:  (-1000, 1000))) })
items.shuffle()
print("Array to be sorted => ", items)

items.mergeSort()
print("Sorted in place    => ", items)
assert(items.isSorted)

print("----")

items.shuffle()
print("Array to be sorted => ", items)

let sortedItems = items.mergeSorted()
print("Sorted in place    => ", sortedItems)
assert(sortedItems.isSorted)
    

//: [Next](@next)
