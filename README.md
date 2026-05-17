# QSpiders Full Stack Training

This repository is a personal learning workspace for QSpiders full stack training. It collects practice programs, notes, classroom examples, mini projects, and framework experiments across Python, DSA, OOP, Web Technologies, React, Django, and API tooling.

The code is organized by topic rather than as one single production application. Most files are small, standalone examples meant for hands-on practice.

## Repository Overview

```text
.
+-- Python/          Python fundamentals, functions, generators, recursion, files, regex, SQL examples
+-- DSA/             Arithmetic, conditions, loops, patterns, numbers, recursion, arrays, Java operator demos
+-- OOPs/            Object-oriented programming examples plus theory notes and questions
+-- Web Tech/        HTML, CSS, JavaScript lessons, media assets, and browser-based demos
+-- React/           Vite React learning app with component, state, props, list, form, and CSS examples
+-- Django/          Multiple Django practice projects and Django notes
+-- postman/         Postman workspace globals
+-- .postman/        Postman local resources
+-- .github/         GitHub configuration
+-- .vscode/         Editor configuration
```

Current source snapshot, excluding `.git`, `node_modules`, and `__pycache__`, contains about 1,090 tracked learning files.

## Main Topics

### Python

`Python/` contains numbered beginner lessons and additional focused examples:

- Basics such as variables, data types, operators, conditions, loops, strings, lists, tuples, sets, and dictionaries.
- Functions, argument handling, unpacking, generators, recursion, and pattern programs.
- `Python/Advance/` includes file handling, exception handling, regular expressions, packages, SQLite connection practice, and a sample `data.db`.
- Utility/practice files include `calculator.py`, `pattern.py`, `Generator.py`, `fun*.py`, `g*.py`, and `r*.py`.

Run a standalone Python file from the repository root:

```bash
python Python/01.py
python Python/calculator.py
python Python/Advance/file_handling.py
```

Many programs use `input()`, so run them in a terminal.

### Data Structures and Algorithms

`DSA/` contains practice organized by concept:

- `Arithematic/` for basic arithmetic operations.
- `Flow Control Statement/`, `Conditional Operator/`, and `Terniary Operators/` for decision-making practice.
- `While loop- 1/`, `While loop-2/`, and `While loop-3/` for loop-based problems.
- `Pattern/` for a large pattern-printing collection.
- `Number/` for prime, palindrome, Fibonacci, factors, pronic, emirp, fascinating, and related number programs.
- `Recursion/` for recursive functions, including Tower of Hanoi.
- `Array/` and `Extra/` for additional algorithm practice.
- `Increment Decrement/` contains Java examples and compiled `.class` files for operator behavior.

Run Python DSA examples:

```bash
python "DSA/Pattern/1.py"
python "DSA/Number/variousPrime.py"
python "DSA/Recursion/tower_of_hanoi.py"
```

Compile and run Java examples:

```bash
cd "DSA/Increment Decrement"
javac A.java
java A
```

### Object-Oriented Programming

`OOPs/` contains Python examples for OOP concepts and a `Notes And Questions/` folder covering:

- Classes and objects
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Decorators and property decorators
- Class relationships
- Important interview/practice questions

Example:

```bash
python OOPs/1.py
```

### Web Technologies

`Web Tech/` contains browser-based learning material.

`Web Tech/HTML/` covers:

- Basic HTML structure
- Links
- Forms
- Tables
- Audio and video
- Multi-page navigation examples

`Web Tech/CSS/` covers:

- Simple, combinator, pseudo-class, pseudo-element, and attribute selectors
- Box model
- Units and variables
- Text, color, font, and background properties
- Display, overflow, position, flexbox, grid, transitions, and box shadows
- Paired `.html` and `.css` demos plus notes and PDFs

`Web Tech/Java Script/` is organized by day/topic and includes:

- Script loading, scope, `var`/`let`/`const`, execution context, literals, and type coercion
- Functions, hoisting, TDZ, arrow functions, function expressions, and IIFEs
- Arrays, objects, object methods, JSON, DOM, events, keyboard/form events
- `this`, `call`, `apply`, `bind`, timers, debouncing, throttling, promises, and currying

Open HTML demos directly in a browser, for example:

```text
Web Tech/HTML/index.html
Web Tech/CSS/index.html
Web Tech/Java Script/Day 12 - DOM/index.html
```

### React

`React/react-app/` is a Vite React app using React 19 and React Icons. It contains topic-wise components under `src/allTopics/`:

- Function and class components
- State in function/class components
- Props and props drilling
- Callbacks and state uplifting
- Lists
- Controlled forms
- Inline CSS, CSS modules, and component styling

Run the React app:

```bash
cd React/react-app
npm install
npm run dev
```

Useful scripts:

```bash
npm run build
npm run lint
npm run preview
```

### Django

`Django/` contains notes and several Django projects. Projects with `manage.py` include:

- `ArticleProject`
- `AuthProject`
- `CustomAuthentication`
- `DjangoForm`
- `djangorestapi`
- `FeedbackProject`
- `firstProject`
- `ModelProject`
- `ProjectNews`
- `smartTODOManager`
- `template_inheritance`
- `Weather`

There is also `DjangoAPI/`, which contains a Django project structure and example app files.

Common project themes include templates, static files, models, forms, CRUD operations, authentication, custom authentication, weather app practice, article/blog models, feedback forms, REST API apps, and a smart todo manager.

Run a Django project:

```bash
cd Django/smartTODOManager
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

If dependencies are missing, create or activate a virtual environment and install Django-related packages as needed:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install django djangorestframework
```

The repository also contains `Django/myenv/`, but local virtual environments are usually machine-specific and should normally stay ignored.

### Postman

Postman workspace data is stored in:

- `postman/globals/workspace.globals.yaml`
- `.postman/resources.yaml`

Use these files as API testing support material for Django/API lessons.

## Suggested Learning Path

1. Start with `Python/01.py` onward for programming fundamentals.
2. Practice control flow and functions in the later Python files.
3. Move into `DSA/Arithematic/`, conditions, while loops, and patterns.
4. Use `DSA/Number/` and `DSA/Recursion/` for algorithmic problem solving.
5. Study `OOPs/` once Python basics are comfortable.
6. Learn `Web Tech/HTML/`, then `Web Tech/CSS/`, then day-wise JavaScript.
7. Explore `React/react-app/` for component-based frontend development.
8. Work through `Django/Notes/`, then run the Django mini projects.
9. Use Postman resources while testing API-focused Django work.

## Notes for Contributors and Future Updates

- Many files are intentionally small and independent for classroom practice.
- Some directory and file names preserve original spellings, such as `Arithematic`, `Terniary Operators`, and `Java Script`.
- Several generated artifacts are currently present, including `.class`, `__pycache__`, SQLite databases, logs, and Vite lock files.
- Before adding new lessons, prefer placing them inside the matching topic folder with clear names.
- For larger apps, include a local README inside the app folder with setup and route details.

## Quick Commands

```bash
# Python
python Python/01.py

# DSA
python "DSA/Pattern/1.py"

# Java
cd "DSA/Increment Decrement"
javac A.java
java A

# React
cd React/react-app
npm install
npm run dev

# Django
cd Django/smartTODOManager
python manage.py runserver
```

## Status

Last updated: May 17, 2026

This repository is actively updated as full stack training progresses. It is best read as a growing study archive: part notes, part exercise bank, part collection of mini projects.
