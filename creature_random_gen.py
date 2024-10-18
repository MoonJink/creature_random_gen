# -----------------------------
# IMPORTS
# -----------------------------
import random

# -----------------------------
# SUBPROGRAMS
# -----------------------------

def species_type():
    species_type_array = [
        "Cursed",
        "Transformed",
        "Divine",
        "Monster",
        "Beast"
    ]
    species_type = random.choice(species_type_array)
    if species_type == "Divine":
        divine_type_array = [
            " (plucked)",
            " (bowed)",
            " (woodwind)",
            " (brass)",
            " (chimes)",
            " (bell)"
        ]
        divine_type_choice = random.choice(divine_type_array)
        species_type += divine_type_choice
    return species_type

def environment():
    environment_array = [
        "Aquatic",
        "Semi-Aquatic",
        "Land",
        "Flying"
    ]
    return random.choice(environment_array)

def country():
    country_array = [
        "Silva",
        "Yever",
        "Ashborne",
        "TROK",
        "Breunswick",
        "Thornsdale",
        "Wranbourne",
        "Sanguis (UPPER)",
        "Sanguis (LOWER)",
        "Formellond",
        "Imperium",
        "Lindow Tribes",
        "Volcano",
        "Libertas",
        "South Libertas",
        "Vindium",
        "Aranae",
        "Whimsy",
    ]
    chosen_country = random.choice(country_array)

    match chosen_country:
        case "Sanguis (UPPER)" | "Sanguis (LOWER)":
            sanguis_sub_biome = [
                " (cold)",
                " (taiga)",
                " (tundra)"
            ]
            chosen_sub_biome = random.choice(sanguis_sub_biome)
            chosen_country = chosen_country + chosen_sub_biome
            return chosen_country
        case "Ashborne":
            ashborne_sub_biome = [
                " (desert)",
                " (savanna)"
            ]
            chosen_sub_biome = random.choice(ashborne_sub_biome)
            chosen_country = chosen_country + chosen_sub_biome
            return chosen_country
        case "Silva":
            silva_sub_biome = [
                " (greater island)",
                " (unknown island)",
                " (lesser island)"
            ]
            chosen_sub_biome = random.choice(silva_sub_biome)
            chosen_country = chosen_country + chosen_sub_biome
            return chosen_country
        case _:
            return chosen_country

def aggression():
    aggression_array = [
        "Low",
        "Medium",
        "High"
    ]
    return random.choice(aggression_array)

def danger():
    danger_array = [
        "Low",
        "Medium",
        "High"
    ]
    return random.choice(danger_array)

def diet():
    diet_array = [
        "Carnivore",
        "Herbivore",
        "Omnivore",
        "Other"
    ]
    return random.choice(diet_array)

# -----------------------------
# MAIN
# -----------------------------
def main():
    print(f"\n'{species_type()}' from '{country()}' in a '{environment()}' habitat with aggression level '{aggression()}' and danger level '{danger()}'. Its diet is '{diet()}'.")
main()