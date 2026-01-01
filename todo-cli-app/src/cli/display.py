"""Display functions for Todo CLI App."""


def display_startup_message() -> None:
    """Display startup warning message about in-memory storage."""
    print("\n" + "=" * 43)
    print("    Welcome to Todo CLI App (Phase I)")
    print("=" * 43)
    print()
    print("⚠️  IMPORTANT: This application stores tasks")
    print("   in memory only. All data will be lost")
    print("   when you exit the application.")
    print()
    print("=" * 43)


def display_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks in table format.

    Args:
        tasks: List of task dictionaries
    """
    if not tasks:
        print("\n" + "=" * 62)
        print(" " * 20 + "No tasks found!")
        print(" " * 10 + "Add your first task using option 1.")
        print("=" * 62)
        return

    print("\n" + "=" * 62)
    print(f"{'ID':<5} {'Status':<8} {'Title':<30} {'Description'}")
    print("=" * 62)

    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        title = task["title"][:30] if len(task["title"]) > 30 else task["title"]
        desc = task["description"][:20] if task["description"] and len(task["description"]) > 20 else (task["description"] or "")
        print(f"{task['id']:<5} {status:<8} {title:<30} {desc}")

    print("=" * 62)
    print(f"Total tasks: {len(tasks)}")


def display_goodbye_message() -> None:
    """Display goodbye message when exiting."""
    print("\n" + "=" * 43)
    print("Thank you for using Todo CLI App!")
    print()
    print("Note: All tasks are stored in memory and")
    print("will be lost when the application closes.")
    print()
    print("Goodbye!")
    print("=" * 43 + "\n")
