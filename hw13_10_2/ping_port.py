import socket
import logging
from dotenv import load_dotenv
from environ import Env

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

env = Env()

def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout in seconds

    try:
        sock.connect((host, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

# Example usage
host = "smtp.meta.ua"

# Use env.int to ensure it's treated as an integer, with a default value of 465
port = env.int("EMAIL_PORT")

# Logging input values
logger.info(f"Checking if port {port} on {host} is open.")

if is_port_open(host, port):
    logger.info(f"Port {port} on {host} is available.")
else:
    logger.info(f"Port {port} on {host} is not available.")
