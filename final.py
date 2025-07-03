import matplotlib.pyplot as plt
import adjustText
import plotly.graph_objects as go
import tkinter as tk
from tkinter import messagebox

stars = {
    'Polaris': (2.52,89.26),
    'Sirius': (6.75,-16.72),
    'Vega': (18.62,38.78),
    'Betelgeuse': (5.92,7.41),
    'Meissa':(5.58,9.93),
    'Rigel':(5.24,-8.20),
    'Altair':(19.85,8.87),
    'Deneb':(20.69,45.28),
    'Procyon':(7.66,5.22),
    'Capella':(5.28,46.00),
    'Arcturus':(14.26,19.18),
    'Spica':(13.42,-11.16),
    'Antares':(16.49,-26.43),
    'Fomalhaut':(22.69,-29.62),
    'Regulus':(10.14,11.97),
    'Sadr':(20.22,40.26),
    'Albireo':(19.51,27.96),
    'Gienah':(20.77,33.97),
    'Aldebaran':(4.60,16.52),
    'Pollux':(7.76,28.03),
    'Castor':(7.58,31.89),
    'Bellatrix':(5.42,6.35),
    'Alnilam':(5.60,-1.20),
    'Mirach':(1.16,35.62),
    'Sheliak':(18.84,33.36),
    'Sulafat':(18.90,32.69),
    'Algol':(3.14,40.96),
    'Dubhe':(11.03,61.75),
    'Merak':(11.01,56.38),
    'Phecda':(11.90,53.69),
    'Megrez':(12.25,57.03),
    'Shaula':(17.56,-37.10),
    'Sargas':(17.62,-42.99),
    'Dschubba':(16.00,-22.62),
    "Denebola":(11.82,14.57),
    "Algieba":(10.33,19.84),
    'Alhena':(6.63,16.40),
    'Wasat':(7.35,21.98),
    'Elnath':(5.44,28.61),
    'Pleione':(3.82,24.18),
    'Schedar':(0.68,56.54),
    'Caph':(0.15,59.15),
    "Gamma cas":(0.95,60.72),
    'Alioth':(12.88,55.96),
    'Mizar':(13.40,54.92),
    'Alkaid':(13.79,49.31),
    'Saiph':(5.80,-9.67),
    'Mintaka':(5.53,-0.3),
    'Yildun':(17.54,86.59),
    'Kochab': (14.85, 74.15),
    'Pherkad': (15.74, 71.83),
    'Alnitak': (5.68, -1.94),
    'Epsilon UMi': (16.77, 82.03),
    'Zeta UMi': (15.74, 77.80),
    'Eta UMi': (16.29, 75.76),
    'Segin': (1.90, 63.67),
    'Ruchbah': (1.43, 60.24),
    'Adhafera':(10.27,23.42),
    'Ras Elased Australis':(9.76,23.77),
    'Ras Elased Borealis':(9.47,26.01),
    'Zosma':(11.23,20.52),
    'Chort':(11.24,15.43),
    }

constellations={
    "Orion":['Mintaka','Alnilam','Alnitak','Saiph','Rigel','Mintaka','Bellatrix','Meissa','Betelgeuse','Alnitak'],
    "Ursa Major":["Alkaid","Mizar","Alioth","Megrez","Phecda","Merak","Dubhe","Megrez"],
    "Ursa Minor":['Polaris', 'Yildun', 'Epsilon UMi', 'Zeta UMi','Eta UMi', 'Pherkad', 'Kochab', 'Polaris'],
    "Cassiopeia":["Segin","Ruchbah","Gamma cas","Schedar","Caph"],
    "Leo":['Regulus', 'Algieba', 'Adhafera', 'Ras Elased Australis', 'Ras Elased Borealis', 'Zosma', 'Chort'],
    "Taurus": ['Aldebaran', 'Elnath', 'Pleione'],
    "Gemini": ['Pollux', 'Castor', 'Wasat', 'Alhena'],
    "Scorpius": ['Dschubba', 'Antares', 'Shaula', 'Sargas'],
    "Cygnus": ['Deneb', 'Sadr', 'Albireo', 'Gienah'],
    "Lyra": ['Vega', 'Sheliak', 'Sulafat']
    }

def load_constellation_info(filepath="constellation_data.txt"):
    data = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()

    current = None
    for line in lines:
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1]
            data[current] = {}
        elif "Alias:" in line:
            data[current]["alias"] = line.split("Alias:")[1].strip()
        elif "Major Stars:" in line:
            stars_line = line.split("Major Stars:")[1].strip()
            data[current]["major_stars"] = [s.strip() for s in stars_line.split(',')]
        elif "Fact:" in line:
            data[current]["fact"] = line.split("Fact:")[1].strip()
    return data


def constellation_map():   
    text=[]
    plt.figure(figsize=(25,25))
    ax=plt.axes(facecolor='black')

    for name, (x, y) in stars.items():
        plt.scatter(x, y, color='white')
        ax.annotate(
            name,
            (x, y),
            textcoords="offset points",
            xytext=(5, 5),  # Arrow offset
            ha='center',
            color='cyan',
            fontsize=10,
            arrowprops=dict(arrowstyle="->", color='gray', shrinkA=10)
        )

    ax.set_xlim(0,25)
    ax.set_ylim(-50,95)

    plt.grid(linestyle='dashed')

    plt.title("2D Star map")
    plt.xlabel("Right Acession[RA] in hrs")
    plt.ylabel("Deg°")

    orion_order = ['Betelgeuse', 'Bellatrix', 'Mintaka', 'Alnilam', 'Rigel', 'Saiph', 'Betelgeuse']

    x_vals = [stars[star][0] for star in orion_order]
    y_vals = [stars[star][1] for star in orion_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(7.07,-1.4, 'Orion', color='orange', fontsize=14, fontweight='bold')

    ursamajor_order = ['Dubhe', 'Merak', 'Phecda', 'Megrez', 'Alioth', 'Mizar', 'Alkaid','Dubhe']
    x_vals = [stars[star][0] for star in ursamajor_order]
    y_vals = [stars[star][1] for star in ursamajor_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(12.62,64.6, 'Ursa Major', color='orange', fontsize=14, fontweight='bold')
    
    cygnus_order = ['Deneb', 'Sadr', 'Albireo', 'Gienah', 'Deneb']
    x_vals = [stars[star][0] for star in cygnus_order]
    y_vals = [stars[star][1] for star in cygnus_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(21,22.6, 'Cygnus', color='orange', fontsize=14, fontweight='bold')

    lyra_order = ['Vega', 'Sheliak', 'Sulafat','Vega']
    x_vals = [stars[star][0] for star in lyra_order]
    y_vals = [stars[star][1] for star in lyra_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(17.51,34.3, 'Lyra', color='orange', fontsize=14, fontweight='bold')

    scorpius_order = ['Dschubba', 'Antares', 'Shaula', 'Sargas']
    x_vals = [stars[star][0] for star in scorpius_order]
    y_vals = [stars[star][1] for star in scorpius_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(17.91,-22.8, 'Scorpius', color='orange', fontsize=14, fontweight='bold')
    
    leo_order = ['Regulus', 'Algieba', 'Denebola', 'Regulus']
    x_vals = [stars[star][0] for star in leo_order]
    y_vals = [stars[star][1] for star in leo_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(11.74,20.9, 'Leo', color='orange', fontsize=14, fontweight='bold')
    
    gemini_order = ['Pollux', 'Castor', 'Wasat', 'Alhena', 'Pollux']
    x_vals = [stars[star][0] for star in gemini_order]
    y_vals = [stars[star][1] for star in gemini_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(7.90,38.7, 'Gemini', color='orange', fontsize=14, fontweight='bold')
    
    taurus_order = ['Aldebaran', 'Elnath', 'Pleione', 'Aldebaran']
    x_vals = [stars[star][0] for star in taurus_order]
    y_vals = [stars[star][1] for star in taurus_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(1.80,20.5, 'Taurus', color='orange', fontsize=14, fontweight='bold')
    
    cass_order = ['Schedar','Caph','Gamma cas','Schedar']
    x_vals = [stars[star][0] for star in cass_order]
    y_vals = [stars[star][1] for star in cass_order]
    plt.plot(x_vals, y_vals, color='yellow', linewidth=1.5,zorder=1)
    plt.text(1.22,67.1, 'Cassiopeia', color='orange', fontsize=14, fontweight='bold')
    plt.show()



def constellation_info(stars,constellations,s):
    info_data = load_constellation_info()
    if s not in constellations:
        print("Please select a constellation from the above list only.")
    fig=go.Figure()
    star_list=constellations[s]
    stars_used={name:stars[name] for name in star_list if name in stars}
    for name,(x,y) in stars_used.items():
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            name=name,
            text=[name],
            textposition='top center',
            marker=dict(color='white', size=8),
            hovertemplate=f"<b>{name}</b><br>RA: {x} hrs<br>Dec: {y}°<extra></extra>"
        ))

    x_vals = [stars[star][0] for star in star_list if star in stars]
    y_vals = [stars[star][1] for star in star_list if star in stars]

    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode='lines',
        name=s,
        line=dict(color='yellow', width=2),
        hoverinfo='skip'
    ))

    cx = sum(x_vals) / len(x_vals)
    cy = sum(y_vals) / len(y_vals)
    fig.add_trace(go.Scatter(
        x=[cx], y=[cy],
        mode='text',
        text=[s],
        textposition='top center',
        textfont=dict(color='orange', size=14)
    ))

    fig.update_layout(
        title=f"{s} Constellation",
        xaxis=dict(title='Right Ascension (hrs)', range=[min(x_vals)-1, max(x_vals)+1], showgrid=True,zeroline=False, gridcolor='gray'),
        yaxis=dict(title='Declination (°)', range=[min(y_vals)-10, max(y_vals)+10], showgrid=True,zeroline=False, gridcolor='gray'),
        paper_bgcolor='black',
        plot_bgcolor='black',
        font=dict(color='cyan'),
        showlegend=False
    )

    fig.show()
    
    print("\n--- CONSTELLATION INFO ---")
    print(f"Name       : {s}")
    print(f"Alias      : {info_data[s]['alias']}")
    print(f"Major Stars: {', '.join(info_data[s]['major_stars'])}")
    print(f"Fact       : {info_data[s]['fact']}\n")

def constellation_quiz():
    quiz_data = [
        {
            'question': "Which constellation is known as the 'Hunter'?",
            'options': ['Orion', 'Ursa Major', 'Ursa Minor', 'Cassiopeia'],
            'answer': 'Orion'
        },
        {
            'question': "The North Star is located in which constellation?",
            'options': ['Orion', 'Ursa Major', 'Ursa Minor', 'Cassiopeia'],
            'answer': 'Ursa Minor'
        },
        {
            'question': "Which constellation is famous for its 'W' shape?",
            'options': ['Orion', 'Ursa Major', 'Ursa Minor', 'Cassiopeia'],
            'answer': 'Cassiopeia'
        },
        {
            'question': "Which constellation contains the star Betelgeuse?",
            'options': ['Orion', 'Ursa Major', 'Ursa Minor', 'Cassiopeia'],
            'answer': 'Orion'
        },
        {
            'question': "Which of these is NOT a zodiac constellation?",
            'options': ['Leo', 'Scorpius', 'Pegasus', 'Taurus'],
            'answer': 'Pegasus'
        },
        {
            'question': "Which shape is the constellation Lyra known for?",
            'options': ['Triangle', 'W', 'Harp', 'Circle'],
            'answer': 'Harp'
        },
        {
            'question': "Which constellation is represented as a bull?",
            'options': ['Orion', 'Ursa Major', 'Ursa Minor', 'Taurus'],
            'answer': 'Taurus'
        },
        {
            'question': "Which constellation represents a Lion?",
            'options': ['Leo', 'Ursa Major', 'Ursa Minor', 'Cassiopeia'],
            'answer': 'Leo'
        },
        {
            'question': "Which constellation is visible all year around?",
            'options': ['Orion', 'Ursa Major', 'Ursa Minor', 'Cassiopeia'],
            'answer': 'Ursa Major'
        },
        {
            'question': "Which star is located at the heart of the Scorpius Constellation?",
            'options': ['Vega', 'Antares', 'Sirius', 'Polaris'],
            'answer': 'Antares'
        }
    ]

    root = tk.Tk()
    root.title("Constellation Quiz")
    root.geometry("500x350")
    
    question_index = [0]
    score = [0]

    def load_question():
        answer_var.set(None)
        q = quiz_data[question_index[0]]
        question_label.config(text=f"Q{question_index[0]+1}: {q['question']}")
        for i, option in enumerate(q['options']):
            option_buttons[i].config(text=option, value=option)
        feedback_label.config(text="")

    def submit_answer():
        selected = answer_var.get()
        correct_answer = quiz_data[question_index[0]]['answer']
        if selected == correct_answer:
            score[0] += 1
            feedback_label.config(text="Correct!", fg="green")
        else:
            feedback_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red")

        submit_btn.config(state="disabled")
        next_btn.config(state="normal")

    def next_question():
        question_index[0] += 1
        if question_index[0] < len(quiz_data):
            load_question()
            submit_btn.config(state="normal")
            next_btn.config(state="disabled")
        else:
            messagebox.showinfo("Quiz Finished", f"You scored {score[0]} out of {len(quiz_data)}")
            root.destroy()

    question_label = tk.Label(root, text="", wraplength=450, font=("Helvetica", 12))
    question_label.pack(pady=20)

    answer_var = tk.StringVar()
    option_buttons = []
    for _ in range(4):
        btn = tk.Radiobutton(root, text="", variable=answer_var, value="", font=("Helvetica", 10))
        btn.pack(anchor="w", padx=40)
        option_buttons.append(btn)

    feedback_label = tk.Label(root, text="", font=("Helvetica", 10))
    feedback_label.pack(pady=5)

    submit_btn = tk.Button(root, text="Submit", command=submit_answer)
    submit_btn.pack(pady=5)

    next_btn = tk.Button(root, text="Next", command=next_question, state="disabled")
    next_btn.pack(pady=5)

    load_question()
    root.mainloop()

# Main program 

print("          ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗           \n          ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║           \n          ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝           \n          ╦╔╗╔╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗╦╦  ╦╔═╗          \n          ║║║║ ║ ║╣ ╠╦╝╠═╣║   ║ ║╚╗╔╝║╣           \n          ╩╝╚╝ ╩ ╚═╝╩╚═╩ ╩╚═╝ ╩ ╩ ╚╝ ╚═╝          \n  ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╦  ╦  ╔═╗╔╦╗╦╔═╗╔╗╔  ╔╦╗╔═╗╔═╗\n  ║  ║ ║║║║╚═╗ ║ ║╣ ║  ║  ╠═╣ ║ ║║ ║║║║  ║║║╠═╣╠═╝\n  ╚═╝╚═╝╝╚╝╚═╝ ╩ ╚═╝╩═╝╩═╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╩ ╩╩ ╩╩  \n              ╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗               \n              ╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║               \n              ╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩               \n")

info_data = load_constellation_info()

while True:
    print("\nPick one to continue:")
    print("1. Basic 2D star map.")
    print("2. Know about major constellations.")
    print("3. Test your knowledge on constellations.")
    print("4. Exit")

    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if n == 1:
        constellation_map()

    elif n == 2:
        print("\nSome of the major constellations are:")
        for i, name in enumerate(constellations.keys(), 1):
            print(f"{i}. {name}")
        s = input("Enter a constellation to continue: ").strip().title()
        if s in constellations:
            constellation_info(stars, constellations, s)
        else:
            print("Constellation not found. Please check spelling.")

    elif n == 3:
        constellation_quiz()

    elif n == 4:
        print("╔═╗═╗ ╦╦╔╦╗╦╔╗╔╔═╗    ╔═╗╔═╗╔═╗╔╦╗╔╗ ╦ ╦╔═╗  \n║╣ ╔╩╦╝║ ║ ║║║║║ ╦    ║ ╦║ ║║ ║ ║║╠╩╗╚╦╝║╣   \n╚═╝╩ ╚═╩ ╩ ╩╝╚╝╚═╝    ╚═╝╚═╝╚═╝═╩╝╚═╝ ╩ ╚═╝  \n")
        break

    else:
        print("Invalid choice. Please choose a number between 1 and 4.")