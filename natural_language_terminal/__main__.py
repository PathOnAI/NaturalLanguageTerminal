from .cli.app import app as create_app
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    
    create_app()