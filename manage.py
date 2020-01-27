from flask import send_from_directory
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from pa_messenger.bootstrap import get_app
from pa_messenger.database import get_db

app = get_app()
db = get_db()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
