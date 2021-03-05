from tkinter import *
from tkinter import font
from textblob import TextBlob


root = Tk()

root.configure(bg="Pink")

root.title("Spell_Corrector")
my_font = font.Font(family='courier' ,size=13, weight='bold', slant='italic')
my_fon = font.Font(family='courier' ,size=13, weight='bold', slant='roman')

Title = Entry(root, width=35, fg='red', bg='yellow')
Title['font'] = my_fon
Title.grid(row=1, column=8)
Title.insert(5, '      Welcome to spell corrector')

label_correct = Entry(root, width=15, fg='blue', bg='yellow')
label_correct['font'] = my_font
label_correct.grid(row=5, column=3)
label_correct.insert(5, ' Correct_word')


result_box_1 = Entry(root, width=40, borderwidth=3, fg='blue')
result_box_1['font'] = my_font
result_box_1.grid(row=5, column=8, padx=50, pady=20)

def spell_checker():
    my_font = font.Font(family='courier' ,size=13, weight='bold', slant='italic')
    entry_word = entry_box.get()
    corrected_word = TextBlob(entry_word)
    corrected_word = corrected_word.correct()
    corrected_word = corrected_word.title()
    
    label_correct = Entry(root, width=15, fg='blue', bg='yellow')
    label_correct['font'] = my_font
    label_correct.grid(row=5, column=3)
    label_correct.insert(5, ' Correct_word')
    
    result_box_1 = Entry(root, width=40, borderwidth=3, fg='blue')
    result_box_1['font'] = my_font
    result_box_1.grid(row=5, column=8, padx=50, pady=20)
    result_box_1.insert(5, corrected_word)
    
    
    def Check_again():
        entry_box.delete(0, END)
    
        result_box_1.delete(0, END)
        
    button_clear = Button(root, text='Reset', fg='red', command=Check_again)
    button_clear['font'] = my_font
    button_clear.grid(row=9, column=8, padx=20, pady=20)
  

    
def Check_again():
    entry_box.delete(0, END)
    
    result_box_1.delete(0, END)
        
button_clear = Button(root, text='Reset', fg='red', command=Check_again)
button_clear['font'] = my_font
button_clear.grid(row=9, column=8, padx=20, pady=20)    
    
label_wrong = Entry(root, width=13, fg='blue', bg='yellow')
label_wrong['font'] = my_font
label_wrong.grid(row=3, column=3)
label_wrong.insert(5, "  Enter word")



entry_box = Entry(root, width=40,borderwidth=5, fg='blue')
entry_box['font'] = my_font
entry_box.grid(row=3, column=8, padx=50, pady=20)


search_button = Button(root, text='Check', fg='red', command=spell_checker)
search_button['font'] = my_font
search_button.grid(row=4, column=8)

root.mainloop()