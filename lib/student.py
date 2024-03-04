class Student:
    def hello(self):
        return "Hey there! I'm so excited to learn stuff.\n"
        
    def raise_hand(self):
        return 'Pick me!\n'

class ChattyStudent(Student):
    def hello(self):
        return super().hello() + "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        
    def raise_hand(self):
        return super().raise_hand() * 10
        