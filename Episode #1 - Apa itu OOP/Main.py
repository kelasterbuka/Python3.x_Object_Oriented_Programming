class Hero: # template
    pass


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero();

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)