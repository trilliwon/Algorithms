class Solution {
    func wordSubsets(_ A: [String], _ B: [String]) -> [String] {

        let bCounterArray = B
            .map {
                $0.reduce(into: [:]) {
                    $0[String($1), default: 0] += 1
                }
            }
            .reduce(into: [:]) { (dict: inout [String: Int], word:  [String: Int]) in
                word.forEach {
                    dict[$0] = (dict[$0] == nil ? $1 : max(dict[$0]!, $1))
                }
        }

        let aCounterDictionary = A.reduce(into: [:]) {
            $0[$1] = $1.reduce(into: [:]) {
                $0[String($1), default: 0] += 1
            }
        }

        var answer = [String]()

        for (word, aCounter) in aCounterDictionary {
            var isUniversal = true
            for (key, bval) in bCounterArray {
                guard let aval = aCounter[key], aval >= bval else {
                    isUniversal = false
                    break
                }
            }

            if isUniversal {
                answer.append(word)
            }
        }

        return answer
    }
}
