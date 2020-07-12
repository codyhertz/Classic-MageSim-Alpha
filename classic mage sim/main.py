import random

spell_power = int(input("Enter your spell power: "))
hit_chance = int(input("Enter you hit rating(please include hit from talents): ")) + 83
frost_fire = int(input("Enter 1 if you are using frost, 2 if you are using fire, 3 if Arcane Frost: "))
toep = input("Are you using TOEP(Y/N)? ")
troll = input("Are you a troll(Y/N)? ")
night_fall = int(input("Nightfall uptime percentage(0-100): "))
curse = input("Curse of Elements(Y/N)? ")
moonkin = input("Do you have a moonkin(Y/N)? ")

if night_fall > 100:
    night_fall = 100
if night_fall < 0:
    night_fall = 0

if moonkin is 'y' or moonkin is 'Y':
    moonkin = 1
else:
    moonkin = 0

if toep is 'y' or toep is 'Y':
    toep = 1
else:
    toep = 0

if curse is 'y' or curse is 'Y':
    curse = 1
else:
    curse = 0

if troll is 'y' or troll is 'Y':
    troll = 1
else:
    troll = 0

if frost_fire < 1 or frost_fire > 3:
    frost_fire = 1
    print("You did not enter a valid spec, so it will be defaulted to frost.")

total_int = int(input("Enter how much int you have: "))
crit_chance = float(input("Enter your crit chance: "))

if frost_fire is 1 or frost_fire is 3:
    crit_chance += 1

full_buffs = input("Do you have full world buffs(Y/N)? ")

extra_int = 0

if full_buffs is 'y' or full_buffs is 'Y':
    crit_chance += 18
    extra_int = total_int * .15 + 40

full_consum = input("Do you have full consumables(Y/N)? ")

if full_consum is 'y' or full_consum is 'Y':
    if frost_fire is 1 or frost_fire is 3:
        spell_power += 200
    else:
        spell_power += 225

crit_chance += extra_int / 59.5

if moonkin is 1:
    crit_chance += 3

x = int(input("Enter number of casts to perform(very large numbers will take a long time, duh): "))

total_damage = 0
toep_cd = 0
toep_casts = 0
beserk_cd = 0
ap_cd = 0
ap_casts = 0
extra_hits = 0
original_spellpower = spell_power
combustion_stacks = 0
combustion_cd = 0
original_crit = crit_chance

for i in range(x):
    hit = 0

    if toep is 1 and toep_cd is 0 and toep_casts is 0:
        toep_casts = 6
        spell_power += 175
    if frost_fire is 3 and ap_cd is 0 and ap_casts is 0:
        ap_casts = 6
    if combustion_cd > 0:
        combustion_cd -= 1

    if random.randint(1, 101) <= hit_chance:
        if frost_fire is 1 or frost_fire is 3:
            if troll is 1 and beserk_cd is 0:
                if random.randint(1, 101) <= hit_chance:
                    extra_hit = random.randint(440, 476) + (.814 * spell_power)

                    if frost_fire is 3:
                        extra_hit *= 1.03
                    if random.randint(0, 101) < night_fall:
                        extra_hit *= 1.15
                    if curse is 1:
                        extra_hit *= 1.1
                    if full_buffs is 'y' or full_buffs is 'Y':
                        extra_hit *= 1.1
                    if frost_fire is 1 or frost_fire is 3:
                        extra_hit *= 1.06

                    if random.randint(1, 10000) <= (crit_chance * 100):
                        extra_hit *= 2

                    if ap_cd is 0:
                        extra_hit *= 1.3

                    # print("Hit for: ", extra_hit)
                    total_damage += extra_hit
                    beserk_cd = 72
                    extra_hit += 1

                    if toep_casts > 0:
                        toep_casts -= 1

                        if toep_casts is 0:
                            toep_cd = 36
                            spell_power = original_spellpower

                    if ap_casts > 0:
                        ap_casts -= 1

                        if ap_casts is 0:
                            ap_cd = 72
                            spell_power = original_spellpower

            hit = random.randint(440, 476) + (.814 * spell_power)
            if toep_casts > 0:
                toep_casts -= 1

                if toep_casts is 0:
                    toep_cd = 36
                    spell_power = original_spellpower

            if ap_casts > 0:
                ap_casts -= 1

                if ap_casts is 0:
                    ap_cd = 72

                    if random.randint(1, 101) <= hit_chance:
                        extra_hit = random.randint(440, 476) + (.814 * spell_power)

                        if frost_fire is 3:
                            extra_hit *= 1.03
                        if random.randint(0, 101) < night_fall:
                            extra_hit *= 1.15
                        if curse is 1:
                            extra_hit *= 1.1
                        if full_buffs is 'y' or full_buffs is 'Y':
                            extra_hit *= 1.1
                        if frost_fire is 1 or frost_fire is 3:
                            extra_hit *= 1.06

                        if random.randint(1, 10000) <= (crit_chance * 100):
                            extra_hit *= 2

                        if ap_cd is 0:
                            extra_hit *= 1.3
                        # print("Hit for: ", extra_hit)
                        total_damage += extra_hit
                        beserk_cd = 72
                        extra_hit += 1

                    spell_power = original_spellpower

            if beserk_cd > 0:
                beserk_cd -= 1
            if toep_cd > 0:
                toep_cd -= 1
            if ap_cd > 0:
                ap_cd -= 1

        else:
            if troll is 1 and beserk_cd is 0:
                if random.randint(1, 101) <= hit_chance:
                    extra_hit = random.randint(596, 761) + spell_power

                    extra_hit *= 1.1
                    if random.randint(0, 101) < night_fall:
                        extra_hit *= 1.15
                    if curse is 1:
                        extra_hit *= 1.1
                    if full_buffs is 'y' or full_buffs is 'Y':
                        extra_hit *= 1.1

                    if random.randint(1, 10000) <= (crit_chance * 100):
                        extra_hit *= 1.5
                        extra_hit *= 1.4
                        if combustion_cd is 0:
                            combustion_stacks += 1

                            if combustion_stacks is 3:
                                crit_chance = original_crit
                                combustion_cd = 60
                    elif combustion_cd is 0:
                        crit_chance += 10

                    # print("Hit for: ", extra_hit)
                    total_damage += extra_hit
                    beserk_cd = 60
                    extra_hits += 1

                    if toep_casts > 0:
                        toep_casts -= 1

                        if toep_casts is 0:
                            toep_cd = 30
                            spell_power -= 175

            hit = random.randint(596, 761) + spell_power

            if toep_casts > 0:
                toep_casts -= 1

                if toep_casts is 0:
                    toep_cd = 30
                    spell_power = original_spellpower

            if beserk_cd > 0:
                beserk_cd -= 1
            if toep_cd > 0:
                toep_cd -= 1

        if frost_fire is 3:
            hit *= 1.03
        if frost_fire is 1 or frost_fire is 3:
            hit *= 1.06
        if frost_fire is 2:
            hit *= 1.1
        if curse is 1:
            hit *= 1.1
        if random.randint(1, 101) < night_fall:
            hit *= 1.15
        if full_buffs is 'y' or full_buffs is 'Y':
            hit *= 1.1
        if random.randint(1, 10000) <= (crit_chance * 100):
            if frost_fire is 1 or frost_fire is 3:
                hit *= 2
            else:
                hit *= 1.5
                hit *= 1.4
                if combustion_stacks is 3:
                    crit_chance = original_crit
                    combustion_cd = 60
                elif combustion_cd is 0:
                    crit_chance += 10
        if ap_cd is 0:
            hit *= 1.3

    if toep_cd > 0:
        toep_cd -= 1

    total_damage += hit

print("")
x += extra_hits
if frost_fire is 1 or frost_fire is 3:
    print("Total damage done: ", total_damage)

    total_damage /= x
    print("Average hit: ", total_damage)

    total_damage /= 2.50
    print('Average DPS: ', total_damage)

else:
    seconds = x * 3
    seconds /= 8
    seconds -= 3
    tick_damage = seconds * 76
    print("Total damage done: ", total_damage + tick_damage)

    total_damage /= x
    print("Average hit: ", total_damage)

    total_damage += tick_damage
    total_damage /= 3
    print('Average DPS: ', total_damage)
