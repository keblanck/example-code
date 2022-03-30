class RTSTest:
    def __init__(self):
        self.name = 'Kathleen\'s Testing class'
        self.array = [1,5,2,1,10,18,6,4,5,1000]
        self.comp = 6
    
    def stringRotation(self, word, rot):
        #handle if the rotation length is greater than the word
        while rot > len(word):
            rot -= len(word)
        newWord = word[-rot:] + word[:-rot]
        return newWord

    def aboveBelow(self):
        print('The list to sort is: ' + str(self.array))
        print('The comparison number is: ' + str(self.comp))
        ab = 0
        be = 0
        for num in self.array:
            if num > self.comp:
                ab += 1
            elif num < self.comp:
                be += 1
        return {'above': ab, 'below': be}

def main():
    test = RTSTest()
    print(test.name)
    
    print(test.aboveBelow())
    print()
    print('Enter \'exit\' as the word to rotate to quit')
    print('what word should we rotate?')
    word = input()
    while word.lower() != 'exit':
        print('how many letters?')
        number = int(input())
        while number <= 0:
            print('Try a positive integer')
            number = int(input())
        print(test.stringRotation(word, number))
        print('what word should we rotate?')
        word = input()



main()
