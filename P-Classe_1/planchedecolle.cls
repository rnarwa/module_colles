\ProvidesClass{planchedecolle}


\LoadClass[12pt, a4paper]{article}

\RequirePackage[T1]{fontenc}
\RequirePackage{amsthm}
\RequirePackage[french]{babel}
\RequirePackage[answerdelayed, lastexercise]{exercise}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amsthm}
\RequirePackage{amssymb}
\RequirePackage[framemethod=tikz]{mdframed}
\RequirePackage{tikz, xcolor}
\RequirePackage[inline]{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{stmaryrd}
\RequirePackage[hidelinks,backref]{hyperref}
\RequirePackage{xcolor}
\RequirePackage{cancel}
\RequirePackage{float}
\RequirePackage{answers}
\RequirePackage[siunitx, EFvoltages, european]{circuitikz}
\RequirePackage{caption}
\RequirePackage{subcaption}
\RequirePackage{listings}
\RequirePackage{mhchem}
\RequirePackage{mathtools}
\RequirePackage{chemfig}
\newcounter{Planche}

\renewcommand{\thefootnote}{\textbf{\alph{footnote}}}

\counterwithin*{Exercise}{Planche}
\counterwithin*{footnote}{Planche}

\renewcommand{\ExerciseHeaderNB}{\RNum{\thePlanche}.\theExercise}
\DeclareCaptionLabelFormat{nonumber}{#1}

\fancyfoot[L]{\@title}






\newcommand{\planche}[1][\RNum{\thePlanche}]{
\stepcounter{Planche}
\vfill
\pagebreak
\begin{center}
    \begin{huge} \@date ~-\end{huge}\begin{LARGE} Planche #1 \end{LARGE}
    \end{center}

    \setcounter{figure}{0}
    \setcounter{footnote}{0}
    }





\setlength{\hoffset}{-18pt}        
\setlength{\oddsidemargin}{0pt} % Marge gauche sur pages impaires
\setlength{\evensidemargin}{9pt} % Marge gauche sur pages paires
\setlength{\marginparwidth}{54pt} % Largeur de note dans la marge
\setlength{\textwidth}{481pt} % Largeur de la zone de texte (17cm)
\setlength{\voffset}{-18pt} % Bon pour DOS
\setlength{\marginparsep}{7pt} % Séparation de la marge
\setlength{\topmargin}{0pt} % Pas de marge en haut
\setlength{\headheight}{14pt} % Haut de page
\setlength{\headsep}{10pt} % Entre le haut de page et le texte
\setlength{\footskip}{27pt} % Bas de page + séparation
\setlength{\textheight}{708pt} % Hauteur de la zone de texte (25cm)

\addtolength{\skip\footins}{5pc plus 5pt}

\theoremstyle{definition}
\newtheorem{question}{Question}


\pagestyle{fancy}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}



\fancyhead[R]{\rightmark}
\fancyhead[L]{}

\fancyfoot[R]{\footnotesize Ruben \textsc{Narwa}\\ \href{mailto:ruben.narwa@ens.psl.eu}{ruben.narwa@ens.psl.eu}}
\fancyfoot[C]{\thepage}


% This command ignores the optional argument for itemize and enumerate lists
\newcommand{\inlineitem}[1][]{%
\ifnum\enit@type=\tw@
    {\descriptionlabel{#1}}
  \hspace{\labelsep}%
\else
  \ifnum\enit@type=\z@
       \refstepcounter{\@listctr}\fi
    \quad\@itemlabel\hspace{\labelsep}%
\fi}
\parindent=0pt

\def\restriction#1#2{\mathchoice
              {\setbox1\hbox{${\displaystyle #1}_{\scriptstyle #2}$}
              \restrictionaux{#1}{#2}}
              {\setbox1\hbox{${\textstyle #1}_{\scriptstyle #2}$}
              \restrictionaux{#1}{#2}}
              {\setbox1\hbox{${\scriptstyle #1}_{\scriptscriptstyle #2}$}
              \restrictionaux{#1}{#2}}
              {\setbox1\hbox{${\scriptscriptstyle #1}_{\scriptscriptstyle #2}$}
              \restrictionaux{#1}{#2}}}
\def\restrictionaux#1#2{{#1\,\smash{\vrule height .8\ht1 depth .85\dp1}}_{\,#2}} 

\newenvironment{absolutelynopagebreak}
  {\par\nobreak\vfil\penalty0\vfilneg
   \vtop\bgroup}
  {\par\xdef\tpd{\the\prevdepth}\egroup
   \prevdepth=\tpd}

\newcommand{\ex}{\overrightarrow{e_x}}
\newcommand{\ey}{\overrightarrow{e_y}}
\newcommand{\ez}{\overrightarrow{e_z}}
\newcommand{\ux}{\overrightarrow{u_x}}
\newcommand{\uy}{\overrightarrow{u_y}}
\newcommand{\uz}{\overrightarrow{u_z}}
\newcommand{\ur}{\overrightarrow{u_r}}
\newcommand{\er}{\overrightarrow{e_r}}
\newcommand{\ethet}{\overrightarrow{e_\theta}}
\newcommand{\uthet}{\overrightarrow{u_\theta}}
\newcommand{\RNum}[1]{\uppercase\expandafter{\romannumeral #1\relax}}
\newcommand{\dderiv}[3][]{\frac{\mathrm{d}^{#1}#2}{\mathrm{d}#3^{#1}}}
\newcommand{\pderiv}[3][]{\frac{\partial^{#1}#2}{\partial#3^{#1}}}
\newcommand{\derivat}[2]{\left.#1\right|_{#2}}
\newcommand{\norme}[2][]{\left\| #2\right\|_{#1}}
\newcommand{\cste}{\mathrm{c}^{\mathrm{\underline{st}}}}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\grad}{\ensuremath{\overrightarrow{\text{grad}}}}
\renewcommand{\div}{\ensuremath{\text{div}}}
\newcommand{\rot}{\ensuremath{\overrightarrow{\text{rot}}}}
\renewcommand{\nabla}{\ensuremath{\overrightarrow{\nabla}}} 
\newcommand{\pka}{\ensuremath{\text{p}K_{\mathrm a}}\ }
\newcommand{\ph}{\ensuremath{\text{p}H}\ }
\newcommand{\snu}{\ensuremath{\mathrm{S_N1}}\ }
\newcommand{\snd}{\ensuremath{\mathrm{S_N2}}\ }


\renewcommand\qedsymbol{$\boxtimes$}
\renewcommand{\tan}{\mathrm{tg}}

\renewcommand{\ExerciseName}{Exercice}
\renewcommand{\AnswerHeader}{\medskip\centerline{\textbf{
Réponse de l'exercice \ExerciseHeaderNB \ExerciseHeaderTitle}\smallskip}}
\renewcommand{\DifficultyMarker}{\Large$^\star$\large}
\renewcommand{\ExePartHeader}{
\medskip\centerline{\emph{\large\ExePartHeaderDifficulty\ExePartName%
\ExePartHeaderNB\ExePartHeaderTitle}}}
\renewcommand{\ExePartName}{Partie}
\renewcommand{\ArticleOf}{de\ }


\captionsetup{labelformat = nonumber}
\AtBeginDocument{\def\labelitemi{$\bullet$}}


% For the python style
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{blue},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=4
}

\lstset{style=mystyle}


% \newcommand{\cours}[2]{
%   \begin{center}
%         \begin{tabular}{|c|}
%         \hline
%         #1\\
%         \hline
%         #2\\
%         \hline
%         \end{tabular}
%     \end{center}
% }
% \newcommand{\Cours}[4]{
%   \begin{center}
%         \begin{tabular}{|c|}
%         \hline
%         #1\\
%         \hline
%         #2\\
%         \hline
%         #3\\
%         \hline
%         #4\\
%         \hline
%         \end{tabular}
%     \end{center}
% }

\makeatletter
\newcommand{\cours}[1]{%
    \begin{center}
      \begin{tabular}{|c|}
      \hline
      #1
  \@coursi
}
\newcommand\stopcours

\newcommand\@coursi{\@ifnextchar\stopcours{\@coursfin}{\@coursii}}

\newcommand\@coursii[1]{%
    \\ \hline
    #1 
  \@coursi
}

\newcommand\@coursfin{
  \\ \hline
  \end{tabular}
  \end{center}
}

\newcommand{\chemimageExo}[2]{
  \vspace{10pt}
    {\centering #1
    \captionof{figure}{#2}}
  \vspace{10pt}
}

\newcommand{\imageExo}[3][1]{
  \vspace{10pt}
    {\centering\includegraphics[scale=#1]{#2}
    \captionof{figure}{#3}}
  \vspace{10pt}
}

\newcommand{\pageReponses}{
  \vfill
  \pagebreak
  \hfill
  \begin{minipage}{0.95\textwidth}
  \vskip 2em
  \rule{\linewidth}{0.4pt}
  {\LARGE \centering \textbf{Réponses aux exercices} \par }
  \rule{\linewidth}{0.4pt}
  \vskip 1 em
  {\large \centering \@date \par}
  \end{minipage}
  \vskip 1em \par

\shipoutAnswer
}

\renewcommand{\citation}[2]{\begin{center}
    \textit{ \og #1 \fg{} }
    \end{center}
     \begin{flushright}
     \small #2.
     \end{flushright}
    }

\newcommand{\citationAction}[2]{\begin{center}
    \textit{ *#1* }
    \end{center}
        \begin{flushright}
        \small #2.
        \end{flushright}
    }

\newcommand{\selectexo}[2]{
    \ExerciseSelect[type = #1, label={#2}]
    \protected@edef\tempExercise{\noexpand\input{../Exercices/exercices_#1.auxtex}}%
    \tempExercise
    \ExerciseStopSelect
}

\graphicspath{{../images}}

\makeatother

