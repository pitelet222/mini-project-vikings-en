import sys
import time
import random
import math

# Import the updated vikingsClasses
sys.path.append(r'c:\Users\Monitor 16\pite_py_projects\mini-project-vikings-en')
exec(open(r"c:\Users\Monitor 16\pite_py_projects\mini-project-vikings-en\vikingsClasses copy 2.py", encoding='utf-8', errors='ignore').read())

class BattleSimulator:
    def __init__(self):
        self.war = None
        self.battle_stats = {
            'turns': 0,
            'total_kills': 0,
            'viking_kills': 0,
            'saxon_kills': 0,
            'start_time': 0,
            'battle_duration': 0
        }
        
    def create_balanced_armies(self, army_size=1000):
        """Crea ejércitos balanceados con estadísticas correctas"""
        print("🏗️ Creando ejércitos balanceados...")
        
        self.war = War()
        
        # Crear ejército vikingo con distribución balanceada
        print(f"⚔️ Generando {army_size} vikingos...")
        for i in range(army_size):
            pos_x = random.randint(50, 400)
            pos_y = random.randint(200, 600)
            
            unit_type = random.randint(1, 100)
            if unit_type <= 50:  # 50% vikingos regulares
                viking = Viking(f"Viking_{i}", 
                              Viking.BASE_HEALTH,      
                              Viking.BASE_STRENGTH,      
                              Viking.BASE_MOVEMENT,    
                              Viking.BASE_SHIELD,      
                              Viking.BASE_RANGE,       
                              Viking.BASE_ATCK_SPEED,  
                              Viking.BASE_CRITICAL_HIT, 
                              pos_x, pos_y)
            elif unit_type <= 70:  # 20% berserkers
                viking = berserk(f"Berserk_{i}",
                               berserk.BASE_HEALTH,      
                               berserk.BASE_STRENGTH,    
                               berserk.BASE_MOVEMENT,    
                               berserk.BASE_SHIELD,      
                               berserk.BASE_RANGE,       
                               berserk.BASE_ATCK_SPEED,  
                               berserk.BASE_CRITICAL_HIT, 
                               pos_x, pos_y)
            elif unit_type <= 85:  # 15% skjadmlaer
                viking = skjadmlaer(f"Skjadmlaer_{i}",
                                  skjadmlaer.BASE_HEALTH,      
                                  skjadmlaer.BASE_STRENGTH,    
                                  skjadmlaer.BASE_MOVEMENT,    
                                  skjadmlaer.BASE_SHIELD,      
                                  skjadmlaer.BASE_RANGE,       
                                  skjadmlaer.BASE_ATCK_SPEED,  
                                  skjadmlaer.BASE_CRITICAL_HIT, 
                                  pos_x, pos_y)
            else:  # 15% ulfhednar
                viking = ulfhednar(f"Ulfhednar_{i}",
                                 ulfhednar.BASE_HEALTH,      
                                 ulfhednar.BASE_STRENGTH,    
                                 ulfhednar.BASE_MOVEMENT,    
                                 ulfhednar.BASE_SHIELD,      
                                 ulfhednar.BASE_RANGE,       
                                 ulfhednar.BASE_ATCK_SPEED,  
                                 ulfhednar.BASE_CRITICAL_HIT, 
                                 pos_x, pos_y)
            
            self.war.vikingArmy.append(viking)
        
        # Crear ejército sajón con distribución balanceada
        print(f"🛡️ Generando {army_size} sajones...")
        for i in range(army_size):
            pos_x = random.randint(600, 950)
            pos_y = random.randint(200, 600)
            
            unit_type = random.randint(1, 100)
            if unit_type <= 50:  # 50% sajones regulares
                saxon = Saxon(Saxon.BASE_HEALTH,      
                            Saxon.BASE_STRENGTH,    
                            Saxon.BASE_MOVEMENT,    
                            Saxon.BASE_SHIELD,      
                            Saxon.BASE_RANGE,       
                            Saxon.BASE_ATCK_SPEED,  
                            Saxon.BASE_CRITICAL_HIT, 
                            pos_x, pos_y)
            elif unit_type <= 70:  # 20% soldados de lanza
                saxon = spear_soldier(spear_soldier.BASE_HEALTH,      
                                    spear_soldier.BASE_STRENGTH,    
                                    spear_soldier.BASE_MOVEMENT,    
                                    spear_soldier.BASE_SHIELD,      
                                    spear_soldier.BASE_RANGE,       
                                    spear_soldier.BASE_ATCK_SPEED,  
                                    spear_soldier.BASE_CRITICAL_HIT, 
                                    pos_x, pos_y)
            elif unit_type <= 85:  # 15% arqueros
                saxon = archer(archer.BASE_HEALTH,      
                             archer.BASE_STRENGTH,    
                             archer.BASE_MOVEMENT,    
                             archer.BASE_SHIELD,      
                             archer.BASE_RANGE,       
                             archer.BASE_ATCK_SPEED,  
                             archer.BASE_CRITICAL_HIT, 
                             pos_x, pos_y)
            else:  # 15% asesinos
                saxon = assasin(assasin.BASE_HEALTH,      
                              assasin.BASE_STRENGTH,    
                              assasin.BASE_MOVEMENT,    
                              assasin.BASE_SHIELD,      
                              assasin.BASE_RANGE,       
                              assasin.BASE_ATCK_SPEED,  
                              assasin.BASE_CRITICAL_HIT, 
                              pos_x, pos_y)
            
            self.war.saxonArmy.append(saxon)
        
        print(f"✅ Ejércitos creados: {len(self.war.vikingArmy)} vikingos vs {len(self.war.saxonArmy)} sajones")
        return self.war
    
    def analyze_army_composition(self):
        """Analiza la composición de los ejércitos"""
        print("\n📊 ANÁLISIS DE COMPOSICIÓN DE EJÉRCITOS")
        print("=" * 60)
        
        # Analizar vikingos
        viking_types = {'Viking': 0, 'berserk': 0, 'skjadmlaer': 0, 'ulfhednar': 0}
        for viking in self.war.vikingArmy:
            viking_types[type(viking).__name__] += 1
        
        print("⚔️ EJÉRCITO VIKINGO:")
        for unit_type, count in viking_types.items():
            percentage = (count / len(self.war.vikingArmy)) * 100
            print(f"   {unit_type}: {count} unidades ({percentage:.1f}%)")
        
        # Analizar sajones
        saxon_types = {'Saxon': 0, 'spear_soldier': 0, 'archer': 0, 'assasin': 0}
        for saxon in self.war.saxonArmy:
            saxon_types[type(saxon).__name__] += 1
        
        print("\n🛡️ EJÉRCITO SAJÓN:")
        for unit_type, count in saxon_types.items():
            percentage = (count / len(self.war.saxonArmy)) * 100
            print(f"   {unit_type}: {count} unidades ({percentage:.1f}%)")
    
    def show_unit_stats(self):
        """Muestra las estadísticas de ejemplo de cada tipo de unidad"""
        print("\n📋 ESTADÍSTICAS DE UNIDADES")
        print("=" * 60)
        
        # Encontrar ejemplos de cada tipo
        examples = {
            'Viking': None, 'berserk': None, 'skjadmlaer': None, 'ulfhednar': None,
            'Saxon': None, 'spear_soldier': None, 'archer': None, 'assasin': None
        }
        
        for viking in self.war.vikingArmy:
            unit_type = type(viking).__name__
            if examples[unit_type] is None:
                examples[unit_type] = viking
        
        for saxon in self.war.saxonArmy:
            unit_type = type(saxon).__name__
            if examples[unit_type] is None:
                examples[unit_type] = saxon
        
        print("⚔️ UNIDADES VIKINGAS:")
        for unit_type in ['Viking', 'berserk', 'skjadmlaer', 'ulfhednar']:
            unit = examples[unit_type]
            if unit:
                print(f"   {unit_type}: HP={unit.health}, STR={unit.strength}, "
                      f"MOV={unit.movement}, SHIELD={unit.shield}, RNG={unit.range}, "
                      f"SPD={unit.atck_speed}, CRIT={unit.crit}")
        
        print("\n🛡️ UNIDADES SAJONAS:")
        for unit_type in ['Saxon', 'spear_soldier', 'archer', 'assasin']:
            unit = examples[unit_type]
            if unit:
                print(f"   {unit_type}: HP={unit.health}, STR={unit.strength}, "
                      f"MOV={unit.movement}, SHIELD={unit.shield}, RNG={unit.range}, "
                      f"SPD={unit.atck_speed}, CRIT={unit.crit}")
    
    def process_combat_turn(self):
        """Procesa un turno completo de combate"""
        turn_kills = 0
        actions_per_turn = min(200, len(self.war.vikingArmy), len(self.war.saxonArmy))
        
        # Fase vikinga
        for _ in range(min(actions_per_turn, len(self.war.vikingArmy))):
            if not self.war.vikingArmy or not self.war.saxonArmy:
                break
                
            viking = random.choice(self.war.vikingArmy)
            
            # Buscar objetivos en rango
            targets_in_range = [s for s in self.war.saxonArmy if viking.can_attack(s)]
            
            if targets_in_range:
                target = random.choice(targets_in_range)
                damage = viking.attack(target)
                if damage > 0:
                    target.receiveDamage(damage)
                    if target.health <= 0:
                        self.war.saxonArmy.remove(target)
                        turn_kills += 1
                        self.battle_stats['total_kills'] += 1
                        self.battle_stats['viking_kills'] += 1
            else:
                # Mover hacia el enemigo más cercano
                if self.war.saxonArmy:
                    viking.move_to_enemy(self.war.saxonArmy)
        
        # Fase sajona
        for _ in range(min(actions_per_turn, len(self.war.saxonArmy))):
            if not self.war.saxonArmy or not self.war.vikingArmy:
                break
                
            saxon = random.choice(self.war.saxonArmy)
            
            # Buscar objetivos en rango
            targets_in_range = [v for v in self.war.vikingArmy if saxon.can_attack(v)]
            
            if targets_in_range:
                target = random.choice(targets_in_range)
                damage = saxon.attack(target)
                if damage > 0:
                    target.receiveDamage(damage)
                    if target.health <= 0:
                        self.war.vikingArmy.remove(target)
                        turn_kills += 1
                        self.battle_stats['total_kills'] += 1
                        self.battle_stats['saxon_kills'] += 1
            else:
                # Mover hacia el enemigo más cercano
                if self.war.vikingArmy:
                    saxon.move_to_enemy(self.war.vikingArmy)
        
        return turn_kills
    
    def run_battle_simulation(self, army_size=1000, max_turns=500, verbose=True):
        """Ejecuta la simulación completa de batalla"""
        print("🏰" * 25)
        print("🏰        SIMULADOR DE BATALLA VIKINGOS vs SAJONES        🏰")
        print("🏰" * 25)
        
        # Crear ejércitos
        self.create_balanced_armies(army_size)
        
        # Mostrar análisis inicial
        if verbose:
            self.analyze_army_composition()
            self.show_unit_stats()
        
        # Configurar estadísticas de batalla
        initial_vikings = len(self.war.vikingArmy)
        initial_saxons = len(self.war.saxonArmy)
        self.battle_stats['start_time'] = time.time()
        
        print(f"\n⚔️ ¡COMIENZA LA BATALLA! ⚔️")
        print("=" * 60)
        print(f"Vikingos: {initial_vikings:,} | Sajones: {initial_saxons:,}")
        
        # Bucle principal de batalla
        while (len(self.war.vikingArmy) > 0 and len(self.war.saxonArmy) > 0 and 
               self.battle_stats['turns'] < max_turns):
            
            self.battle_stats['turns'] += 1
            turn_kills = self.process_combat_turn()
            
            # Mostrar progreso cada 10 turnos
            if verbose and self.battle_stats['turns'] % 10 == 0:
                battle_time = time.time() - self.battle_stats['start_time']
                vikings_left = len(self.war.vikingArmy)
                saxons_left = len(self.war.saxonArmy)
                total_casualties = (initial_vikings + initial_saxons) - (vikings_left + saxons_left)
                
                print(f"Turno {self.battle_stats['turns']:3d}: "
                      f"Vikingos {vikings_left:4d} | Sajones {saxons_left:4d} | "
                      f"Bajas: {total_casualties:4d} | Tiempo: {battle_time:.1f}s")
                
                if turn_kills >= 50:
                    print("        💥💥💥 ¡MASACRE ABSOLUTA!")
                elif turn_kills >= 20:
                    print("        💥💥 ¡Combate brutal!")
                elif turn_kills >= 10:
                    print("        💥 Lucha intensa")
                elif turn_kills > 0:
                    print("        ⚔️ Intercambio de golpes")
        
        # Calcular resultados finales
        self.battle_stats['battle_duration'] = time.time() - self.battle_stats['start_time']
        self.display_battle_results(initial_vikings, initial_saxons)
        
        return self.war, self.battle_stats
    
    def display_battle_results(self, initial_vikings, initial_saxons):
        """Muestra los resultados finales de la batalla"""
        final_vikings = len(self.war.vikingArmy)
        final_saxons = len(self.war.saxonArmy)
        
        print("\n" + "🏆" * 60)
        print("🏆                    RESULTADOS DE LA BATALLA                    🏆")
        print("🏆" + "=" * 58 + "🏆")
        
        # Determinar ganador
        if final_vikings > final_saxons:
            winner = "VIKINGOS"
            print("🎉 ¡VICTORIA VIKINGA! ¡Por Odín y el Valhalla! 🎉")
        elif final_saxons > final_vikings:
            winner = "SAJONES"
            print("🎉 ¡VICTORIA SAJONA! ¡La defensa ha prevalecido! 🎉")
        else:
            winner = "EMPATE"
            print("⚔️ ¡EMPATE! Ambos ejércitos lucharon valientemente ⚔️")
        
        # Estadísticas detalladas
        viking_casualties = initial_vikings - final_vikings
        saxon_casualties = initial_saxons - final_saxons
        total_casualties = viking_casualties + saxon_casualties
        
        print(f"\n📊 ESTADÍSTICAS DE BATALLA:")
        print(f"   Duración: {self.battle_stats['turns']} turnos ({self.battle_stats['battle_duration']:.1f} segundos)")
        print(f"   Bajas totales: {total_casualties:,} ({(total_casualties/(initial_vikings + initial_saxons)*100):.1f}%)")
        print(f"   Ritmo de bajas: {self.battle_stats['total_kills']/self.battle_stats['turns']:.1f} por turno")
        print(f"   Eficiencia: {(initial_vikings + initial_saxons)/self.battle_stats['battle_duration']:.0f} unidades procesadas/segundo")
        
        print(f"\n⚔️ RESULTADOS VIKINGOS:")
        print(f"   Inicial: {initial_vikings:,} → Final: {final_vikings:,} → Bajas: {viking_casualties:,} ({(viking_casualties/initial_vikings*100):.1f}%)")
        print(f"   Enemigos eliminados: {self.battle_stats['viking_kills']:,}")
        
        print(f"\n🛡️ RESULTADOS SAJONES:")
        print(f"   Inicial: {initial_saxons:,} → Final: {final_saxons:,} → Bajas: {saxon_casualties:,} ({(saxon_casualties/initial_saxons*100):.1f}%)")
        print(f"   Enemigos eliminados: {self.battle_stats['saxon_kills']:,}")
        
        # Mostrar supervivientes destacados
        if final_vikings > 0:
            print(f"\n🏆 HÉROES VIKINGOS SUPERVIVIENTES:")
            for i, hero in enumerate(self.war.vikingArmy[:5]):
                unit_type = type(hero).__name__
                print(f"   {hero.name} ({unit_type}): HP={hero.health:.0f}, STR={hero.strength}")
        
        if final_saxons > 0:
            print(f"\n🛡️ HÉROES SAJONES SUPERVIVIENTES:")
            for i, hero in enumerate(self.war.saxonArmy[:5]):
                unit_type = type(hero).__name__
                name = getattr(hero, 'name', f'Saxon_Hero_{i+1}')
                print(f"   {name} ({unit_type}): HP={hero.health:.0f}, STR={hero.strength}")
        
        print(f"\n🎬 ¡BATALLA COMPLETADA! Ganador: {winner} 🎬")
        print("🏆" * 60)

def main():
    """Función principal para ejecutar el simulador"""
    simulator = BattleSimulator()
    
    print("Bienvenido al Simulador de Batallas Vikingos vs Sajones!")
    print("Este simulador usa las estadísticas actualizadas de tus clases.")
    
    # Configuración de batalla
    try:
        army_size = int(input("\nTamaño de ejército (por defecto 1000): ") or "1000")
        max_turns = int(input("Máximo de turnos (por defecto 500): ") or "500")
        verbose = input("¿Mostrar detalles? (s/n, por defecto s): ").lower() != 'n'
    except ValueError:
        print("Usando valores por defecto...")
        army_size = 1000
        max_turns = 500
        verbose = True
    
    # Ejecutar simulación
    war_result, stats = simulator.run_battle_simulation(army_size, max_turns, verbose)
    
    # Opción para batalla rápida adicional
    while True:
        another = input("\n¿Ejecutar otra batalla? (s/n): ").lower()
        if another == 's':
            simulator = BattleSimulator()
            simulator.run_battle_simulation(army_size, max_turns, verbose)
        else:
            break
    
    print("\n¡Gracias por usar el Simulador de Batallas!")

if __name__ == "__main__":
    main()