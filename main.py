from commands import *

if __name__ == "__main__":
    CommandManager.register_command("help", help_command)
    CommandManager.register_command("show", show_command)
    CommandManager.register_command("add", add_command)
    CommandManager.register_command("delete", delete_command)
    CommandManager.register_command("category", category_command)
    CommandManager.register_command("date", date_command)
    CommandManager.register_command("sort", sort_command)
    CommandManager.register_command("save", save_command)
    CommandManager.register_command("load", load_command)

    interpreter = Interpreter()
    interpreter.run()
