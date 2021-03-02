class Solution:
    def interpret(self, command: str) -> str:
        ans = command.replace('()', 'o')
        return ans.replace('(al)', 'al')