import csv
import random

def generate_age():
    return random.randint(1, 15)

def generate_vaccination_status(severity):
    return random.choices(['Vaccinated', 'Not Vaccinated'], weights=[100 - Severity, Severity])[0]

def generate_response(severity, values):
    threshold = random.uniform(0.3, 0.6) * 100

    if severity < threshold:
        weights = [0.6, 0.2, 0.2]
    else:
        weights = [0.2, 0.4, 0.4]

    return random.choices(values, weights=weights)[0]

def generate_severity():
    return random.uniform(0, 100)

csv_file_path = 'cat_illness_dataset.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Age', 'Gender', 'Appetite', 'Activity Level', 'Water Consumption',
                  'Behaviour Changes', 'Litter Box Habits', 'Coat Condition', 'Vocalization',
                  'Weight Changes', 'Interaction with Other Pets', 'Sleep Patterns',
                  'FVRCP', 'Severity']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate synthetic data
    for _ in range(300000):  # Adjust the number of rows as needed
        cat_age = generate_age()
        cat_gender = random.choice(['Male', 'Female'])
        cat_severity = generate_severity()
        cat_vaccination_status = generate_vaccination_status(cat_severity)

        # Generate responses to questions
        responses = {
            'Appetite': random.choice(['Normal', 'Increased', 'Decreased']),
            'Activity Level': random.choice(['Normal', 'More active than usual', 'Less active than usual']),
            'Water Consumption': random.choice(['Normal', 'Increased', 'Decreased']),
            'Behaviour Changes': random.choice(['Normal', 'More affectionate', 'More withdrawn']),
            'Litter Box Habits': random.choice(['Normal', 'More frequent urination', 'Less frequent urination']),
            'Coat Condition': random.choice(['Normal', 'Dull', 'Fluffy']),
            'Vocalization': random.choice(['Normal', 'More vocal', 'Less vocal']),
            'Weight Changes': random.choice(['Stable', 'Weight gain', 'Weight loss']),
            'Interaction with Other Pets': random.choice(['Normal', 'More aggressive', 'More submissive']),
            'Sleep Patterns': random.choice(['Normal', 'More sleeping', 'Less sleeping']),
        }

        # Write row to CSV
        writer.writerow({
            'Age': cat_age,
            'Gender': cat_gender,
            'Vaccination Status': cat_vaccination_status,
            'Severity': cat_severity,
            **responses  # Include all the responses to questions
        })

print(f"Dataset generated successfully at {csv_file_path}")
