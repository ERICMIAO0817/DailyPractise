class Solution:
    def reverseWords(self, s: str) -> str:
        tup = s.split(' ')
        print(tup)
        news = ''
        for index, item in enumerate(tup):
            if index == len(tup) - 1:
                news = news + ''.join(list(item)[::-1])
            else:
                news = news + ''.join(list(item)[::-1]) + ' '
        return news


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
