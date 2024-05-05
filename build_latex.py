import os
import re

source_directory = './content'  # Directory where your .h files are located
output_latex_file = './pdf/compiled_document.tex'

latex_preamble = """
\\documentclass[9pt]{article}
\\usepackage{blindtext}
\\usepackage{listings}
\\usepackage{geometry}
\\usepackage{multicol}
\\setlength{\columnsep}{1cm}
\\geometry{landscape, margin=1in}
\\lstset{
    basicstyle=\\footnotesize\\ttfamily,
    breaklines=true,
    keepspaces=true,
    tabsize=2
}
\\title{Ropack}
\\author{Rohit Dasgupta}
\\begin{document}
\\maketitle
\\begin{multicols*}{3}

"""

latex_closing = """
\\end{multicols*}
\\end{document}
"""

def escape_latex(s):
    """
    Escapes LaTeX special characters from a given string.
    """
    # return re.sub(r"([&%$#_{}])", r"\\\1", s)
    return s

def process_header_files(directory):
    """
    Process each .h file in the directory, converting it to a LaTeX formatted string.
    """
    contents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.h') or file.endswith('.cpp'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    file_content = f.read()
                    contents.append(f"\\section*{{{os.path.basename(file_path)}}}")
                    contents.append("\\begin{lstlisting}")
                    contents.append(file_content)
                    contents.append("\\end{lstlisting}")
    return "\n".join(contents)

def main():
    latex_content = process_header_files(source_directory)
    with open(output_latex_file, 'w') as f:
        f.write(latex_preamble)
        f.write(latex_content)
        f.write(latex_closing)

if __name__ == "__main__":
    main()
