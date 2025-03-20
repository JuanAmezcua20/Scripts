import shutil
import os

# Define your folder paths
source_weapons_folder = "C:\\Users\\Juan\\Documents\\METABRAWL\\NFTs season 1\\Weapons\\"
source_characters_folder = "C:\\Users\\Juan\\Documents\\METABRAWL\\NFTs season 1\\Characters\\"
destination_folder = "C:\\Users\\Juan\\Documents\\METABRAWL\\NFTs season 1\\1000 Exclusive Collection\\"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Get the weapon and character images
weapons = [f for f in os.listdir(source_weapons_folder) if f.endswith(".png")]
characters = [f for f in os.listdir(source_characters_folder) if f.endswith(".png")]

# Check if files are available
if len(weapons) < 1:
    raise ValueError("The source weapons folder must contain at least 1 PNG file!")
if len(characters) < 1:
    raise ValueError("The source characters folder must contain at least 1 PNG file!")

# Start adding from file 397
file_number = 397
weapon_index = 0
character_index = 0

while file_number <= 1000:  # Generate files up to 1,000
    # Add 25 weapons
    for _ in range(25):
        if file_number > 1000:  # Stop if we've reached 1,000 files
            break

        # Cycle through weapons
        weapon = weapons[weapon_index % len(weapons)]
        new_file_name = f"{file_number}.png"
        shutil.copy(os.path.join(source_weapons_folder, weapon), os.path.join(destination_folder, new_file_name))
        file_number += 1
        weapon_index += 1

    if file_number > 1000:  # Stop if we've already reached 1,000 files
        break

    # Add 1 character after every 25 weapons
    character = characters[character_index % len(characters)]
    new_file_name = f"{file_number}.png"
    shutil.copy(os.path.join(source_characters_folder, character), os.path.join(destination_folder, new_file_name))
    file_number += 1
    character_index += 1  # Move to the next character

print(f"Adding weapon file: {weapon}")
print(f"Adding character file: {character}")
