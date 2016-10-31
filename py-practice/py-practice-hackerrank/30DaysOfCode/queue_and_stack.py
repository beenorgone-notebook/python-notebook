class Solution:

    def __init__(self):
        '''Create a queue and a stack'''
        self.queue = []
        self.stack = []

    def pushCharacter(self, character):
        '''pushes a character onto a stack'''
        self.stack.append(character)

    def enqueueCharacter(self, character):
        '''enqueus a character in the queue instance variable'''
        self.queue.append(character)

    def popCharacter(self):
        '''pops and returns the character at the top of the stack instance variable'''
        if not self.stack:
            return None
        return self.stack.pop()

    def dequeueCharacter(self):
        '''pops and returns the character at the top of the queue instance variable.'''
        if not self.queue:
            return None
        return self.queue.pop(0)


'''# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")'''
