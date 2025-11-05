import json 
def load_books():
    with open("libros.json", "r", encoding="utf-8") as file:
        books = json.load(file)

    return books 

def save_books(books):
    with open("libros.json", "w", encoding="utf-8") as files:
        json.dump(books,files)




