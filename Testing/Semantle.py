import gensim
import random
import tkinter as tk
from answers import secretWords as answers
from constants import PATH_TO_DATASET

gnews_model = gensim.models.KeyedVectors.load_word2vec_format(PATH_TO_DATASET, binary=True)
possible_words = gnews_model.index_to_key
guessed_words = []
default_chart = []
for i in range(20):
    default_chart.append(("", ""))

gameWindow = tk.Tk()
gameWindow.title("Semantle")
gameTitle = tk.Label(gameWindow, text = "Semantle", font=("Arial Bold", 50))
gameTitle.grid(column=0, row=0)
inputTitle = tk.Label(gameWindow, text = "Input Your Guess:", font = ("Arial Bold", 30))
inputTitle.grid(column=0, row=2)
inputBox = tk.Entry()
inputBox.grid(column=0, row = 5)
blankSpace = tk.Label(text = "")
blankSpace.grid(column=4, row = 5)
similarityScoreText = tk.Label(text = "Similarity Score will appear here")
similarityScoreText.grid(column= 0, row = 7)
chart_frame = tk.Frame(gameWindow)
chart_frame.grid(row = 8, column = 0)

# Creates a static column on the left side of the GUI
#This will hold the respecitve rank of 
static_label = tk.Label(chart_frame, text="No.", width=5, borderwidth=1, relief="solid")
static_label.grid(row=9, column=0, sticky="nsew")


# Add the numbers 1-20 to the static column
rank_label = tk.Label(chart_frame, text="Rank", width = 5, borderwidth= 1, relief = "solid")
rank_label.grid(row = 0, column = 0, sticky = "nsew")
# Add the word "Word" over the list of words
word_label = tk.Label(chart_frame, text = "Word", width = 10, borderwidth= 1, relief = "solid")
word_label.grid(row = 0, column = 1, sticky = "nsew")
#Add the word "Similarity" over the list of similarity scores
similarity_label = tk.Label(chart_frame, text = "Similarity", width = 10, borderwidth= 1, relief = "solid")
similarity_label.grid(row = 0, column = 2, sticky = "nsew")
for i in range(1, 21):
    number_label = tk.Label(chart_frame, text=str(i), width=5, borderwidth=1, relief="solid")
    number_label.grid(row=i, column=0, sticky="nsew")

for i, (word, number) in enumerate(default_chart):
    word_label = tk.Label(chart_frame, text=word, width=15, borderwidth=1, relief="solid")
    word_label.grid(row=i+1, column=1, sticky="nsew")
    
    number_label = tk.Label(chart_frame, text=number, width=5, borderwidth=1, relief="solid")
    number_label.grid(row=i+1, column=2, sticky="nsew")
    
    # Add a bit of padding between rows
    chart_frame.grid_rowconfigure(i+1, minsize=5)
    
# Configure the columns to expand to fill available space
chart_frame.grid_columnconfigure(0, weight=1)
chart_frame.grid_columnconfigure(1, weight=2)
chart_frame.grid_columnconfigure(2, weight=2)

mystery_word = answers[random.randint(0, len(answers))]
print("The mystery word is", mystery_word) 


#Main Game Loop 
def clicked(event=None):
    global guessed_words
    guess_word = inputBox.get().lower()
    #If the user inputed a valid word in our large dataset
    #This should be equivalent to checking for a valid english word
    if(not guess_word == mystery_word):
        if(guess_word in possible_words):
            similarity_score = round(100 * gnews_model.similarity(guess_word, mystery_word), 6)
            similarityScoreText.config(text = str(similarity_score))
            guessed_words.append((guess_word, similarity_score))
            guessed_words = sorted(guessed_words, key=lambda x: x[1])
            guessed_words.reverse()
            for i, (word, number) in enumerate(guessed_words):
                if(i < 20):
                    label_to_change = chart_frame.grid_slaves(row=i + 1, column=1)[0]
                    label_to_change.config(text= str(word))
                    label_to_change = chart_frame.grid_slaves(row=i + 1, column=2)[0]
                    label_to_change.config(text= str(number))
            inputBox.delete(0, tk.END)
        #Invalid word inputed 
        else:
            similarityScoreText.config(text = "Invalid Word, Try Again")
            inputBox.delete(0, tk.END)
    else: 
       similarityScoreText.config(text = "You Win!")

inputButton = tk.Button(text = "Submit", command = clicked)
inputButton.grid(column = 1, row = 5)
gameWindow.bind('<Return>', clicked)
gameWindow.mainloop()