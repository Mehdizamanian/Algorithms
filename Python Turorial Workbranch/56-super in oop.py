class A:

    def message(self):
        print('hello')


class B(A):
    def message(self):
        print('hi')
    
    # we use super in another standard method to get overwrite method back by looking at parrent same method
    def message_edited(self):
        super().message()


c=B()
c.message()
c.message_edited()
