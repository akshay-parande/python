# Sample assembly program (usually read from a file)
assembly_code = [
    "START 100",
    "LOOP ADD A, B",
    "      SUB C, D",
    "      MOVER BREG, ='5'",
    "      MOVER AREG, ='5'",
    "      ADD BREG, AREG"
    "      MOVEM BREG, Y",
    "      END"
]

# Symbol table, literal table, and machine code table
symbol_table = {}
literal_table = {}
machine_code = []

# Function for Pass-I: Building the symbol and literal tables
def pass1(assembly_code):
    global symbol_table, literal_table
    location_counter = 0

    for line in assembly_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        # Check if the line is a comment or empty
        if parts[0].startswith(';'):
            continue

        # Check if the line contains a label
        if parts[0][-1] == ':':
            label = parts[0][:-1]
            symbol_table[label] = location_counter
            parts = parts[1:]  # Remove the label part from the instruction

        # Handle START directive
        if parts[0] == "START":
            location_counter = int(parts[1])

        # Handle machine instructions
        elif parts[0] in ["ADD", "SUB", "MOVER", "MOVEM"]:
            location_counter += 1  # Assume each instruction is 1 unit length
            
            # Check for literals in operands
            for part in parts[1:]:
                if part.startswith("='") and part.endswith("'"):
                    literal = part
                    if literal not in literal_table:
                        literal_table[literal] = None  # Address to be assigned in Pass-II

        # Handle END directive
        elif parts[0] == "END":
            break

    print("Pass-I complete. Symbol Table and Literal Table created.")

# Function for Pass-II: Generating machine code using the symbol and literal tables
def pass2(assembly_code):
    global symbol_table, literal_table, machine_code
    location_counter = 0

    for line in assembly_code:
        parts = line.split()

        if len(parts) == 0:
            continue

        # Ignore comment lines
        if parts[0].startswith(';'):
            continue

        # Ignore labels (already processed in Pass-I)
        if parts[0][-1] == ':':
            parts = parts[1:]

        # Process START directive
        if parts[0] == "START":
            location_counter = int(parts[1])
            continue

        # Process machine instructions
        if parts[0] in ["ADD", "SUB", "MOVER", "MOVEM"]:
            opcode = {
                "ADD": "01",
                "SUB": "02",
                "MOVER": "03",
                "MOVEM": "04"
            }[parts[0]]

            operands = []
            for part in parts[1:]:
                if part in symbol_table:
                    operands.append(str(symbol_table[part]))
                elif part.startswith("='") and part.endswith("'"):
                    if literal_table[part] is None:
                        literal_table[part] = location_counter
                        location_counter += 1
                    operands.append(str(literal_table[part]))
                else:
                    operands.append(part)

            machine_code.append(f"{opcode} {' '.join(operands)}")
            location_counter += 1

        # Process END directive
        elif parts[0] == "END":
            break

    print("Pass-II complete. Machine code generated.")

# Run Pass-I and Pass-II
pass1(assembly_code)
pass2(assembly_code)

# Display the results
print("\nSymbol Table:")
for symbol, address in symbol_table.items():
    print(f"{symbol} -> {address}")

print("\nLiteral Table:")
for literal, address in literal_table.items():
    print(f"{literal} -> {address}")

print("\nGenerated Machine Code:")
for code in machine_code:
    print(code)
