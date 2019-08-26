class Solution {
    func uniqueMorseRepresentations(_ words: [String]) -> Int {
        let morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        var resultDict = [String: Int]()
        for word in words {
            var wordOfMorse = ""
            for c in word {
                wordOfMorse += morseCodes[Int(c.unicodeScalars.first!.value-97)]
            }
            resultDict[wordOfMorse, default: 0] += 1
        }
        print(resultDict)
        return resultDict.count
    }
}
