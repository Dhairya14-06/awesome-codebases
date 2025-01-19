import random

# 1. Define a new array called weapons with 6 different weapon names in increasing strength
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# 2. Roll the dice (1-6) to choose which weapon to use
weaponRoll = random.randint(1, 6)

# 3. Get combat strength with error handling
while True:
    try:
        combat_strength = input("Enter your hero's combat strength: ").strip()
        if not combat_strength:
            raise ValueError("Input cannot be empty.")
        combat_strength = int(combat_strength)
        break
    except ValueError:
        print("Error: Please enter a valid integer for combat strength.")

# 4. Add weaponRoll to hero's combat strength
combat_strength += weaponRoll

# 5. Use the roll as an index to select a weapon and display it
hero_weapon = weapons[weaponRoll - 1]
print(f"Your hero's weapon is: {hero_weapon}")

# 6. Condition checks based on the weapon roll
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

# 7. Additional check if the weapon is not 'Fist'
if hero_weapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")


