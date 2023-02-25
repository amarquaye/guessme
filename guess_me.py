from random import randint
import flet as ft

def main(page: ft.Page):
    """Main App"""

    page.title = "GUESS ME"
    page.theme_mode = "Light"
    page.scroll = "HIDDEN"
    page.padding =20

    page.fonts = {
        "DaddyTimeMono" : "fonts/DaddyTimeMono.ttf"
    }

    answer = randint(1,10)
    answer = int(answer)
    print(answer)
    

    #Functions
    def check_player1(e):
        """Function to check if player 1 got the right answer"""

        try:
            if int(player1.value) == answer:
                result.color = "green"
                result.value = "Congrats Player 1, you won te game (:"            
                page.update()
            elif int(player1.value) > answer:
                result.color = "yellow"
                result.value = "Almost there, try a smaller number!"
                page.update()
            elif int(player1.value) < answer:
                result.color = "yellow"
                result.value = "So close, but try a larger number!"
                page.update()
            elif not player1.value:
                result.color = "red"
                player1.error_text = "Please enter a valid number from 1 to 10!"
                page.update()
            else:
                result.color = "red"
                result.value = "Please enter a valid number from 1 to 10!"
                page.update()

        except ValueError:
            result.color = "red"
            result.value = "Please enter a valid number from 1 to 10"
            page.update()

        

    def check_player2(e):
        """Function to check if player 2 got the right answer"""
        if int(player2.value) == answer:
            result.value = "Congrats Player 2, you won the game (:"
            page.update()
        elif int(player2.value) > answer:
            result.color = "yellow"
            result.value = "Almost there, try a smaller number!"
            page.update()
        elif int(player2.value) < answer:
            result.color = "yellow"
            result.value = "So close, but try a larger number!"
            page.update()
        elif not player2.value:
            result.color = "red"
            player2.error_text = "Please enter a valid number from 1 to 10!"
            page.update()
        else:
            result.color = "red"
            result.value = "Please enter a valid number fro, 1 to 10!"
            page.update()

    title_text = ft.Text("Guess Me", font_family="DaddyTimeMono", size=40)
    result = ft.Text(size=18, font_family="DaddyTimeMono")
    row1 = ft.Row(alignment="center",controls=[
        title_text
    ])
    card1 = ft.Card(
        ft.Container(
        content=row1,padding=30
        
        )
    )
    

    player1  = ft.TextField(label="Player 1", hint_text="Guess a number from 1 to 10", border_radius=20)
    player2 = ft.TextField(label="Player 2", hint_text="Guess a number from 1 to 10", border_radius=20)

    but1 = ft.ElevatedButton("Guess", on_click=check_player1)
    but2 = ft.ElevatedButton("Guess", on_click=check_player2)

    row2 = ft.Row(controls=[
        player1, but1
    ])

    row3 = ft.Row(controls=[
        player2, but2
    ])

    container2 = ft.Container(
        content=row2, padding=10
    )

    container3 = ft.Container(
        content=row3, padding=10
    )

    container4 = ft.Container(
        content=result, padding = 20
    )
    page.add(card1, container2, container3, container4)


ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")