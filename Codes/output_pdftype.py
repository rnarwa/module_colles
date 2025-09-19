import sys
import os
exedir = './../Exercices/'

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
        if char != ',' and char != ']':
            lexeme += char # adding a char each time
        if (i+1 < len(fname)): # prevents error
            if fname[i+1] == ',' or lexeme in keywords or fname[i+1] == ']': 
                if lexeme != '':
                    lexemes.append(lexeme)
                    lexeme = ''
    parameters={}
    for i, lex in enumerate(lexemes):
        if lex in keywords:
            parameters[lex] = lexemes[i+1]
    
    return parameters

type = sys.argv[1:]
print(type)

texfile = open('temp.tex', 'w+')
files = os.listdir(exedir)

texfile.write('\\documentclass{planchedecolle}\n\\title{Test}\n\\date{Test}\n\\begin{document}\n\n')

for file in files:
    for elm in type:
        if elm in file: 
            exofile = open(exedir + file, 'r')
            for line in exofile:
                line = line.replace('\n','')
                if line == '\\begin{Exercise}' or interesting_line == '\\begin{Exercise}\n':
                    if line == '\\begin{Exercise}':
                        interesting_line = next(exofile)
                    else:
                        interesting_line = line
                    process_line = interesting_line.replace(' ', '')
                    parse= parser(process_line, ['type=', 'label='])
                    planche  = parse['type=']
                    nom_exo = parse['label=']
                    planche = planche.replace(' ', '')
                    if planche in type:
                        texfile.write('\\begin{Exercise}\n')
                        while interesting_line != '\\end{Exercise}\n':
                            texfile.write(interesting_line)
                            interesting_line = next(exofile)
                        texfile.write('\\end{Exercise}\n')
                        interesting_line = next(exofile)
                        while interesting_line == '\n':
                            interesting_line = next(exofile)
                        
                        if interesting_line == '\\begin{Answer}\n':
                            while interesting_line != '\\end{Answer}\n':
                                texfile.write(interesting_line)
                                interesting_line = next(exofile)
                            texfile.write('\\end{Answer}\n')

        
texfile.write('\\pageReponses\n\\end{document}')

