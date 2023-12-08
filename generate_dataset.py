import csv
import random

def generate_age():
    return random.randint(1, 15)

def generate_vaccination_status(severity):
    return random.choices(['Vaccinated', 'Not Vaccinated'], weights=[100 - severity, severity])[0]

def generate_response(severity, values):
    threshold = random.uniform(0.3, 0.6) * 100

    if severity < threshold:
        weights = [0.6, 0.2, 0.2]
    else:
        weights = [0.2, 0.4, 0.4]

    return random.choices(values, weights=weights)[0]

def generate_severity():
    return random.uniform(0, 100)

csv_file_path = 'dog_illness_dataset.csv'

counter = 0

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Age', 'Gender', 'Appetite', 'Activity Level', 'Water Consumption',
                  'Behaviour Changes', 'Breathing Changes', 'Limbs Swelling', 'Vocalization',
                  'Weight Changes', 'Nose Condition', 'Sleep Patterns',
                  'Vaccination Status', 'Severity']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate synthetic data
    for _ in range(300000):  # Adjust the number of rows as needed
        counter += 1
        dog_age = generate_age()
        dog_gender = random.choice(['Male', 'Female'])
        dog_severity = generate_severity()
        dog_vaccination_status = generate_vaccination_status(dog_severity)

        # Generate responses to questions
        responses = {
            'Appetite': generate_response(dog_severity, ['Normal', 'Increased', 'Decreased']),
            'Activity Level': generate_response(dog_severity, ['Normal', 'More active than usual', 'Less active than usual']),
            'Water Consumption': generate_response(dog_severity, ['Normal', 'Increased', 'Decreased']),
            'Behaviour Changes': generate_response(dog_severity, ['Normal', 'More affectionate', 'More withdrawn']),
            'Breathing Changes': generate_response(dog_severity, ['Normal', 'More  breathing', 'Less breathing']),
            'Limbs Swelling': generate_response(dog_severity, ['Normal', 'Dull', 'Fluffy']),
            'Vocalization': generate_response(dog_severity, ['Normal', 'More vocal', 'Less vocal']),
            'Weight Changes': generate_response(dog_severity, ['Stable', 'Weight gain', 'Weight loss']),
            'Nose Condition': generate_response(dog_severity, ['Normal', 'More wet', 'More dry']),
            'Sleep Patterns': generate_response(dog_severity, ['Normal', 'More sleeping', 'Less sleeping']),
        }

        # Write row to CSV
        writer.writerow({
            'ID': f"{counter}",
            'Age': dog_age,
            'Gender': dog_gender,
            'Vaccination Status': dog_vaccination_status,
            'Severity': dog_severity,
            **responses  # Include all the responses to questions
        })

print(f"Dataset generated successfully at {csv_file_path}")
