class Solution(object):
    def interpret(self, command):
        res = ""
        dic = {"G":"G","(al)":"al","()":"o"}
        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'
            elif command[i:i+2] == '()':
                res += 'o'
            elif command[i:i+4] == '(al)':
                res += "al"
            else : 
                continue
        return res
        