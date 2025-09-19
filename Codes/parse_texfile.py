import os
import pickle

exedir = '../Exercices/'

files = os.listdir(exedir)

# file = open(exedir + 'exercices.auxtex', 'r')
text = open(exedir + 'Liste des exercices.txt', 'w+',encoding='utf-8')

def parser(fname, keywords):
    '''Parse a string (filename) to extract parameters specified in keywords.

    Parameters
    ----------
    fname: str
        Name of the file to parse.
    keywords: list of str
        Name of the parameters to extract.

    Outputs
    -------
    parameters: dict.
        The extracted value of the parameters to parse, such as that for all parameter in keywords, parameters[parameter] is the value of this parameter. Parameter.
    '''
    lexemes = []
    lexeme = ''
    for i, char in enumerate(fname):
        if char != ',' and char != ']' and char != '[':
            lexeme += char # adding a char each time
        if (i+1 < len(fname)): # prevents error
            if fname[i+1] == ',' or lexeme.replace(' ', '') in keywords or fname[i+1] == ']': 
                if lexeme != '':
                    lexemes.append(lexeme)
                    lexeme = ''
    parameters={}

    for i, lex in enumerate(lexemes):
        if lex.replace(' ', '') in keywords:
            parameters[lex.replace(' ', '')] = lexemes[i+1]
    
    return parameters
dico = {}
corr = []
dico_labels = {}

for file_name in files:
    if file_name == 'Liste des exercices.txt':
        pass
    else:
        file = open(exedir + file_name, 'r', encoding='utf-8')
        for line in file:
            line = line.replace('\n','')
            if line == '\\begin{Exercise}':
                interesting_line = next(file)
                # interesting_line = interesting_line.replace(' ', '')
                parse= parser(interesting_line, ['type=', 'label=', 'title='])
                planche  = parse['type='].replace(' ', '')
                nom_exo = parse['label='].replace(' ', '')
                try:
                    titre_exo = parse['title='].strip()
                    if not(r"\\" in titre_exo):
                        titre_exo.replace('{', '').replace('}','')
                except: print(titre_exo, parse)
                nom_exo = nom_exo.replace('{','')
                nom_exo = nom_exo.replace('}','')
                if planche not in dico.keys():
                    dico[planche] = []
                dico[planche].append(nom_exo)
                dico_labels[nom_exo] = titre_exo
            if line  == '\\begin{Answer}':
                interesting_line = next(file)
                interesting_line = interesting_line.replace(' ', '')
                interesting_line = interesting_line.replace('[', '')
                exo_corr = parser(interesting_line, ['ref='])['ref=']
                exo_corr = exo_corr.replace('{','')
                exo_corr = exo_corr.replace('}','')
                corr.append(exo_corr)

text.write(r"Liste des labels d'exos triés par planche. Utiliser \selectexo{planche}{label_exo} pour inclure dans un .tex d'une planche. Utiliser exo_view.bat label_exo ou exo_view.bat -type planche pour avoir une prévisualisation des exercices voulus.")
for planche in dico.keys():
    text.write('\n\nListe des exercices pour les planches ' + planche + ':\n')
    for exo in dico[planche]:
        if exo in corr:
            text.write(exo + ' (corrigé); ')
        else:
            text.write(exo+ '; ')

with open(r'../Rapport/Liste_exos.picl', 'wb+') as file:
    pickle.dump(dico_labels, file)






