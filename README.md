# qTodo

A simple, fast, and intuitive Command-Line Interface (CLI) task manager built in Python.

## Installation

You can install `qtodo` globally directly from PyPI using pip:

```bash
pip install qtodo
```

## Quick Start

`qtodo` is built around the concept of "Lists" (like "Inbox", "Project", "Groceries"). By default, you'll be placed in the `Inbox` list.

```bash
# Add a task to your default list
qtodo add "Buy milk"

# Add a task to a specific list (it creates the list automatically if it doesn't exist!)
qtodo add "Fix login bug" @Work

# See your tasks
qtodo ls

# Mark a task as done (using its ID from the ls command)
qtodo done 1
```

## Commands Reference

### Managing Tasks

- `qtodo add "TASK" [@LIST_NAME]`: Add a new task. Optionally append `@listname` to add it directly to a specific list.
  - `--priority (-p)`: Priority of the task (1-3, default is 2)
  - `--duration`: Expected duration in minutes (default is 60)
  - `--due`: Due date (e.g., 'today', 'tomorrow', '2023-12-31')
- `qtodo ls [@LIST_NAME]`: List tasks. By default, it shows tasks from your currently active list.
  - `--due`: Filter by a specific due date.
  - `--all`: Show all tasks, including completed ones from the past.
- `qtodo done <ID>`: Toggle a task's completion status.
- `qtodo rm <ID>`: Delete a task permanently.

### Managing Lists

- `qtodo switch <LIST_NAME>`: Change your default list context. All subsequent `add` and `ls` commands will automatically target this list without needing to type `@listname`.
- `qtodo lists`: View all your existing lists.
- `qtodo newlist <NAME>`: Create a new list explicitly (optionally provide a `--desc`).
- `qtodo editlist <OLD_NAME> <NEW_NAME>`: Rename a list or update its description.
- `qtodo rmlist <NAME>`: Permanently delete an entire list and all of the tasks inside it.

## Example Workflow

Let's say you're starting a new coding project:

1. Create a dedicated list and switch your context to it so you don't have to keep typing its name:
   ```bash
   qtodo newlist Code --desc "My new app"
   qtodo switch Code
   ```
2. Add some tasks:
   ```bash
   qtodo add "Setup database" -p 1
   qtodo add "Write API endpoints" --due tomorrow
   qtodo add "Design frontend"
   ```
3. Check your list:
   ```bash
   qtodo ls
   ```
4. Check off the database task (assuming its ID is 1):
   ```bash
   qtodo done 1
   ```

## Connect

- **GitHub:** [dhanushd-27/qTodo](https://github.com/dhanushd-27/qTodo)
- **Portfolio:** [dhanush.tech](https://dhanush.tech/)
- **LinkedIn:** [dhanush27](https://www.linkedin.com/in/dhanush27/)
- **X (Twitter):** [@orcatwt](https://x.com/orcatwt)
