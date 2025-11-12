import flet as ft 
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'my first app'
    greeting_text = ft.Text(value='Hello world')
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []
    history_text = ft.Text('History of greetings:')
        
    favorit_list = []
    favorit_text = ft.Text('favorit list:')


    def on_button_click(_):
        name = name_input.value.strip()
        # print(name)

        if name:
            greeting_text.color = None
            greeting_text.value = f'Hello {name}'
            name_input.value = None

            # greeting_history.append(timestamp + " " + name)
            timestamp = datetime.now().strftime("%D:%M:%Y  %H:%M:%S")

            greeting_history.append(f"{timestamp} {name}")
            history_text.value = 'History of greetings: \n' + '\n'.join(greeting_history)
        
        
            

        else:
            greeting_text.value = "You didn't enter the name!!!"
            greeting_text.color = ft.Colors.RED


        page.update()

    def clear_last_history(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'History of greetings: \n' + '\n'.join(greeting_history)
        else:
            history_text.value = "The list is empty, nothing to pop."
        page.update()


    clear_last_button = ft.ElevatedButton(text='Clear Last', icon=ft.Icons.REMOVE, on_click=clear_last_history)
    page.add(clear_last_button)


    def add_favorites(_):
            favorit_list.append(f'favorit list: {greeting_history[-1]}')
            favorit_text.value = 'favorit list:' + ' '.join(favorit_list)
            page.update()

    add_favorites_button = ft.ElevatedButton(text='Add to favorites', icon=ft.Icons.FAVORITE_SHARP, on_click=add_favorites, icon_color=ft.Colors.RED_900)


    name_input = ft.TextField(label='Enter the name', on_submit=on_button_click)
    input_button_text = ft.TextButton(text='send', icon=ft.Icons.SEND_ROUNDED, on_click=on_button_click)

    def theme_mode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    theme_mode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_mode)


    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'History of greetings:'
        page.update()


    clear_button = ft.ElevatedButton(text='Clear', icon=ft.Icons.DELETE, on_click=clear_history)

    page.update()


    page.add(greeting_text, name_input, input_button_text,theme_mode_button, clear_button, history_text,add_favorites_button, favorit_text)

ft.app(target=main_page)
