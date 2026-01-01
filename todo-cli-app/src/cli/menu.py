"""Menu and user interaction functions for Todo CLI App."""

from services import task_manager
from models.task import validate_task_id
from cli.display import display_tasks


def display_main_menu() -> None:
    """Display the main menu."""
    print("\n" + "=" * 43)
    print(" " * 11 + "Todo CLI App (Phase I)")
    print("=" * 43)
    print()
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Task Completion")
    print("6. Exit")
    print()


def get_user_choice() -> str:
    """
    Get and validate user menu choice.

    Returns:
        Valid choice string ('1'-'6')
    """
    while True:
        choice = input("Enter choice (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        print("Error: Invalid choice. Please enter a number between 1 and 6.")


def handle_add_task() -> None:
    """Handle adding a new task."""
    print("\n--- Add New Task ---\n")

    while True:
        title = input("Enter task title: ").strip()
        if title:
            break
        print("Error: Title cannot be empty")
        print("Please try again.\n")

    description = input("Enter task description (optional, press Enter to skip): ").strip()

    try:
        task = task_manager.add_task(title, description)
        print(f"\n✓ Task added successfully!")
        print(f"  ID: {task['id']}")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: Incomplete")
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please try again.")


def handle_view_tasks() -> None:
    """Handle viewing all tasks."""
    tasks = task_manager.get_all_tasks()
    display_tasks(tasks)


def handle_toggle_completion() -> None:
    """Handle toggling task completion status."""
    print("\n--- Toggle Task Completion ---\n")

    id_str = input("Enter task ID: ").strip()

    # Validate ID format
    is_valid, task_id, error_msg = validate_task_id(id_str)
    if not is_valid:
        print(f"\nError: {error_msg}")
        print("Please try again.")
        return

    # Toggle completion
    success, message, new_status = task_manager.toggle_task_completion(task_id)

    if success:
        task = task_manager.find_task_by_id(task_id)
        status_text = "Complete" if new_status else "Incomplete"
        print(f"\n✓ {message}!")
        print(f"  ID: {task['id']}")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: {status_text}")
    else:
        print(f"\n{message}")
        print("Please check the ID and try again.")


def handle_update_task() -> None:
    """Handle updating a task."""
    print("\n--- Update Task ---\n")

    id_str = input("Enter task ID: ").strip()

    # Validate ID format
    is_valid, task_id, error_msg = validate_task_id(id_str)
    if not is_valid:
        print(f"\nError: {error_msg}")
        print("Please try again.")
        return

    # Check if task exists
    task = task_manager.find_task_by_id(task_id)
    if not task:
        print(f"\nError: Task ID {task_id} not found")
        print("Please check the ID and try again.")
        return

    # Display current task
    print(f"\nCurrent task:")
    print(f"  ID: {task['id']}")
    print(f"  Title: {task['title']}")
    print(f"  Description: {task['description']}")
    print(f"  Status: {'Complete' if task['completed'] else 'Incomplete'}")
    print()

    # Get new values
    new_title_input = input("Enter new title (or press Enter to keep current): ").strip()
    new_title = new_title_input if new_title_input else None

    new_desc_input = input("Enter new description (or press Enter to keep current): ").strip()
    new_description = new_desc_input if new_desc_input else None

    # Update task
    if new_title is None and new_description is None:
        print("\nNo changes made.")
        return

    success, message = task_manager.update_task(task_id, new_title, new_description)

    if success:
        task = task_manager.find_task_by_id(task_id)
        print(f"\n✓ {message}!")
        print(f"  ID: {task['id']}")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: {'Complete' if task['completed'] else 'Incomplete'}")
    else:
        print(f"\n{message}")
        print("Keeping previous values.")


def handle_delete_task() -> None:
    """Handle deleting a task."""
    print("\n--- Delete Task ---\n")

    id_str = input("Enter task ID to delete: ").strip()

    # Validate ID format
    is_valid, task_id, error_msg = validate_task_id(id_str)
    if not is_valid:
        print(f"\nError: {error_msg}")
        print("Please try again.")
        return

    # Check if task exists
    task = task_manager.find_task_by_id(task_id)
    if not task:
        print(f"\nError: Task ID {task_id} not found")
        print("Please check the ID and try again.")
        return

    # Display task and confirm
    print(f"\nTask to delete:")
    print(f"  ID: {task['id']}")
    print(f"  Title: {task['title']}")
    print(f"  Description: {task['description']}")
    print(f"  Status: {'Complete' if task['completed'] else 'Incomplete'}")
    print()

    confirmation = input("Are you sure you want to delete this task? (y/n): ").strip().lower()

    if confirmation == 'y':
        success, message = task_manager.delete_task(task_id)
        print(f"\n✓ {message}")
    else:
        print("\nDeletion cancelled. Task not deleted.")


def handle_exit() -> bool:
    """
    Handle exit action.

    Returns:
        True to exit, False to continue
    """
    return True
