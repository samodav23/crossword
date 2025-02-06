import streamlit as st

def create_crossword():
    words = {
        "SHAKESPEARE": "Cel mai bun scriitor din lume",
        "CORESI": "Primul loc in care ne-am vazut",
        "SCHEI": "Cel mai romantic cartier din Brasov",
        "BOTEZ": "Unde se bea prosecco?",
        "OLI": "Cei mai draguti copii",
        "ITALIA": "Prima noastra vacanta!!!",
        "COPAC": "Unde ii place lui Oli prea mult sa stea",
        "STAR": "Unde ne-am pupat prima oara ?"
    }

    hidden_word = "TEIUBESC"
    grid_size = 12
    grid = [["" for _ in range(grid_size)] for _ in range(grid_size)]

    # Place the hidden word "TE IUBESC" vertically in the center
    hidden_col = 5
    for i, letter in enumerate(hidden_word):
        grid[i][hidden_col] = letter

    # Place words horizontally to intersect with "TE IUBESC"
    word_positions = {
        "SHAKESPEARE": (0, 0),
        "CORESI": (1, 0),
        "SCHEI": (2, 0),
        "BOTEZ": (3, 0),
        "OLI": (4, 0),
        "ITALIA": (6, 0),
        "COPAC": (7, 0),
        "STAR": (8, 0),
    }

    for word, (row, start_col) in word_positions.items():
        for i, letter in enumerate(word):
            grid[row][start_col + i] = letter

    return grid, words

def draw_crossword():
    grid, words = create_crossword()

    st.title("Crucișeul Interactiv")
    st.write("Completează grila pentru a descoperi replica ascunsă!")

    # Create a form for the crossword
    form = st.form(key="crossword_form")
    user_grid = []

    for row_idx, row in enumerate(grid):
        cols = form.columns(len(row))
        user_row = []
        for col_idx, cell in enumerate(row):
            if cell == "":
                user_input = cols[col_idx].text_input("", key=f"cell_{row_idx}_{col_idx}", max_chars=1).upper()
                user_row.append(user_input)
            else:
                cols[col_idx].text(cell if row_idx == 0 or col_idx == 5 else "")
                user_row.append(cell)
        user_grid.append(user_row)

    submitted = form.form_submit_button("Verifică răspunsurile")

    if submitted:
        correct = True
        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                if cell != "" and cell != user_grid[row_idx][col_idx]:
                    correct = False

        if correct:
            st.success("Felicitări! Ai descoperit replica ascunsă: 'Te Iubesc'!")
            st.write("❤️ Do you want to be my valentine? ❤️")
        else:
            st.error("Unele răspunsuri sunt greșite. Mai încearcă!")

if __name__ == "__main__":
    draw_crossword()
