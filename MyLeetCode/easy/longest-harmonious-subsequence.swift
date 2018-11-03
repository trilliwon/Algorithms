class Solution {
	
	func findLHS(_ nums: [Int]) -> Int {
		
		if nums.isEmpty { return 0 }
		
		var nums = nums.sorted()
		var tupleArray = [(count: Int, value: Int)]()
		
		// input initial value
		var firstValue = nums[0]
		tupleArray.append((count: 1, value: firstValue))
		
		for index in 1..<nums.count {
			if nums[index] == firstValue {
				let bv = tupleArray[tupleArray.count-1].0
				tupleArray[tupleArray.count-1].0 += 1
			} else {
				firstValue = nums[index]
				tupleArray.append((1, firstValue))
			}
		}
		
		
		var harmoniousArraySize = 0
		
		if tupleArray.count == 1 {
			harmoniousArraySize = 0
		}
		
		for index in 1..<tupleArray.count {
			
			/// if value defernce by 1
			if abs(tupleArray[index-1].value - tupleArray[index].value) == 1 {
				
				/// make harmonious tuple
				let hTuple = (tupleArray[index-1].count + tupleArray[index].count)
				if hTuple > harmoniousArraySize {
					harmoniousArraySize = hTuple
				}
			}
		}
		
		return harmoniousArraySize
	}
}

