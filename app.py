from flask import Flask, render_template, request
from itertools import product
from itertools import count

app = Flask(__name__)

# Define the tables with class information
tables = [
    [
        (11409, "Monday", "10:30 AM - 11:35 AM", "Coop"),
        (11857, "Monday", "01:35 PM - 02:40 PM", "Coop"),
        (11695, "Tuesday", "01:35 PM - 02:40 PM", "Coop"),
        (11705, "Tuesday", "01:35 PM - 02:40 PM", "Coop"),
        (11858, "Tuesday", "01:35 PM - 02:40 PM", "Coop"),
        (11859, "Tuesday", "01:35 PM - 02:40 PM", "Coop"),
        (12103, "Wednesday", "01:35 PM - 02:40 PM", "Coop"),
        (12329, "Wednesday", "11:45 AM - 12:50 PM", "Coop"),
        (14588, "Wednesday", "11:45 AM - 12:50 PM", "Coop"),
        (15448, "Wednesday", "01:35 PM - 02:40 PM", "Coop"),
        (15449, "Wednesday", "02:50 PM - 03:55 PM", "Coop"),
        (20157, "Wednesday", "02:50 PM - 03:55 PM", "Coop"),
        (11909, "Tuesday", "03:25 PM - 04:30 PM", "Coop"),
        (12102, "Tuesday", "03:25 PM - 04:30 PM", "Coop")
    ],
    [
        (13924, "Monday, Wednesday, Thursday", "08:00 AM - 09:05 AM", "Calc 2"),
        (11136, "Monday, Wednesday, Thursday", "08:00 AM - 09:05 AM", "Calc 2"),
        (12275, "Monday, Wednesday, Thursday", "09:15 AM - 10:20 AM", "Calc 2"),
        (11223, "Monday, Wednesday, Thursday", "09:15 AM - 10:20 AM", "Calc 2"),
        (13788, "Monday, Wednesday, Thursday", "09:15 AM - 10:20 AM", "Calc 2"),
        (15700, "Monday, Wednesday, Thursday", "09:15 AM - 10:20 AM", "Calc 2"),
        (10699, "Monday, Wednesday, Thursday", "10:30 AM - 11:35 AM", "Calc 2"),
        (12042, "Monday, Wednesday, Thursday", "10:30 AM - 11:35 AM", "Calc 2"),
        (12211, "Monday, Wednesday, Thursday", "01:35 PM - 02:40 PM", "Calc 2"),
        (14520, "Monday, Wednesday, Thursday", "01:35 PM - 02:40 PM", "Calc 2"),
        (14760, "Monday, Wednesday, Thursday", "01:35 PM - 02:40 PM", "Calc 2"),
        (16552, "Monday, Wednesday, Thursday", "01:35 PM - 02:40 PM", "Calc 2"),
        (10204, "Monday, Wednesday, Thursday", "04:35 PM - 05:40 PM", "Calc 2"),
        (15703, "Monday, Wednesday, Thursday", "04:35 PM - 05:40 PM", "Calc 2")
    ],
    [
        (10125, "Monday, Wednesday, Thursday", "09:15 AM - 10:20 AM", "Logic and Comp"),
        (13743, "Monday, Wednesday, Thursday", "10:30 AM - 11:35 AM", "Logic and Comp"),
        (14331, "Monday, Wednesday, Thursday", "04:35 PM - 05:40 PM", "Logic and Comp")
    ],
    [
        (11413, "Tuesday, Friday", "09:50 AM - 11:30 AM", "Programming in C++")
    ],
    [
        (12342, "Tuesday, Friday", "03:25 PM - 05:05 PM", "Web Development"),
        (17229, "Tuesday", "06:00 PM - 09:20 PM", "Web Development")
    ]
]

# Function to check if two classes overlap
def overlap(class1, class2):
    day1, time1 = class1[1], class1[2]
    day2, time2 = class2[1], class2[2]

    if day1 == day2:
        start1, end1 = map(lambda x: int(x.split()[0].replace(":", "")), time1.split(" - "))
        start2, end2 = map(lambda x: int(x.split()[0].replace(":", "")), time2.split(" - "))

        return not (end1 <= start2 or end2 <= start1)
    return False

# Generate all possible combinations of classes without overlapping
def generate_combinations():
    id_generator = count(1)
    all_combinations = []
    for comb in product(*tables):
        if len(set(cls[3] for cls in comb)) == len(tables) and not any(overlap(pair[0], pair[1]) for pair in product(comb, comb) if pair[0] != pair[1]):
            combination_id = next(id_generator)
            all_combinations.append((combination_id, comb))
    return all_combinations

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crn_to_remove = int(request.form['crn'])
        for i, table in enumerate(tables):
            tables[i] = [cls for cls in table if cls[0] != crn_to_remove]

    combinations = generate_combinations()
    print(combinations)  # Add this line to print combinations
    return render_template('index.html', combinations=combinations)


if __name__ == '__main__':
    app.run(debug=True)
