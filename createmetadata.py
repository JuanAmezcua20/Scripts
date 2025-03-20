import json
import os

# Number of metadata files to generate
total_files = 1000

# Base template
metadata_template = {
    "name": "",
    "description": "",
    "external_url": "",
    "image": "",
    "attributes": [
        {
            "trait_type": "Type",
            "value": ""
        }
    ],
    "properties": {
        "files": [
            {
                "uri": "",
                "type": ""
            }
        ],
        "category": "",
        "creators": []
    },
    "compiler": "Metadata Generator v1.0"
}

# Your BaseURI
base_uri = "https://metabrawl.mypinata.cloud/ipfs/bafybeic3vmi6tkl5b67au5oukbvyobgcmm3prrtqmccjs2v5wcwlg32wue/"

# Output folder path
output_folder = "C:/Users/Juan/Documents/METABRAWL/NFTs season 1/metadata/"
os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists

# Specific indices for 'character' type NFTs
specific_indices = {25, 26, 51, 73}  # Add other specific "character" indices as needed

# Generate metadata files
for i in range(1, total_files + 1):
    # Copy the base template
    metadata = metadata_template.copy()

    # Assign values
    metadata["name"] = f"NFT #{i}"
    metadata["description"] = f"This is metadata for NFT #{i}."
    metadata["image"] = f"{base_uri}{i}.png"
    metadata["attributes"][0]["value"] = "character" if i % 25 == 0 or i in specific_indices else "weapon"

    # Save JSON file
    with open(f"{output_folder}{i}.json", "w") as f:
        json.dump(metadata, f, indent=4)

print("Metadata files generated successfully!")
