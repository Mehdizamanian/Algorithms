

class Members  :
    def __init__(self, name , age , team , injurred ):
        self.name=name
        self.age=age
        self.team=team
        self.injurred = injurred

    def get_status ( self ):
     print(
         "name :" + self.name+"\n"+
         "age :" + self.age + "\n" +
         "team :" + self.team + "\n" +
         "injurred :" + self.injurred
     )


class Player(Members):

    def get_status(self):
        print(
            "Player name :" + self.name + "\n" +
            "Player age :" + self.age + "\n" +
            "Player team :" + self.team + "\n" +
            "Player injurred :" + self.injurred
        )


class Coach ( Members ) :

    def get_status ( self ):
     print(
         "Coach name :" + self.name+"\n"+
         "Coach age :" + self.age + "\n" +
         "Coach team :" + self.team + "\n" +
         "Coach injurred :" + self.injurred
     )


