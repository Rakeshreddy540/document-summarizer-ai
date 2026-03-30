def format_output(data):
    """
    Formats the output data into a readable string.
    """
    return str(data)


def handle_file(file_path, mode='r'):
    """
    Handles file opening and closing.
    """
    try:
        with open(file_path, mode) as file:
            return file.read() if mode == 'r' else file
    except IOError as e:
        return f'Error opening file: {e}'


def log_error(error_message, log_file='error.log'):
    """
    Logs error messages to a specified log file.
    """
    with open(log_file, 'a') as log:
        log.write(f'{error_message}\n')
