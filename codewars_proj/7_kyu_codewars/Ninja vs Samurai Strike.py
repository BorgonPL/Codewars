class Warrior:
    def __init__(self,name):
        self.name=name
        self.health=100
        
    def strike(self,enemy,swings):
        enemy.health=(max([-1,enemy.health-(swings*10)]) if max([-1,enemy.health-(swings*10)])>=0 else 0)