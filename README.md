# DFA Plate Number Validator

**This project is a Deterministic Finite Automaton (DFA) simulator that validates vehicle plate numbers based on a specific format rule:**

### The plate number must follow the format:

3 letters + 3 digits, where the second letter must be a vowel (A, E, I, O, U).

### Features
* Accepts user input via terminal

* Checks each character using DFA state transitions

* Rejects invalid formats with helpful error messages

* Case-insensitive (e.g., cAe123 is valid)

* Includes sample valid/invalid inputs for testing

### Examples

**Valid: CAE123, BOU789, MEI000**

**Invalid: CBZ123 (2nd letter not a vowel), 123456 (starts with digits), CA1E23 (wrong pattern)**

### Use Cases

* Educational tool for learning DFA logic

* Demonstration of automata theory in action

* Lightweight Python-based simulator for validating string patterns
