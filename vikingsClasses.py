import random

# Soldier


class Soldier:

    ## Define the properties on the constructor
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    ## Return the strenght of the soldier
    
    def attack(self):
        return self.strength
        
    ## We don't need to return anything, we just susbtract the damage from the health
    
    def receiveDamage(self, damage):
        self.health -= damage

    

# Viking

class Viking(Soldier):
    
    ## We define viking's properties as the constructor
    
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    ## Define battlecry, don't take any arguments and just return a string
    
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
            

# Saxon

class Saxon(Soldier):
    
    ## We define saxon's constructor, saxons has no names
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    ## We define saxon's properties
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
# Davicente

class War():
    
    ## The war constructor sholdn't recieve any arguments, we create the army of both sides
    
    def __init__(self):
       self.VikingArmy = []
       self.SaxonArmy = []

    ## We append the new viking to the Viking Army 

    def addViking(self, viking):
        self.VikingArmy.append(viking)

    ## We append the new saxon to the Saxon Army
    
    def addSaxon(self, saxon):
        self.SaxonArmy.append(saxon)
    
    ## We return the saxon's missing health from the vikings attack
    
    def vikingAttack(self):
        viking = random.randrange(len(self.VikingArmy))
        saxon = random.randrange(len(self.SaxonArmy))
        
        result1 = saxon.self.recieveDamage(self, viking.strength)
        
        if saxon.health <= 0:
            self.SaxonArmy.delete(saxon)
        
        return result1
        
    ## We return viking's missing health fromn the saxon's attack
    
    def saxonAttack(self):
        viking = random.randrange(len(self.VikingArmy))
        saxon = random.randrange(len(self.SaxonArmy))
        
        result2 = viking.self.recieveDamage(self, saxon.strength)
        
        if viking.health <= 0:
            self.VikingArmy.delete(viking)
        
        return result2
    

    def showStatus(self):
        if len(self.VikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        
        elif len(self.SaxonArmy) == 0:
            return f"Vikings have won the war of the century!"
            
        elif len(self.VikingArmy) >= 1 and len(self.SaxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

