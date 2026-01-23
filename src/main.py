from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Welcome, Button, Label

class tuiApp(App):
   pass

class eventApp(App):
   COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]
   def on_mount(self) -> None:
         self.screen.styles.background = "darkblue"

   def on_key(self, event: events.Key) -> None:
      if event.key.isdecimal():
         self.screen.styles.background = self.COLORS[int(event.key)]

class WelcomeApp(App):
    async def on_key(self) -> None:
        await self.mount(Welcome())
        self.query_one(Button).label = "YES!"

    def on_button_pressed(self) -> None:
        self.exit()

class QuestionApp(App[str]):
    def compose(self) -> ComposeResult:
        yield Label("Do you love Textual?")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)

if __name__ == "__main__":
   app = QuestionApp()
   reply = app.run()
   print(reply)