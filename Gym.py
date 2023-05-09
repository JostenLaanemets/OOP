class Trainers:
    def __init__(self,stamina:int,color:str):
        self.stamina=stamina
        self.color=color
    def __repr__(self) -> str:
        return f'Trainers: [{self.stamina}, {self.color}]'

class Member:
    def __init__(self,name:str,age:int,trainers:Trainers):
        self.name=name
        self.age=age
        self.trainers=trainers
        self.gyms=[]
        
    def __repr__(self) -> str:
        return f'[{self.name}], [{self.age}]: [{self.trainers}]'
    
    def get_gyms(self)->list:
        return [x.name for x in self.gyms]
        
class Gym:
    def __init__(self,name:str,max_members_number: int):
        self.name=name   
             
        if max_members_number>=1:
            self.max_members_number= max_members_number
        self.gym_reg=[]
        self.stamina=[]

    def __repr__(self) -> str:
        return f'Gym [{self.name}] : [{self.get_members_number()}]'
        

    def add_member(self,member:Member)-> Member:
        if self.can_add_member(member) and\
            (member.trainers.color !='') and\
            member.trainers.stamina>=0 and\
            member not in self.gym_reg:
            if (len(self.gym_reg)+1)>self.max_members_number:
                lowest_stamina = min([x.trainers.stamina for x in self.gym_reg ])
                [self.gym_reg.remove(x) for x in self.gym_reg if x.trainers.stamina==lowest_stamina]
                self.gym_reg.append(member)
                member.gyms.append(self)
                self.stamina.append(member.trainers.stamina)
                return member
            else:
                self.gym_reg.append(member)
                member.gyms.append(self)
                self.stamina.append(member.trainers.stamina)
                return member
        return None
                
                    
    
    def can_add_member(self,member:Member):
        return isinstance(member,Member)
    
    def remove_member(self,member:Member):
        self.gym_reg.remove(member)

    def get_total_stamina(self)->int:
        total_stamina=0
        for member in self.gym_reg: 
            total_stamina= total_stamina+member.trainers.stamina
        return total_stamina
    def get_members_number(self):
        number=0
        for x in self.gym_reg:
            number+=1
        return number

    def get_all_members(self):
        return self.gym_reg       
                    
    def get_average_age(self)->float:
        total_age=0
        for member in self.gym_reg:
            total_age=total_age+member.age
        return round(total_age/len(self.gym_reg),2)
            

class City:
    def __init__(self,max_gym_number:int):
        self.gyms=[]
        self.max_gym_number= max_gym_number

    def build_gym(self, gym : Gym)->Gym:
        if self.can_build_gym(gym) and isinstance(gym, Gym):
            self.gyms.append(gym)
            return gym
            
    def can_build_gym(self,gym)->bool:
        return len(self.gyms)<=self.max_gym_number and gym not in self.gyms
        
    def destroy_gym(self):
        return [self.gyms.remove(x) for x in self.gyms if x.get_members_number() == min([x.get_members_number() for x in self.gyms])]
        
    def get_max_members_gym(self)->list:
        return [x.name for x in self.gyms if x.get_members_number() == max([x.get_members_number() for x in self.gyms])]

    def get_max_stamina_gyms(self) -> list:
        return [x.name for x in self.gyms if x.get_total_stamina() == max([x.get_total_stamina() for x in self.gyms ])]
    
    def get_max_average_ages(self) -> list:
        return [x.name for x in self.gyms if max([x.get_average_age() for x in self.gyms]) == x.get_average_age()]
    
    def get_min_average_ages(self) -> list:
        return [x.name for x in self.gyms if min([x.get_average_age() for x in self.gyms]) == x.get_average_age()]

    def get_gyms_by_trainers_color(self, color: str) -> list:
        Gyms_with_trainers_color=[gyms.name for gyms in self.gyms for x in gyms.gym_reg if x.trainers.color == color ]
        gym_name = {}
        for name in Gyms_with_trainers_color:
            if name in gym_name:
                gym_name[name] += 1
            else:
                gym_name[name] = 1
        return sorted(set(Gyms_with_trainers_color), key=lambda x: gym_name[x], reverse=True)
        
    def get_gyms_by_name(self, name: str) -> list:
        Gyms_with_given_name=[gyms.name for gyms in self.gyms for x in gyms.gym_reg if x.name == name ]
        gym_name = {}
        for name in Gyms_with_given_name:
            if name in gym_name:
                gym_name[name] += 1
            else:
                gym_name[name] = 1
        return sorted(set(Gyms_with_given_name), key=lambda x: gym_name[x], reverse=True)

    def get_all_gyms(self) -> list:
        return [x.name for x in self.gyms]










