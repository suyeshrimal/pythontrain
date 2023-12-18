from abc import ABC, abstractmethod

class Computer(ABC):
    def run(self,app):
        self.process(app)

    @abstractmethod
    def process(self, app): 
        pass

class Mobile(Computer):
    def process(self, app):
        print("Mobile is running",app)

class laptop(Computer):
    def process(self, app):
        print("laptop is running", app)
samsung=Mobile()
samsung.run("Pubg")
lap=laptop()
lap.run("COC")