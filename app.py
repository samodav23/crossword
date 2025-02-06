import random
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
    
    grid_size = 12  # Grila mai mare pentru cuvantul ascuns
    grid = [['' for _ in range(grid_size)] for _ in range(grid_size)]
    solutions = [['' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Plasam cuvantul ascuns "Te Iubesc"
    hidden_word = "TEIUBESC"
    hidden_column = 5  # Pozitia coloanei pentru "Te Iubesc"
    
    for i, letter in enumerate(hidden_word):
        grid[i][hidden_column] = ' '
        solutions[i][hidden_column] = letter
    
    # Plasam restul cuvintelor
    placed_words = []
    for word in words.keys():
        placed = False
        attempts = 0
        
        while not placed and attempts < 50:
            direction = random.choice(["H", "V"])
            row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            
            if direction == "H" and col + len(word) <= grid_size:
                if all(grid[row][col + i] in ['', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = ' '
                        solutions[row][col + i] = word[i]
                    placed = True
            elif direction == "V" and row + len(word) <= grid_size:
                if all(grid[row + i][col] in ['', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = ' '
                        solutions[row + i][col] = word[i]
                    placed = True
            attempts += 1
        
        if placed:
            placed_words.append(word)
    
    return grid, solutions, words, hidden_column

def draw_crossword():
    grid, solutions, words, hidden_column = create_crossword()
    
    st.title("Crucișeul Interactiv")
    st.write("Completează grila pentru a descoperi replica ascunsă!")
    
    correct = True

    for r in range(len(grid)):
        cols = st.columns(len(grid[r]))
        for c in range(len(grid[r])):
            if solutions[r][c]:
                if c == hidden_column:
                    cols[c].text_input("", key=f"cell_{r}_{c}", max_chars=1, disabled=True, value=solutions[r][c])
                else:
                    user_input = cols[c].text_input("", key=f"cell_{r}_{c}", max_chars=1).upper()
                    if user_input != solutions[r][c]:
                        correct = False
            else:
                cols[c].text(" ")
    
    st.subheader("Indicii:")
    for word, clue in words.items():
        st.write(f"**{word}**: {clue}")

    user_message = st.text_input("Scrie aici replica ascunsă completată:")

    if st.button("Verifică răspunsurile"):
        if correct and user_message == "TE IUBESC":
            st.success("Felicitări! Ai descoperit replica ascunsă: 'Te Iubesc'!")
            st.write("❤️ Do you want to be my valentine? ❤️")
        elif correct:
            st.warning("Ai completat corect grila, dar nu ai scris corect replica ascunsă!")
        else:
            st.error("Unele răspunsuri sunt greșite. Mai încearcă!")

if __name__ == "__main__":
    draw_crossword()
