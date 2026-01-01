"""Main entry point for Todo CLI App (Phase I)."""

import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from cli.display import display_startup_message, display_goodbye_message
from cli.menu import (
    display_main_menu,
    get_user_choice,
    handle_add_task,
    handle_view_tasks,
    handle_toggle_completion,
    handle_update_task,
    handle_delete_task,
    handle_exit
)


def main() -> None:
    """Main application loop."""
    # Display startup message
    display_startup_message()

    # Main menu loop
    try:
        while True:
            display_main_menu()
            choice = get_user_choice()

            if choice == '1':
                handle_add_task()
            elif choice == '2':
                handle_view_tasks()
            elif choice == '3':
                handle_update_task()
            elif choice == '4':
                handle_delete_task()
            elif choice == '5':
                handle_toggle_completion()
            elif choice == '6':
                if handle_exit():
                    break

        # Display goodbye message
        display_goodbye_message()

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n")
        display_goodbye_message()


if __name__ == "__main__":
    main()
