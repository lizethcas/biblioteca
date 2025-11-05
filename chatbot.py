import flet as ft
import os
import json
from load_book import load_books, save_books
from show_books import show_books, add_book
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
    
    def update(book):
        print(book)
        titulo =  ft.TextField( label = "titulo", value = book ["Titulo"])
        autor =  ft.TextField(label = "Autor", value = book ["Autor"])
        portada = ft.TextField(label = "Portada", value = book ["Portada"])
        comentarios = ft.TextField(label = "comentarios", value = book ["comentarios"])
        calificacion = ft.TextField(label = "calificacion", value = book ["calificacion"])
        def on_save(e):
            data = {
            "Titulo" : titulo.value,
            "Autor" : autor.value,
            "Portada" : portada.value,
            "comentarios" : comentarios.value,
            "calificacion" : calificacion.value
            }
            books.append(data)
            save_books(books)
            messages.controls.append(ft.Text("libro actualizado exitosamente") )
            page.update() 
        buttons = ft.Button("Guardar", on_click =  on_save)
        messages.controls.append(
            ft.Column(
                controls = [titulo, autor, portada, comentarios, calificacion, buttons]
                       
            )
        ) 
        page.update()
    def confirm(book):
        confirmation = ft.Column(
            controls=[
                ft.Text("¿Estás seguro que quieres eliminar el libro?"),
                ft.Row(
                    controls=[
                        ft.Button("SI", on_click=lambda e, b=book: delete(b)),
                        ft.Button("NO", on_click=lambda e, b=book: show_books())
                    ]
                )
            ]
        )
        messages.controls.append(confirmation)
        page.update()
    def delete(book):
        books.remove(book)
        save_books(books)
        messages.controls.append(ft.Text("libro eliminado exitosamente"))
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
                            ft.Button("eliminar", on_click=lambda e, b=book: confirm(b)),
                            ft.Button("actualizar", on_click=lambda e, b=book: update(b))
                                ]
                            )
                        ] 
                    )  
                 ]
             )
        list.controls.append(row)
        page.update()
    add_book(books, messages, page)
    def add_message(e):
        message = text_area.value.strip()
        if message == "list":
            messages.controls.append(show_books(books, show_details))
        elif message == "add":
           messages.controls.append(add_book())
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
ft.app(main)




