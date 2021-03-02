class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
        highest = 0
        for i in altitudes:
            if(i > highest): highest = i
        return highest