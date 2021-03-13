#leetcode 3 : Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrs = []   # 중복 없는 substring을 담는 리스트
        substr = ''   # 중복 없는 substring을 생성
        for w in s:
            if w not in substr:  #w가 substr에 없으면 추가
                substr += w
            elif w in substr:     #w가 substr에 값이 있으면
                substrs.append(substr)   #그 전까지 substr를 substrs에 저장
                index= substr.rfind(w)+1  #sub에서 w 위치를 찾아서 저장
                substr = substr[index:]+w   #w이후 substring 부터다시 저장
        substrs.append(substr) #마지막 substring까지 list에 추가

        max=0

        #리스트중 가장 길이가 긴 substring 반환

        for i, word in enumerate(substrs):
            if max < len(word):
                max = len(word)

        return max
        
