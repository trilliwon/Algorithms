class Solution {
func reverse(_ x: Int) -> Int {
	if -2147483648 > x || x > 2147483647{
		return 0
	}
	
	let isLessThanZero = 0 > x
	var value = abs(x)
	
	guard let reversed: Int = Int(String(value).characters.map { "\($0)" }.reversed().reduce("") { $0 + $1 }) else { return 0 }

	if isLessThanZero {
		value =  reversed * -1
	} else {
		value = reversed
	}
	
	if -2147483648 > value || value > 2147483647{
		return 0
	}
	return value
}
}
