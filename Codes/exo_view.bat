@echo off
setlocal enabledelayedexpansion

rem If -type is offered
if "%1"=="-type" (
    set type=
    :loop2
    if "%2"=="" goto typewrite
    set type=%type% %2
    shift
    goto loop2
)


rem Loop through all exercises labels
set params=
:loop
if "%1"=="" goto exwrite
set params=%params% %1
shift
goto loop



:exwrite
python output_pdfexo.py %params%
goto compile


:typewrite
python output_pdftype.py %type%
goto compile

:compile
pdflatex temp.tex
echo "done"

timeout /t 3 /nobreak

rem delete auxiliary files
del temp.log
del temp.synctex.gz
del texput.fls 
del temp.aux 
del temp.out

rem view pdf (change the path to your pdf viewer path)
code "C:\Users\mrawr\Documents\LaTek Files\Kholles PSCI 2324\Codes\temp.pdf"