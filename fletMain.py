
import flet as ft
import pygame

def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)
    page.title = "Amit's Counter App"
    page.bgcolor = ft.Colors.WHITE
    pygame.mixer.init()

    easter_message = ft.Text(
        "",
        size=25,
        visible=False,
    )
    limit = True
    limitpic = True
    def check_word(e):
        nonlocal limit
        nonlocal limitpic
        typed_text = (e.control.value or "").strip().lower()

        secrets = {
            "hint": {
                "text": "Hey, the first hint is given to you by a character - from Doki Doki Literature Club! (type out just + the character's name to get the hint!) (another hint - a popular message picture is the exact word! (just + name))",
                "color": ft.Colors.RED,
            },
            "amit": {
                "text": "six seven!",
                "color": ft.Colors.GREEN,
            },
            "furina": {
                "text": "it is I, Furina de Fontaine, Fontaine's biggest star!",
                "color": ft.Colors.WHITE,
            },
            "verity": {
                "text": "Seriously?",
                "color": ft.Colors.YELLOW,
            },
            "just monika": {
                "text": "Hey! its me, Monika! heres the first hint for the code! The cod is Amit's birthday month and date in numbers! (MMDD)",
                "color": ft.Colors.PINK,
            },
            "monika": {
                            "text": "Hey! its me, Monika! sadly - i wont leave your screen. so, enjoy my company!",
                            "color": ft.Colors.GREEN,
                        },
            "birthday": {
                "text": "seriously? you dont know my birthday? Ask noga - she knows it!",
                "color": ft.Colors.RED,
            },
            "noga": {
                "text": "hey! its me, Noga! heres the second hint for the code! The second number in amits response is his birth month!",
                "color": ft.Colors.PURPLE,
            },
            "ben": {
                            "text": "hey! im, Ben Kraus!",
                            "color": ft.Colors.BLACK,
                        },

            "july": {
                "text": "hey you got my birthday month! now you just need to find out the date! ill help you find it if you type out my last name! (goodluck)",
                "color": ft.Colors.ORANGE,
            },
            "pasamanik": {
                "text": "didnt think youd manage to do that! good job! anywho, heres the final hint for the code! my birth date is the square root of 10 squared!",
                "color": ft.Colors.CYAN,
            },

            
        }
                 
        if typed_text == "amit we love your app":
            pygame.mixer.music.load("win.mp3")
            pygame.mixer.music.play(0)
            page.add(ft.Container(bgcolor=ft.Colors.GREEN, width=500, height=40, content=ft.Text("Achievement Unlocked: The End?", size=20, color=ft.Colors.WHITE)))
            limit = False
        if typed_text == "furina":
                pygame.mixer.music.load("sinner.mp3")
                pygame.mixer.music.play(0)
                page.title = "Furina's Counter App"
                page.bgcolor = ft.Colors.BLUE
        if typed_text == "noga":
                pygame.mixer.music.load("noga.mp3")
                pygame.mixer.music.play(0)
        if typed_text == "ben":
                pygame.mixer.music.load("ben.mp3")
                pygame.mixer.music.play(0)
        if typed_text == "monika":
            pygame.mixer.music.load("play.mp3")
            pygame.mixer.music.play(-1)
            if limitpic:
                limitpic = False
                img = ft.Image(
                src="monika.jpg",
                width=290,
                height=290,
                fit=ft.BoxFit.CONTAIN,
            )
                page.add(img)
                page.update()
            else:
                page.clean()
                page.bgcolor = ft.Colors.RED
                pygame.mixer.music.load("sayonara.mp3")
                pygame.mixer.music.play(-1)
                img = ft.Image(
                src="jumpscare.jpeg",
                width=1500,
                height=790,
                fit=ft.BoxFit.CONTAIN,
            )
                page.title = "Just Monika"
                page.add(img)
                page.update()
                
                
        if typed_text == "0710":
            page.clean()
            page.update()
            page.bgcolor = ft.Colors.WHITE
            page.add(ft.Text("Congratulations! You won! (pssst if you want to - restart the game and type in (amit we love your app) and the counter wont reset on you!)", size=50, color=ft.Colors.GREEN))
            img = ft.Image(
                            src="win_resized.gif",
                            width=600,
                            height=600,
                            fit=ft.BoxFit.CONTAIN,
                     )
            page.add(img)
            page.update()
            pygame.mixer.music.load("win.mp3")
            pygame.mixer.music.play(0)

        if typed_text in secrets:
            easter_message.value = secrets[typed_text]["text"]
            easter_message.color = secrets[typed_text]["color"]
            easter_message.visible = True
        else:
            easter_message.value = ""
            easter_message.visible = False

        page.update()

    user_input_field = ft.TextField(
        label="Type a secret word...",
        width=300,
        on_change=check_word,
    )

    def easter_egg(e):
        if user_input_field not in page.controls:
            page.add(user_input_field, easter_message)
        page.update()

    def increase_click(e):
        counter.data += 1
        if limit:
            if counter.data == 10:
                counter.data = 0
        else:
            if counter.data == 15:
                page.clean()
                page.update()
                page.bgcolor = ft.Colors.BLACK
                pygame.mixer.music.load("sayonara.mp3")
                pygame.mixer.music.play(-1)
                page.add(ft.Text("lol, you really thought id be so kind as to give you an infinite timer? #prank :) (let me be a dev plz)", size=50, color=ft.Colors.GREEN))
                img = ft.Image(
                src="prank.jpeg",
                width=600,
                height=600,
                fit=ft.BoxFit.CONTAIN,
         )
                page.add(img)

        counter.value = str(counter.data)
        counter.color = ft.Colors.GREEN
        page.update()

    page.add(
        ft.Row(
            controls=[
                ft.FloatingActionButton(
                    icon=ft.Icons.ADD,
                    on_click=increase_click,
                ),
                ft.FloatingActionButton(
                    icon=ft.Icons.QUESTION_MARK,
                    on_click=easter_egg,
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
        ),
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        ),
    )


ft.run(main)
