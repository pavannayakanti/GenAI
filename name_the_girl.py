import os

# List of 100 Indian female names
names = [
    "Aadhya", "Aaradhya", "Aarohi", "Aarya", "Abha", "Aditi", "Aishwarya", "Akanksha", "Alisha", "Amisha",
    "Amrita", "Ananya", "Anika", "Anita", "Anjali", "Ankita", "Anushka", "Anvi", "Anya", "Aradhana",
    "Archana", "Arpita", "Aruna", "Arya", "Asha", "Asmita", "Avani", "Bela", "Bhavna", "Bhavya",
    "Bhoomi", "Chandni", "Chhavi", "Chitra", "Damini", "Deepa", "Deepika", "Devika", "Diksha", "Divya",
    "Drishti", "Durga", "Eesha", "Esha", "Farah", "Gayatri", "Gauri", "Geeta", "Harini", "Heena",
    "Hema", "Isha", "Ishita", "Jaya", "Jyoti", "Kajal", "Kalyani", "Kamala", "Kanchan", "Karishma",
    "Kavita", "Keerthi", "Khushi", "Kirti", "Komal", "Krishna", "Kritika", "Lakshmi", "Lata", "Lavanya",
    "Leela", "Lina", "Lisha", "Madhavi", "Madhuri", "Malini", "Manisha", "Meera", "Megha", "Mira",
    "Mitali", "Mohana", "Namrata", "Nandini", "Nisha", "Nitya", "Pallavi", "Pari", "Parineeti", "Pooja",
    "Pragya", "Pratibha", "Preeti", "Priya", "Radhika", "Ragini", "Raina", "Rajeshwari", "Rani", "Rekha"
]

# Directory to save the text files
output_dir = "female_names"

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate 100 text files, each with a unique name
for i, name in enumerate(names):
    file_path = os.path.join(output_dir, f"name_{i+1}.txt")
    with open(file_path, "w") as file:
        file.write(name)

print("Generated 100 text files with unique Indian female names.")
