'''
To hide the internal functionalities we have to use abstraction
'''

from abc import ABC,abstractmethod
class InstaBackend(ABC):

    @abstractmethod
    def story(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def reels(self):
        pass

    @abstractmethod
    def profile(self):
        pass
    

class InstaFrontend(InstaBackend):
    def story(self):
        print('Display Story')

    def post(self):
        print('Display Post')

    def reels(self):
        print('Display Reels')

    def profile(self):
        print('Display Profile')

user=InstaFrontend()
user.story()
user.reels()

'''
user1=InstaBackend()
user1.story()      #can't access beacuse we have hidden the internal functionalities
'''

    
