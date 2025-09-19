from gui_classes import *
from rapport_class import *
from rapport_generation import *
from planche_handler import *

liste_classe = ['Classe_1', 'Classe_2']
liste_eleves = ['']
planche_dd_list = ['']
exo_dd_list = {'':''}


def update_option_menu(om:tk.OptionMenu, om_variable, option_list):
    menu = om['menu']
    menu.delete(0, 'end')
    for item in option_list:
        menu.add_command(label = item, command = lambda value=item: om_variable.set(value))

def refresh():
    # try:
    if class_opt.get() in liste_classe:
        # print(class_opt.get() + '_liste_eleves.csv')
        liste_eleves = np.genfromtxt(r'./Liste_eleves/' + class_opt.get() + '_liste_eleves.csv', dtype = str, delimiter=',')
        # global studentDDselect 
        # studentDDselect = tk.OptionMenu(scroll_frame, student_opt, *liste_eleves)
        update_option_menu(studentDDselect, student_opt, liste_eleves)
        studentDDselect.grid(row=2, column=0, columnspan=2)
    # except:
    #     print('Problem in Student List Generation')

    # try:
    if student_opt.get() in liste_eleves:
        planche_semaines_list = gen_planches('../P-' + class_opt.get())
        # print(planche_semaines_list)
        global planche_dd_list
        planche_dd_list = [planche_semaine.number + '-' + planche_semaine.name for planche_semaine in planche_semaines_list.values()]
        update_option_menu(plancheDDselect, planche_opt, planche_dd_list)
        plancheDDselect.grid(row=3, column=0)
    else:
        plancheDDselect.grid_forget()
        exoDDselect.grid_forget()
        exo_clear()
        planche_opt.set('Semaine')
        student_opt.set('Eleve')
        generateButton.grid_forget()

    # except:
    #     print('Problem in Planches list Generation')

    # try:
    if planche_opt.get() in planche_dd_list:
        exo_dd_list = planche_semaines_list[planche_opt.get()].planches
        update_option_menu(exoDDselect, exo_opt, exo_dd_list.keys())
        exoDDselect.grid(row=3, column=1)
    else: 
        exoDDselect.grid_forget()
        planche_opt.set('Semaine')
    # except:
    #     print("Problem in Exercices list creation")

    # try:    
    if exo_opt.get() in exo_dd_list.keys():
        exo_clear()
        global exo_list
        exo_list = planche_semaines_list[planche_opt.get()].planches[exo_opt.get()]
        print(exo_list)
        for i, exo in enumerate(exo_list):
            globals()[f'Exo_{i}_label'] = tk.Label(scroll_frame, text = exo)
            globals()[f'Exo_{i}_note_input'] = tk.Entry(scroll_frame)
            globals()[f'Exo_{i}_label'].grid(row = 4+i, column = 0)
            globals()[f'Exo_{i}_note_input'].grid(row = 4+i, column = 1)

        global comm_label
        comm_label = tk.Label(scroll_frame, text='Commentaire: ')
        global comm_input
        comm_input = tk.Text(scroll_frame, width=20, height=10)
        global note_label
        note_label = tk.Label(scroll_frame, text='Note:')
        global note_input
        note_input = tk.Entry(scroll_frame)
        comm_label.grid(row=4+i+1, column=0)
        comm_input.grid(row=4+i+1, column=1)
        note_label.grid(row =6+i, column=0)
        note_input.grid(row=6+i, column=1)
        generateButton.grid(row = 0, column=1, columnspan=2)
    else:
        exo_clear()
        exo_opt.set('Planche')

    # except:
    #     print("Problem in exercices creation")
    
def exo_clear():
    for var in globals().keys():
        print(var, 'note' in var)
        if 'Exo_' in var:
            # print(var, globals()[var])
            globals()[var].grid_forget()
    try :
        globals()["comm_label"].grid_forget()
        globals()["comm_input"].grid_forget()
        globals()['note_input'].grid_forget()
        globals()['note_label'].grid_forget()
    except KeyError: pass

def clear():
    # class_opt.set("Classe")
    student_opt.set('Eleve')
    planche_opt.set('Semaine')
    exo_opt.set('Planche')

    for var in globals().keys():
        # print(var, 'Exo_' in var)
        if 'Exo_' in var:
            # print(var, globals()[var])
            globals()[var].grid_forget()
    # globals()["liste_eleves"] = []
    globals()["planche_dd_list"] = []
    globals()["exo_dd_list"] = {} 
    generateButton.grid_forget()

    # globals()["studentDDselect"].grid_forget()
    globals()["plancheDDselect"].grid_forget()
    globals()["exoDDselect"].grid_forget()
    globals()["comm_label"].grid_forget()
    globals()["comm_input"].grid_forget()
    globals()['note_input'].grid_forget()
    globals()['note_label'].grid_forget()
    # globals()['generateButton'].grid_forget()

def generate_report():
    global rapport
    rapport = Rapport()
    rapport.student = student_opt.get()
    rapport.exercices = exo_list
    rapport.commentary = comm_input.get('1.0', 'end')
    rapport.note = note_input.get()
    for i, exo in enumerate(exo_list):
        rapport.set_note(exo, globals()[f'Exo_{i}_note_input'].get())

    write_report(class_opt.get(), rapport, planche_opt.get())
    print(rapport.__dict__)
    # compile_button.grid(row= 0, column= 4)

    clear()

def compile():
    # subprocess.run("timeout /t 1")
    # print(f"pdflatex ..\R-{class_opt.get()}\Rapport-de-colle-{rapport.student.replace(' ', '-')}_{planche_opt.get().replace(' ', '-')}_{str(date.today()).replace('\n','')}.tex")

    subprocess.run(r'pdflatex ..\R-' + class_opt.get() + r'\Rapport-de-colle-' + str(date.today()) + '_' + rapport.student.replace(' ', '_') +'_'+planche_opt.get().replace(' ', '-') +r'.tex -output-directory=..\R-' + class_opt.get(), shell=True)
    subprocess.run(fr'del "..\R-{class_opt.get()}\*.log"')
    subprocess.run(fr'del "..\R-{class_opt.get()}\*.aux"')
    # subprocess.run("dir", shell=True)


app = GUI(screenName='Générateur de rapport de Colles')

main_window = ScrollableFrame(app)
main_window.pack(fill = 'both', expand=True)

scroll_frame = main_window.scrollable_frame


class_opt = tk.StringVar(value='Classe')
student_opt = tk.StringVar(value='Eleve')
planche_opt = tk.StringVar(value='Semaine')
exo_opt = tk.StringVar(value='Planche')

refreshButton = tk.Button(scroll_frame, text = 'Refresh', command = refresh)
generateButton = tk.Button(scroll_frame, text = 'Generate Rapport', command = generate_report)
compile_button = tk.Button(scroll_frame, text = 'Compile', command=compile)
studentDDselect = tk.OptionMenu(scroll_frame, student_opt, *liste_eleves)
classeDDselect = tk.OptionMenu(scroll_frame, class_opt, *liste_classe)
exoDDselect = tk.OptionMenu(scroll_frame, exo_opt, *exo_dd_list)
plancheDDselect = tk.OptionMenu(scroll_frame, planche_opt, *planche_dd_list)


refreshButton.grid(row=0, column=0)
classeDDselect.grid(row =1, column = 0, columnspan=2)

if __name__ == '__main__':
    app.mainloop()