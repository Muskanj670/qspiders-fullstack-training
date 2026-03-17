# QSpider Learning Repository

A comprehensive **educational learning repository** containing programming fundamentals and data structures & algorithms across multiple languages. Files are organized progressively by difficulty level, from basics to intermediate concepts.

## 📚 Repository Structure

### Python Fundamentals (`Python/`)
Complete progression from basics to advanced programming (47+ files)
- **01.py - 14.py**: Core basics (variables, data types, operators, conditionals)
- **15.py - 25.py**: Control flow (loops, break, continue)
- **26.py - 40.py**: Functions and pattern printing
- **41.py - 47.py**: Advanced concepts (generators, recursion, variable arguments)
- **Generator.py**: Generator functions and yield keyword concepts
- **r1.py - r5.py**: Recursion examples and factorial calculations
- **fun1.py - fun6.py**: Function practice exercises
- **pattern.py, extra.py, extra2.py**: Practice exercises
- **calculator.py**: Calculator implementation
- **unpacking.py**: Variable unpacking concepts

Each file builds on previous concepts with progressive complexity.

### Data Structures & Algorithms (`DSA/`)

#### Arithmetic Operations (`DSA/Arithematic/`)
- Basic arithmetic operations using Python fundamentals
- Files: 1.py - 6.py

#### Flow Control Statements (`DSA/Flow Control Statement/`)
- If-else, switch-case concepts and practice
- Files: 2.py, 6.py - 9.py
- PDF: Flow Control Statement concepts

#### Increment/Decrement (`DSA/Increment Decrement/`)
- Java demonstrations of pre/post increment concepts
- Files: A.java - N.java
- Concepts: `++var` vs `var++`, assignment operators, comparison

#### Conditional Operators (`DSA/Conditional Operator/`)
- Ternary operators and conditional expressions
- Files: 1.py, 2.py, 3.py, 4.py, 5.py, 7.py, 15.py, 17.py, 19.py

#### While Loops
**While loop-1/** (Basic while loop patterns)
- 18 practice files (1.py - 18.py)
- Simple loops, counters, conditions

**While loop-2/** (Intermediate patterns)
- 20 practice files (1.py - 20.py)
- Nested loops, pattern generation

**While loop-3/** (Advanced patterns)
- Complex pattern printing and algorithmic problems
- Files: 1.py - 36.py (with gaps)

### Web Technologies (`Web Tech/`)

#### HTML Fundamentals
- Basic structure and semantic tags
- Forms, tables, audio/video elements
- Linking between pages
- Files: index.html, Demo1.html, forms.html, table.html, etc.

#### CSS Styling
- **01_simpleSelector.html**: Element, class, ID selectors
- **02.combinatorSelector.html**: Adjacent, child, descendant combinators
- **03_PsuedoclassSelector.html**: :hover, :active, :focus states
- **04_PsuedoElementSelector.html**: ::before, ::after pseudo-elements
- **06_BoxModel.html**: Margin, padding, border concepts
- **07_cssUnits.html**: CSS measurement units (px, em, rem, etc.)
- **08_cssVariables.html**: CSS custom properties and variables
- **Day 1 Attribute Selector/**: CSS attribute selectors ([type="text"], etc.)
- **Day 2 Color Property/**: Color values (hex, rgb, rgba, hsl)
- **Day 2 Font Property/**: Font-family, size, weight, style
- **Day 3 Background Property/**: Background images, gradients, positioning
- **boxShadow.html, Grid.html**: Advanced styling techniques
- Paired CSS files for practical demonstrations

## 🚀 How to Run Files

### Python Files
Each file is standalone and executable via terminal:
```bash
python filename.py
```
Many files use `input()` for user interaction—follow terminal prompts.

**Examples:**
```bash
python Python/01.py          # Hello World
python DSA/While\ loop-1/1.py  # While loop exercise
python DSA/Arithematic/1.py   # Arithmetic operations
```

### Java Files
Compile and run:
```bash
javac Filename.java
java Filename
```

**Examples:**
```bash
javac DSA/Increment\ Decrement/A.java
java A
```

### HTML/CSS Files
Open directly in a web browser:
```bash
# On Windows, right-click and select "Open with" → your browser
# Or drag the HTML file into your browser window
```

## 📝 Code Style & Conventions

### Python
- Comments use **"WAP"** prefix: `#WAP TO PRINT HELLO WORLD`
- Heavy use of `input()`/`print()` for interactivity
- UPPERCASE for constants: `NAME = input("Enter name: ")`
- Descriptive variable names: `NUM1`, `LENGTH`, `BREADTH`
- Minimal imports; focuses on core language features

### Java
- Simple standalone classes (no packages)
- Always includes `public static void main()` entry point
- Demonstrates specific concepts (operators, control flow)
- Minimal use of external libraries

### HTML/CSS
- Standard HTML5 doctype and meta tags
- Comments mark feature regions: `<!-- TEXT FORMATTING TAG -->`
- CSS imported via `<link>` tags in HTML files
- Inline demonstrations of concepts

## 📖 Learning Path

1. **Start with Python/01.py through Python/14.py** — Language fundamentals
2. **Move to Python/15.py onwards** — Control flow and functions
3. **Python/Generator.py, r1.py-r5.py** — Advanced concepts (generators, recursion)
4. **Parallel: DSA/Arithematic/** — Basic operations reinforcement
5. **DSA/Flow Control Statement/** — Conditional statements
6. **DSA/Increment Decrement/** — Java-based operator concepts
7. **DSA/While loop-1, 2, 3/** — Progressive loop complexity
8. **Web Tech/HTML/** — Markup fundamentals
9. **Web Tech/CSS/** — Styling progression (selectors → box model → properties)

## 📌 Important Notes

- **No external dependencies** — All code uses built-in language features only
- **Files are independent** — Each file solves one problem; no module interconnections
- **Naming preserved** — Some files have typos (e.g., `2,py`) preserved as-is for historical accuracy
- **Interactive learning** — Python files expect terminal input for hands-on practice
- **Educational focus** — Code prioritizes clarity and teaching over optimization
- **PDF resources** — Additional conceptual materials included in relevant directories

## 📚 Additional Resources

- [DSA/Notes.txt](DSA/Notes.txt) — Conceptual notes on logical operators and patterns
- [Python/Notes.txt](Python/Notes.txt) — Python-specific notes and concepts
- [Web Tech/CSS/Notes.txt](Web Tech/CSS/Notes.txt) — CSS styling notes
- PDF files included in relevant directories for additional learning materials
- Each section builds progressively; refer to earlier files if concepts need review

---

**Status**: Actively updated as learning progresses through QSpider training.  
**Last Updated**: March 16, 2026  
**Recent Additions**: Generators, recursion, advanced CSS properties, flow control statements
