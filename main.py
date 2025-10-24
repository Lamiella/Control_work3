import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'Список покупок'
    page.theme_mode = ft.ThemeMode.DARK

    shop_list = ft.Column(spacing = 10)

    def create_list_row(prod_id, prod_text):
        
        prod_field = ft.TextField(value=prod_text, read_only=True, expand=True)

        def set_bought(_):
            check = checkbox.value
            if check == 1:
                main_db.bought(prod_id, bought=1)
            elif check == 0:
                main_db.bought(prod_id, bought=0)
        
        checkbox = ft.Checkbox(on_change=set_bought)

        def del_prod(_):
            main_db.delete_prod(prod_id)
            load_list()

        del_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=del_prod, icon_color=ft.Colors.RED)

        return ft.Row([checkbox, prod_field, del_button])
    
    def load_list():
        shop_list.controls.clear()
        for prod_id, prod_text in main_db.get_prod():
            shop_list.controls.append(create_list_row(prod_id=prod_id, prod_text=prod_text))
        page.update()
    
    def add_prod(_):
        if prod_input.value:
            prod = prod_input.value
            prod_id = main_db.add_prod(prod)
            shop_list.controls.append(create_list_row(prod_id=prod_id, prod_text=prod))
            prod_input.value = ''
            page.update()

    prod_input = ft.TextField(label='Введите название товара', expand=True, on_submit=add_prod)
    add_button = ft.IconButton(icon=ft.Icons.ADD, tooltip= 'Добавить товар',on_click=add_prod)
    
    page.add(ft.Row([prod_input,add_button]),shop_list)

    load_list()

if __name__  == '__main__':
    main_db.init_db()
    ft.app(target = main)