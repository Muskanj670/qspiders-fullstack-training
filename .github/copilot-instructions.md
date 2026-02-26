# Copilot Instructions for Qspider Learning Repository

## Project Overview
This is an **educational learning repository** containing programming fundamentals across multiple languages:
- **Python**: Progressive lessons from basics to intermediate (43+ files in `Python/`, DSA algorithms)
- **Java**: Pointer/increment-decrement concepts in `DSA/Increment Decrement/`
- **Web Tech**: HTML/CSS fundamentals in `Web Tech/`
- **DSA**: Data structures & algorithms with loops, arithmetic operations

No external dependencies, build systems, or complex infrastructure—each file is standalone and executable.

## File Organization & Naming Conventions

### Numbered Progressive Learning
- Files are numbered sequentially (01.py, 02.py... 43.py, etc.) indicating **progressive difficulty**
- Higher numbers = more advanced concepts
- First few files in each section teach basics; later files combine concepts
- Example: `Python/01.py` (Hello World) → `Python/40.py` (pattern printing)

### Folder Structure by Topic
- `DSA/Arithmetic/` - Basic arithmetic operations (Python)
- `DSA/Increment Decrement/` - Post/pre increment concepts (Java)
- `DSA/While loop-1,2,3/` - While loop variations (numbered exercises)
- `Python/` - Complete Python basics progression
- `Web Tech/HTML/` & `Web Tech/CSS/` - Web markup and styling

### Naming Issues to Preserve
- Some files have typos (e.g., `2,py` instead of `2.py`)—preserve these as-is, don't rename
- `While loop-3/` folders use dashes in folder names—maintain this convention

## Code Style & Patterns

### Python Files
- Comments use **"WAP"** prefix: `#WAP TO PRINT HELLO WORLD`
- Heavy use of `input()`/`print()` for user interaction
- Variables named descriptively: `NAME`, `NUM1`, `NUM2`, `LENGTH`, `BREADTH`
- UPPERCASE for constants: `NAME = input(...)`
- Minimal imports; focus on core language features
- Examples: [Python/01.py](Python/01.py), [DSA/While loop-3/1.py](DSA/While%20loop-3/1.py)

### Java Files
- Simple class definitions demonstrating single concepts
- Always include `public static void main()` entry point
- Focus on operator behavior (increment, decrement, comparison)
- Examples: [DSA/Increment Decrement/A.java](DSA/Increment%20Decrement/A.java)

### HTML/CSS Files
- Standard HTML5 doctype and meta tags
- Inline demonstrations of concepts
- CSS files paired with HTML files (e.g., `task1.html` + `task1.css`)
- Comments show feature regions (`<!-- TEXT FORMATING TAG -->`)
- Examples: [Web Tech/HTML/index.html](Web%20Tech/HTML/index.html), [Web Tech/CSS/01_simpleSelector.html](Web%20Tech/CSS/01_simpleSelector.html)

## How to Work with This Codebase

### Execution
- **Python**: Run directly with `python filename.py`—each file is self-contained with I/O prompts
- **Java**: Compile with `javac` then run with `java ClassName`—no packages used
- **HTML/CSS**: Open in browser; CSS files imported via `<link>` tags
- No build commands, test runners, or CLIs needed

### When Modifying Files
- **Preserve existing comments** with "WAP" prefix—they document intent
- **Keep files standalone**—don't add imports unless absolutely necessary
- **Maintain UPPERCASE variables** for constants following existing style [Python/01.py](Python/01.py)
- **Test by running individually** (`python file.py` or opening HTML in browser)

### Notes Documentation
- [DSA/Notes.txt](DSA/Notes.txt) contains conceptual notes (e.g., logical operators explanation)
- Reference when adding related exercises (e.g., adding logical operator code after reading notes)

## Key Constraints & Assumptions

1. **No External Dependencies**: All code uses only built-in language features
2. **Educational Focus**: Code prioritizes clarity/teaching over efficiency or robust error handling
3. **I/O Heavy**: Python files expect terminal input; they're interactive learning tools
4. **No Packaging**: Java files are single classes with no package declarations
5. **Independent Files**: Each file solves one problem—don't create interconnected modules
6. **No Version Control Ignored Files**: .gitignore may not exist; all files are tracked

## Special Patterns to Follow

- **Arithmetic section**: Focus on basic operators (+, -, *, /, %, //)
- **Increment/Decrement**: Demonstrate post-increment (`a++`) vs pre-increment (`++a`) behavior
- **While loops**: Cover counters, conditions, and break/continue where appropriate
- **Web Tech HTML**: Use semantic tags, proper nesting, and comments for different sections
- **Web Tech CSS**: Demonstrate selectors (simple, combinator, pseudo-class, pseudo-element) progressively

## Related Documentation
- Conceptual explanations in [DSA/Notes.txt](DSA/Notes.txt) for logical operator logic and patterns
