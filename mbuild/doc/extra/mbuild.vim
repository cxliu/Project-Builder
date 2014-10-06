" to use this file, copy mbuild.vim in your .vim/syntax/... folder
" you might want to add this line to your vimrc file
" au BufNewFile,BufRead *.mb set syntax=mbuild
" or set :set syntax=mbuild by hand 


:syn match Comment "#.*"

:syn match Special "\\\n"

:syn region Keyword start=+@+ end=+ +
:syn region Special start=+(+ end=+)+
:syn region Special start=+\[+ end=+\]+
:syn region String start=+[pr]\?"+ end=+"+
:syn region String start=+[pr]\?'+ end=+'+

