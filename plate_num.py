def is_vowel(c):
    return c.upper() in 'AEIOU'

def dfa_plate_checker(plate):
    plate = plate.upper()

    if len(plate) != 6:
        return False, "Invalid length: must be 6 characters"

    L1, L2, L3 = plate[0], plate[1], plate[2]
    D1, D2, D3 = plate[3], plate[4], plate[5]

    # q0: First letter
    if not L1.isalpha():
        return False, "First character must be a letter"

    # q1: Second letter must be a vowel
    if not L2.isalpha():
        return False, "Second character must be a letter"
    if not is_vowel(L2):
        return False, "Second letter must be a vowel (A, E, I, O, U)"

    # q2: Third letter
    if not L3.isalpha():
        return False, "Third character must be a letter"

    # q3-q5: Digits
    if not D1.isdigit():
        return False, "Fourth character must be a digit"
    if not D2.isdigit():
        return False, "Fifth character must be a digit"
    if not D3.isdigit():
        return False, "Sixth character must be a digit"

    return True, "Valid plate number"

# Console loop
def run_simulator():
    print("Plate Number DFA Simulator")
    print("Format: 3 letters + 3 digits (2nd letter must be a vowel)")

    while True:
        plate = input("\nEnter a plate number (or type 'exit' to quit): ").strip()
        if plate.lower() == 'exit':
            print("Goodbye!")
            break

        valid, message = dfa_plate_checker(plate)
        print(f"Result: {message}")

# Run the app
run_simulator()
