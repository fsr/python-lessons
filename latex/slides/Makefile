FILES=01_getting_started 02_grundlagen 03_builtins 04_modules_packages_pip 05_decorators 06_comprehensions 07_functions_advanced 08_process 09_web_client 10_regex 11_smtplib 12_curses

# atom regex replacer
# $1: $1.tex\n	pdflatex -jobname=build/$1 $1.tex

01_getting_started: 01_getting_started.tex
	pdflatex -jobname=build/01_getting_started 01_getting_started.tex
02_grundlagen: 02_grundlagen.tex
	pdflatex -jobname=build/02_grundlagen 02_grundlagen.tex
03_builtins: 03_builtins.tex
	pdflatex -jobname=build/03_builtins 03_builtins.tex
04_modules_packages_pip: 04_modules_packages_pip.tex
	pdflatex -jobname=build/04_modules_packages_pip 04_modules_packages_pip.tex
05_decorators: 05_decorators.tex
	pdflatex -jobname=build/05_decorators 05_decorators.tex
06_comprehensions: 06_comprehensions.tex
	pdflatex -jobname=build/06_comprehensions 06_comprehensions.tex
07_functions_advanced: 07_functions_advanced.tex
	pdflatex -jobname=build/07_functions_advanced 07_functions_advanced.tex
08_process: 08_process.tex
	pdflatex -jobname=build/08_process 08_process.tex
09_web_client: 09_web_client.tex
	pdflatex -jobname=build/09_web_client 09_web_client.tex
10_regex: 10_regex.tex
	pdflatex -jobname=build/10_regex 10_regex.tex
11_smtplib: 11_smtplib.tex
	pdflatex -jobname=build/11_smtplib 11_smtplib.tex
12_curses: 12_curses.tex
	pdflatex -jobname=build/12_curses 12_curses.tex

all: $(FILES)
default: all
clean:
	@#the touch is just so that rm does not complain when nothing of the given pattern is found and the pattern is given to rm directly
	@cd build; \
	touch __rm.aux \
		__rm.log \
		__rm.out \
		__rm.nav \
		__rm.snm \
		__rm.toc \
		__rm.vrb; \
	rm  *.aux \
		*.log \
		*.out \
		*.nav \
		*.snm \
		*.toc \
		*.vrb
