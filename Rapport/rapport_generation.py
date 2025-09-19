from rapport_class import Rapport
from datetime import date
import subprocess
import os

working_dir = "C:/Users/mrawr/Documents/LaTek_Files/Kholles"


# base_file_path = "./template_rapport.tex"
# file = open(base_file_path, 'rt')

def write_report(classe, rapport:Rapport, planche):
    if rapport.note != '':
        note = r'\begin{flushright} \textbf{Note: }' + rapport.note + r'\end{flushright}'
    else:
        note = ''

    try:
        rapport_file = open('../R-' + classe + '/Rapport-de-colle-' + str(date.today()) + '_' +rapport.student.replace(' ', '_')  +'_'+planche.replace(' ', '-') +'.tex', 'w+',encoding='utf-8')
    except FileNotFoundError: 
        os.mkdir('../R-' + classe)
        rapport_file = open('../R-' + classe + '/Rapport-de-colle-' + str(date.today()) + '_' +rapport.student.replace(' ', '_')  +'_'+planche.replace(' ', '-') +'.tex', 'w+',encoding='utf-8')

    rapport_file.write(r'\documentclass{article}\usepackage{array} \usepackage{multirow} \usepackage[francais]{babel} \usepackage{lmodern} \usepackage[T1]{fontenc} \begin{document}\begin{tabular}{|c|p{7cm}p{1pt}|}\hline')
    rapport_file.write(r'\multicolumn{3}{|c|}{Rapport de Colle: \textbf{' + f'{rapport.student}' + r'} -- \today} \\ \hline\hline')
    for i, exercise in enumerate(rapport.exercices):
        rapport_file.write(r'\multicolumn{2}{|l|}{' + f'{exercise.replace('_', r'\_')}' + r'} & \multicolumn{1}{r|}{' + f'{rapport.exercices_note[i]}' +r'} \\ \hline')

    try: 
        rapport_file.write(r'\multicolumn{2}{|l|}{' f'{sum(rapport.exercices_note)}' +r'} & \multicolumn{1}{r|}{NOTE} \\ \hline')
    except:
        pass
    
    rapport_file.write(r' Commentaire & \multicolumn{2}{|p{8cm}|}{' +f'{rapport.commentary}{note}' +r'}  \\ \hline')
    rapport_file.write(r'\end{tabular}\end{document}')
    rapport_file.close()
    subprocess.run(r'pdflatex ..\R-' + classe + r'\Rapport-de-colle-' + str(date.today()) + '_' +rapport.student.replace(' ', '_')  +'_'+planche.replace(' ', '-')+r'.tex -output-directory=..\R-' + classe +r' -aux-directory=.', shell=True)
    subprocess.run(r'.\del_aux_files.bat', shell = True)