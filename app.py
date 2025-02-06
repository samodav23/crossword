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

    # Configurăm pozițiile pentru literele din "Te Iubesc"
    hidden_word = "TEIUBESC"
    hidden_column = 5  # Coloană fixă pentru "Te Iubesc"
    hidden_positions = [(i, hidden_column) for i in range(len(hidden_word))]

    return words, hidden_word, hidden_positions

def draw_crossword():
    words, hidden_word, hidden_positions = create_crossword()

    st.title("Crucișeul Interactiv")
    st.write("Completează cuvintele pe rândurile afișate pentru a descoperi replica ascunsă!")

    # Spațiu pentru inputuri
    user_inputs = {}

    for word_index, (word, clue) in enumerate(words.items()):
        st.subheader(f"{word_index + 1}. {clue}")
        user_input = st.text_input(f"Scrie răspunsul pentru indiciul {word_index + 1}", key=f"word_{word_index}").upper()
        user_inputs[word] = user_input

    # Verificăm dacă toate cuvintele sunt corecte și aliniem literele
    correct = True
    grid = [["" for _ in range(12)] for _ in range(12)]

    for word_index, (word, _) in enumerate(words.items()):
        if user_inputs[word] == word:
            # Plasăm literele pe rânduri
            for i, letter in enumerate(word):
                grid[word_index][i] = letter
        else:
            correct = False

    # Construim "Te Iubesc" din literele plasate
    for i, (row, col) in enumerate(hidden_positions):
        if grid[row][col] == hidden_word[i]:
            continue
        else:
            correct = False

    # Afișăm grila pentru verificare
    st.write("### Grila ta completată:")
    for row in grid:
        st.text(" ".join(row))

    # Verificăm dacă totul este corect
    if st.button("Verifică răspunsurile"):
        if correct:
            st.success("Felicitări! Ai descoperit replica ascunsă: 'Te Iubesc'!")
            st.write("❤️ Do you want to be my valentine? ❤️")
        else:
            st.error("Unele răspunsuri sunt greșite. Mai încearcă!")

if __name__ == "__main__":
    draw_crossword()
