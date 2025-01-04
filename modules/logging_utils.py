import sys
import os
from datetime import datetime


class Tee:
    """Redirect output to both console and optionally a log file."""
    def __init__(self, log_file=None):
        self.log_file = open(log_file, "w") if log_file else None
        self.console = sys.stdout

    def write(self, message):
        self.console.write(message)
        self.console.flush()  # Ensure immediate console output
        if self.log_file:
            self.log_file.write(message)
            self.log_file.flush()  # Ensure immediate log file writing

    def flush(self):
        self.console.flush()
        if self.log_file:
            self.log_file.flush()

    def close(self):
        if self.log_file:
            self.log_file.close()


def setup_logging(destination_directory=None, log_to_file=False):
    """Set up logging, redirecting output to console and optionally a log file."""
    if log_to_file and destination_directory:
        log_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file_path = os.path.join(destination_directory, f"log_{log_timestamp}.txt")

        # Ensure the destination directory exists
        os.makedirs(destination_directory, exist_ok=True)

        # Create Tee object and redirect sys.stdout and sys.stderr
        tee = Tee(log_file=log_file_path)
        sys.stdout = tee
        sys.stderr = tee
        return tee
    else:
        # Console-only logging
        return Tee()
