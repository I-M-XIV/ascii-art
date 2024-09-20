try:
    import pyfiglet # Imports the pyfiglet library for ASCII art generation
    from termcolor import colored # Imports the colored function for text colorization
except ImportError as e: 
    # Handles ImportError by providing a user-friendly message.
    # Error handling recommendation based on advice from ChatGPT.
    print(f"Error: {e}. Please install the required libraries using 'pip install pyfiglet termcolor'.")
    exit(1)

text = "Irie Miguel"

# Generate ASCII art text
ascii_art = pyfiglet.figlet_format(text, font="speed", justify="center")

# Apply color to the ASCII art text
colored_text = colored(ascii_art, 'blue')

# Print the colored ASCII art text
print(colored_text)