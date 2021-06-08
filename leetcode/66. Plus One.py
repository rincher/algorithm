class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = 0
        array = []
        length = len(digits)
        for i in digits:
            length -= 1
            answer += i * 10 ** (length)
        answer += 1
        answer = str(answer)
        for i in answer:
            array.append(i)
        return array
