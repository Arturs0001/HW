from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import random

console = Console()

history = []

choices = ["Rock", "Paper", "Scissors"]


while True:
    menu = """
[1] Start Game
[2] Game History
[3] Exit
"""

    console.print(
        Panel(menu, title="Rock Paper Scissors", expand=False)
    )

    choice = Prompt.ask(
        "Choose option",
        choices=["1", "2", "3"]
    )

    if choice == "1":

        player = Prompt.ask(
            "Choose",
            choices=["Rock", "Paper", "Scissors"]
        )

        computer = random.choice(choices)

        if player == computer:
            result = "Draw"
            color = "yellow"

        elif (
            (player == "Rock" and computer == "Scissors") or
            (player == "Paper" and computer == "Rock") or
            (player == "Scissors" and computer == "Paper")
        ):
            result = "Win"
            color = "green"

        else:
            result = "Lose"
            color = "red"

        console.print()
        console.print(
            f"[bold {color}]You: {player}[/bold {color}]"
        )

        console.print(
            f"[bold cyan]Computer: {computer}[/bold cyan]"
        )

        console.print(
            f"[bold {color}]{result}![/bold {color}]"
        )

        history.append({
            "player": player,
            "computer": computer,
            "result": result
        })

    elif choice == "2":

        table = Table(title="Game History")

        table.add_column("Round")
        table.add_column("Player")
        table.add_column("Computer")
        table.add_column("Result")

        wins = 0
        loses = 0
        draws = 0

        for i, game in enumerate(history, start=1):

            result = game["result"]

            if result == "Win":
                colored_result = "[green]Win[/green]"
                wins += 1

            elif result == "Lose":
                colored_result = "[red]Lose[/red]"
                loses += 1

            else:
                colored_result = "[yellow]Draw[/yellow]"
                draws += 1

            table.add_row(
                str(i),
                game["player"],
                game["computer"],
                colored_result
            )

        console.print(table)

        console.print()
        console.print(f"[green]Wins:[/green] {wins}")
        console.print(f"[red]Loses:[/red] {loses}")
        console.print(f"[yellow]Draws:[/yellow] {draws}")

    elif choice == "3":
        console.print("[bold red]Goodbye![/bold red]")
        break