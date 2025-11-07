import flet as ft

from load_book import load_books, save_books
from show_books import show_books, add_book, delete, update
comandos = {
    "add":"agregar",
    "remove" : "eliminar",
    "update" : "actualizar",
    "list" : "listar" 
}

books = load_books()
def main (page: ft.Page):
    page.title = "biblioteca"
    messages = ft.Column(scroll = True, expand = True, width = page.width)
    def confirm(book,show_details):
        confirmation = ft.Column(
            controls=[
                ft.Text("¿Estás seguro que quieres eliminar el libro?"),
                ft.Row(
                    controls=[
                        ft.Button("SI", on_click=lambda e, b=book: delete(books, b, messages, page)),
                        ft.Button("NO", on_click=lambda e, b=book: show_books(books, show_details))
                    ]
                )
            ]
        )
        messages.controls.append(confirmation)
        page.update()
 
    def show_details(book,list):
        row =  ft.Row(
                    controls = [
                    ft.Image(book["Portada"], width = 350, height = 350),
                    ft.Column(
                        controls=[
                    ft.Text(book["Titulo"]),
                    ft.Text(book["Autor"]),
                    ft.Text(book["comentarios"]),
                    ft.Text(book["calificacion"]),
                    ft.Row(
                        controls=[
                            ft.Button("eliminar", on_click=lambda e, b=book: confirm(b,show_details)),
                            ft.Button("actualizar", on_click=lambda e, b=book: update(books, b, messages, page))
                                ]
                            )
                        ] 
                    )  
                 ]
             )
        list.controls.append(row)
        page.update()
    def add_message(e):
        message = text_area.value.strip()
        if message == "list":
            messages.controls.append(show_books(books, show_details))
        elif message == "add":
           messages.controls.append(add_book(books, messages, page))
        else:
            messages.controls.append(ft.Text(message))
        text_area.value = ""  # limpiar después de enviar
        messages.scroll_to(offset = -1, duration = 1000)
        page.update()
 
    text_area=ft.TextField(
    hint_text="comandos:".join(comandos.keys()),
    multiline= False,
    min_lines=1,
    max_lines=10,
    expand=False,
    height=150,
    on_submit = add_message
    )
    page.add(
        ft.Container(
        expand = True, 
        width = page.width,
        height = page.height,
        content = messages
    ), 
    text_area
    )
ft.app(target=main, view=ft.WEB_BROWSER)




