
def place_treasure(position: str):
    """
    Place 'X' on a 3x3 treasure map using a 2-digit position string (rowcol),
    where row and col are 1..3. Prints the updated map and the resolved indices.
    Returns the updated map (list of lists).
    Example: position='23' -> row 2, column 3.
    """
    # Build a fresh 3x3 map
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    treasure_map = [row1, row2, row3]

    # Basic validation: must be 2 digits between 1 and 3
    if not (isinstance(position, str) and len(position) == 2 and position.isdigit()):
        raise ValueError("Position must be a 2-digit string like '23' with digits 1..3.")

    r = int(position[0])
    c = int(position[1])
    if not (1 <= r <= 3 and 1 <= c <= 3):
        raise ValueError("Row and column must each be between 1 and 3.")

    # Convert to zero-based indices
    r_idx = r - 1
    c_idx = c - 1

    # Place the X
    treasure_map[r_idx][c_idx] = "X"

    # Pretty-print the map
    print(f"Placing X at row {r}, column {c} (zero-based: {r_idx}, {c_idx})")
    print("Current map:")
    # Combine each row into a string for display
    for row in treasure_map:
        print("[" + "|".join(row) + "]")

    return treasure_map


def main():    # Example usage
    position = input("Enter the treasure position (rowcol, e.g., '23' for row 2 column 3): ")
    try:
        place_treasure(position)
    except ValueError as ve:
        print(f"Error: {ve}")   
    
# entry point of the script
if __name__ == "__main__":
    main()