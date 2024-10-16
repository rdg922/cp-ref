import os
import re

source_directory = './content'  # Directory where your .h and .cpp files are located
output_latex_file = './pdf/compiled_document.tex'

latex_preamble = r"""
\documentclass[10pt]{article}
\usepackage{blindtext}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{multicol}
\usepackage{needspace}  % Import the needspace package
\setlength{\columnsep}{1cm}
% Adjusted margins to be smaller
\geometry{landscape, left=0.5in, right=0.5in, top=0.5in, bottom=0.5in}

% Define custom colors
\definecolor{keywordcolor}{rgb}{0,0,1}
\definecolor{stringcolor}{rgb}{0.6,0.1,0.1}
\definecolor{commentcolor}{rgb}{0,0.5,0}

\lstset{
    language=C++,                   % Specify C++ language
    basicstyle=\footnotesize\ttfamily,
    keywordstyle=\color{keywordcolor}\bfseries,
    stringstyle=\color{stringcolor},
    commentstyle=\color{commentcolor}\itshape,
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=10pt,
    tabsize=2,
    breaklines=true,
    breakatwhitespace=true,         % Break lines at whitespace
    prebreak=\space,                % Add space before line break
    postbreak=\space,               % Add space after line break
    showstringspaces=false,
    captionpos=b
}
\author{Rohit Dasgupta}
\begin{document}
\begin{multicols*}{3}
"""

latex_closing = r"""
\end{multicols*}
\end{document}
"""

def escape_latex(s):
    """
    Escapes LaTeX special characters from a given string.
    """
    return re.sub(r"([&%$#_{}~^\\])", r"\\\1", s)

def process_header_files(directory):
    """
    Process each .h and .cpp file in the directory, converting it to a LaTeX formatted string,
    organizing them into sections based on folder structure.
    """
    contents = []
    for root, dirs, files in sorted(os.walk(directory), key=lambda x: x[0]):
        # Get the relative path from the source directory
        rel_dir = os.path.relpath(root, directory)
        depth = rel_dir.count(os.sep)

        # Skip the root directory itself if you don't want a section for it
        if rel_dir != '.':
            # Determine the appropriate section level based on directory depth
            section_command = {
                0: '\\section',
                1: '\\subsection',
                2: '\\subsubsection',
                3: '\\paragraph',
                4: '\\subparagraph'
            }.get(depth, '\\subparagraph')

            # Escape the directory name for LaTeX
            section_title = escape_latex(os.path.basename(root))
            # Add the section to the contents
            contents.append(f"{section_command}*{{{section_title}}}")
            # Prevent page break between section heading and content
            contents.append("\\nopagebreak[4]")

        # Sort files to ensure they are in order
        files = sorted(files)
        for file in files:
            if file.endswith('.h') or file.endswith('.cpp'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    file_content = f.read()
                    # Escape the file name for LaTeX
                    file_title = escape_latex(file)
                    # Use subsection for files
                    file_section_command = {
                        0: '\\subsection',
                        1: '\\subsubsection',
                        2: '\\paragraph',
                        3: '\\subparagraph',
                        4: '\\subparagraph'
                    }.get(depth, '\\subparagraph')

                    # Reserve space for the title and code block (at least 5 lines)
                    contents.append("\\Needspace{10\\baselineskip}")
                    contents.append(f"{file_section_command}*{{{file_title}}}")
                    # Prevent page break between file heading and code
                    contents.append("\\nopagebreak[4]")
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
