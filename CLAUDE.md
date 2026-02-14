# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Project Overview

This is a **Python learning and practice repository** containing educational code examples, coursework exercises, and personal study materials. It covers topics from beginner fundamentals through advanced data science, web automation, and GUI development. The code is organized by course/topic into subdirectories.

- **Language:** Python (100%)
- **Python Version:** 3.9
- **IDE:** PyCharm
- **Purpose:** Personal learning workspace, not a production application

## Repository Structure

```
bwktim/
├── 0.Start_Coding_Python/          # Beginner Python tutorials
├── 1.100Days_of_Python_Codes_from_Udemy/  # Udemy 100 Days of Python course
├── 2.Jupyter_Notebooks/            # Jupyter Notebook exercises
├── Advanced Python Modules/        # Advanced module tutorials
├── Numpy_Practice/                 # NumPy exercises (Jupyter)
├── OneMin_Python/                  # Short Python practice exercises
├── Pandas/                         # Pandas data practice (Jupyter)
├── Pandas-Demo/                    # Pandas demonstrations (Jupyter)
├── PycharmProjects/sparta_python/  # Sparta coding club projects
├── PythonDataWorkspace/Pandas/     # Data analysis workspace
├── Python_Codes/                   # Extensive Python examples (~120 files)
├── Python_Dojang/                  # Python Dojang course materials
├── Python_Programming_Masterclass/ # Masterclass course files
├── Test_Python/                    # Test and experimentation files
├── VENVWORKSPACE/                  # Virtual environment workspace
├── Workspace/                      # General workspace
├── build/Module_Example/           # Build artifacts
├── python-masterclass-remaster-shared/  # Shared masterclass materials
├── python_for_student/             # Main student practice area (~380 files)
├── rpa_basic/1_excel/              # RPA (Robotic Process Automation) basics
└── (root-level scripts)            # Miscellaneous example files
```

## Running Code

There is no build system, task runner, or test framework. Individual scripts are run directly:

```bash
python <filename>.py
```

Jupyter notebooks (`.ipynb` files) are found in multiple directories and should be opened with Jupyter Notebook/Lab or a compatible IDE.

## No Build/Test/Lint Commands

- No `requirements.txt`, `setup.py`, `pyproject.toml`, or `Pipfile`
- No test framework (pytest, unittest) is configured
- No linter or formatter configuration (no flake8, black, pylint, etc.)
- No CI/CD pipelines

## Key Dependencies (used across files)

| Category | Libraries |
|----------|-----------|
| Data Science | `numpy`, `pandas`, `scipy`, `sklearn` |
| Visualization | `matplotlib` |
| Web/Automation | `selenium`, `beautifulsoup4` (bs4), `requests` |
| GUI | `tkinter` (built-in), `turtle` (built-in) |
| File I/O | `openpyxl`, `xlrd`, `csv`, `json`, `pickle` |
| Standard Library | `os`, `re`, `random`, `datetime`, `math`, `threading`, `time` |

## Code Patterns and Conventions

### Organization
- Files are organized by course or topic into subdirectories
- File naming follows topic-based conventions: `class_*.py`, `graph_*.py`, `tk_*.py`, `py##_*.py`
- Comments and variable names appear in both **English and Korean**

### Common Patterns
- **OOP:** Classes with inheritance, operator overloading (`__add__`, `__repr__`, etc.)
- **Data Structures:** Custom implementations of linked lists, BSTs, stacks
- **Functional:** Lambda expressions, `map`/`filter`, list comprehensions, generators
- **File I/O:** Context managers (`with` statements), CSV/JSON/Excel read/write
- **Web Scraping:** Selenium WebDriver + BeautifulSoup pipelines
- **GUI:** Tkinter widgets with grid/pack layout managers

### Style Notes
- No enforced code style; formatting varies across files (learning at different stages)
- Many files are self-contained scripts meant to be run independently
- Some files reference external resources (YouTube tutorials, online courses)

## Important Notes for AI Assistants

1. **This is a learning repository** - code quality and style vary intentionally as it reflects different learning stages. Do not refactor or "clean up" existing code unless explicitly asked.
2. **Bilingual content** - Many comments, variable names, and file names use Korean. Preserve the existing language conventions when editing files.
3. **No test suite** - There are no automated tests to run. Verify changes by running individual scripts.
4. **Self-contained scripts** - Most files are standalone and do not depend on each other. Changes to one file rarely affect others.
5. **Data files** - Some scripts depend on data files (`sample.xlsx`, CSV files in `python_for_student/`). Do not remove or rename these without checking for references.
6. **ChromeDriver** - A `chromedriver` binary exists at the repository root for Selenium scripts. It may be version-specific.
