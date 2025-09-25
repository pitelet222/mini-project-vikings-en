import random
import time as time
import math
# Soldier


class Soldier:

    BASE_HEALTH = 100
    BASE_STRENGTH = 50
    BASE_MOVEMENT = 3
    BASE_SHIELD = 10
    BASE_RANGE = 1
    BASE_ATCK_SPEED = 1.0
    BASE_CRITICAL_HIT = 1
    
    
    
    ## Define the stats that will be unique to every special soldier unit

    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_x, position_y):
        self.health = health or self.BASE_HEALTH
        self.strength = strength or self.BASE_STRENGTH
        self.shield = shield or self.BASE_SHIELD
        self.movement = movement or self.BASE_MOVEMENT
        self.range = range or self.BASE_RANGE
        self.atck_speed = atck_speed or self.BASE_ATCK_SPEED
        self.last_atck_time = 0
        self.crit = crit or self.BASE_CRITICAL_HIT
        self.position_x = position_x
        self.position_y = position_y

        
        
    ## We define the last attack 

    def can_attack(self, target_unit):
        
        current_time = time.time()
        cooldown = 1.0 / self.atck_speed
        distance = self.calculate_distance(target_unit)
        return ((current_time - self.last_atck_time) >= cooldown) and (distance <= self.range)
        
    def attack(self, target_unit):
        
        if self.can_attack(self, target_unit):
            self.last_atck_time = time.time()
            return self.strength * self.crit
        return 0

    ## We don't need to return anything, we just susbtract the damage from the health

    def receiveDamage(self, damage):

        # first, we use the shield as a extra health bar

        if self.shield > 0:
            if damage <= self.shield:
                self.shield -= damage
                damage = 0
            else:
                damage -= self.shield
                self.shield = 0
                
        # the remaining damage made, is substracted from the health bar
        self.health -= damage
        
    def calculate_distance(self, other_unit):
        
        x_diff = other_unit.position_x - self.position_x
        y_diff = other_unit.position_y - self.position_y
        distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))
        return distance        
        
        
    def move_to_enemy(self, enemy_units):
        if not enemy_units:
            return
        for enemy in enemy_units:
            if not self.can_attack(enemy):
                self.position_y += self.movement

        if self.position_y > 2000:
            self.position_y = 0

    

# These are the regular viking slodiers, they will have the standard stats for vikings

class Viking(Soldier):
    
    BASE_HEALTH = 110
    BASE_STRENGTH = 55
    
    ## We define viking's properties as the constructor
    
    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        self.name = name
        

    ## Define battlecry, don't take any arguments and just return a string
    
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
        
    ## Berserk, higher strength, life and movement speed

class berserk(Viking):
    
    BASE_HEALTH = 110
    BASE_STRENGTH = 70
    BASE_MOVEMENT = 4
    BASE_SHIELD = 5
    
    
    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x):
        super().__init__(name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
    
    ## Skjafmlaer, heavy units, higher shield and less movement
    
class skjadmlaer(Viking):
    
    BASE_SHIELD = 25
    BASE_MOVEMENT = 1
    
    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        super().__init__(name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        
        
    ## Ulfhednar, wolf units, lower health, but lots of attack speed and movement
    
class ulfhednar(Viking):
    
    BASE_HEALTH = 60
    BASE_MOVEMENT = 5
    BASE_ATCK_SPEED = 2
    BASE_RANGE = 0.5
    BASE_CRITICAL_HIT = 1.25

    def __init__(self, name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        super().__init__(name, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        
# Saxon

class Saxon(Soldier):
    
    ## We define saxon's constructor, saxons has no names
    
    def __init__(self, health, strength, movement, shield, range, atck_speed,crit, position_y, position_x):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        
    ## We define saxon's properties
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
        
    ## Spear units, higher attack speed, range and shield, lower strength

class spear_soldier(Saxon):
    
    BASE_STRENGTH = 30
    BASE_RANGE = 2
    BASE_ATCK_SPEED = 1.5
    BASE_SHIELD = 20
    
    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        
    ## Archers, lots of range, lower strength
    
class archer(Saxon):
    
    BASE_STRENGTH = 30
    BASE_RANGE = 12
    BASE_MOVEMENT = 0
    
    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)
        
class assasin(Saxon):
    
    BASE_HEALTH = 70
    BASE_ATCK_SPEED = 1.8
    BASE_RANGE = 0.7
    BASE_CRITICAL_HIT = 1.30
    
    def __init__(self, health, strength, movement, shield, range, atck_speed, crit, position_y, position_x):
        super().__init__(health, strength, movement, shield, range, atck_speed, crit, position_y, position_x)

class War():
    
    ## The war constructor sholdn't recieve any arguments, we create the army of both sides
    
    def __init__(self):  
       self.vikingArmy = []
       self.saxonArmy = []

## We define army generators, first, define the size that we want the special units as well as the regular soldiers (max = 1, so if we wannt 800 out of 1000 the size is 0.8)
## We create loops for each unit, and append it to the army list, each of them with they're own stats, as we want them to have the stats that we already defined, we setthem at None



    def vikings_army_generator(self, size=1000):
        regulars = int(size * 0.80)
        berserk = int(size * 0.05)
        heavys = int(size * 0.10)
        wolfs = int(size * 0.05)
        for i in range(regulars):
            name = f"Viking warrior{i+1}"
            viking = Viking(name, None, None, None, None, None, None, None)
            self.vikingArmy.append(viking)
        for f in range(berserk):
            name = f"Viking berserk {f+1}"
            viking2 = berserk(name, None, None, None, None, None, None, None)
            self.vikingArmy.append(viking2)
        for j in range(heavys):
            name = f"Viking skjadmlaer {j+1}"
            viking3 = skjadmlaer(name, None, None, None, None, None, None, None)
            self.vikingArmy.append(viking3)
        for k in range(wolfs):
            name = f"Viking ulfhednar {k+1}"
            viking4 = ulfhednar(name, None, None, None, None, None, None, None)
            self.vikingArmy.append(viking4)
            
    
    
    
    def saxons_army_generator(self, size=1000):
        regulars = int(size * 0.50)
        spears = int(size * 0.25)
        archers = int(size * 0.15)
        assasins = int(size * 0.10)
        for i in range(regulars):
            saxon = Saxon(None, None, None, None, None, None, None)
            self.saxonArmy.append(saxon)
        for f in range(spears):
            saxon2 = spear_soldier(None, None, None, None, None, None, None)
            self.saxonArmy.append(saxon2)
        for j in range(archers):
            saxon3 = archer(None, None, None, None, None, None, None)
            self.saxonArmy.append(saxon3)
        for k in range(assasins):
            saxon4 = assasin(None, None, None, None, None, None, None)
            self.saxonArmy.append(saxon4)

            
    def massive_army_battle(self, min_size=500, max_size=2000):
        army_size = random.randint(min_size, max_size)

    def move_viking(self):
        for viking in self.vikingArmy:
            viking.move_to_enemy(self.saxonArmy)
            
    def move_saxon(self):
        for saxon in self.saxonArmy:
            saxon.move_to_enemy(self.vikingArmy)
        

    ## We return the saxon's missing health from the vikings attack
    
    def vikingAttack(self):
        if not self.vikingArmy:
            return "No Vikings left alive to fight!!"
        
        if not self.saxonArmy:
            return "No Saxons left to attack!"
        
        viking = random.choice(self.vikingArmy)
        
        targets_in_range = []
        for saxon in self.saxonArmy:
            if viking.can_attack(saxon):
                targets_in_range.append(saxon)

        # If no targets in range, move towards closest enemy
        if not targets_in_range:
            # Find closest saxon with a simple loop
            closest_saxon = self.saxonArmy[0]
            shortest_distance = viking.calculate_distance(closest_saxon)
            
            for saxon in self.saxonArmy:
                distance = viking.calculate_distance(saxon)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_saxon = saxon
            
            viking.move_to_enemy([closest_saxon])
            return f"{viking.name} moved closer to the enemy!"
        
        # Attack a random target in range
        target = random.choice(targets_in_range)
        damage = viking.attack(target)
        result = target.receiveDamage(damage)
        
        if target.health <= 0:
            self.saxonArmy.remove(target)
            
        return result
        
    ## We return viking's missing health fromn the saxon's attack
    
    def saxonAttack(self):
        if not self.saxonArmy:
            return "No Saxons left alive to fight!!"
        
        if not self.vikingArmy:
            return "No Vikings left to attack!"
        
        saxon = random.choice(self.saxonArmy)
        
        targets_in_range = []
        for viking in self.vikingArmy:
            if saxon.can_attack(viking):
                targets_in_range.append(viking)

        # If no targets in range, move towards closest enemy  
        if not targets_in_range:
            # Find closest viking with a simple loop
            closest_viking = self.vikingArmy[0]
            shortest_distance = saxon.calculate_distance(closest_viking)
            
            for viking in self.vikingArmy:
                distance = saxon.calculate_distance(viking)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest_viking = viking
            
            saxon.move_to_enemy([closest_viking])
            return "A Saxon moved closer to the enemy!"
        
        # Attack a random target in range
        target = random.choice(targets_in_range)
        damage = saxon.attack(target)
        result = target.receiveDamage(damage)
        
        if target.health <= 0:
            self.vikingArmy.remove(target)
        
        return result
    

    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
            
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

