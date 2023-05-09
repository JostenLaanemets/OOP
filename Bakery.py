from typing import Optional

class Pastry:
    def __init__(self, name: str, complexity_level: int) -> None:
        self.name=name
        self.complexity_level=complexity_level
    def __repr__(self) -> str:
        return f'{self.name}'

class Baker:
    def __init__(self, name: str, experience_level: int, money: int):
        self.name=name
        self.experience_level=experience_level
        self.money=money
    def __str__(self) -> str:
        return f'Baker: {self.__name}({self.experience_level})'

    def __repr__(self) -> str:
        return self.__str__()


class Backery:


    def __init__(self, name:str , min_experience_level: int, budget: int):
        self.name=name
        self.min_experience_level=min_experience_level
        self.budget=budget
        self.all_bakers=[]
        self.all_recipes={}
        self.all_pastries=[]
        
    
    def add_baker(self, baker: Baker)->Optional[Baker]:
        if isinstance(baker, Baker) and (baker.experience_level >= self.min_experience_level):
            self.all_bakers.append(baker.name)

            return baker
        else:
            return None
        
    def add_recipe(self,name:str):
        if (self.budget-len(name)>=0) and (name not in self.all_recipes) and (len(self.all_bakers)!=0):
            self.budget-=len(name)
            #complexity_level = abs(len(name) * len(self.get_bakers()) - min([baker.experience_level for baker in self.all_bakers]))
            self.all_recipes[name]='complexity_level'


    def make_order(self,name:str)->'Pastry':
        pastry_complexity_lvl=self.all_recipes.keys()
        if name in self.get_recipes():
            eligable_baker =[baker for baker in self.all_bakers if baker.experience_level >= Pastry.complexity_level]
            return eligable_baker
            #chosen_baker=min(eligable_baker,key=lambda x: x.experience_level - pastry_complexity_lvl)
            


    def get_recipes(self):
        return self.all_recipes
    
    def get_bakers(self):
        return self.all_bakers
        
    def get_pastries(self):
        return self.pastries
    
    def remove_baker(self,baker:Baker):
        if baker in self.all_bakers:
            self.all_bakers.remove(baker)
        


BKRY=Backery('B',40,4000)
x= Baker('pablo',50,0)
BKRY.add_baker(x)
print(BKRY.get_bakers())
BKRY.add_recipe('Burgir')
print(BKRY.get_recipes())
BKRY.make_order('Burgir')

'LIST COMPREHENSION'
'double loop'