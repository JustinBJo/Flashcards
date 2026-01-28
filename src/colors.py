"""
Color utilities for terminal output using ANSI codes.
"""

class Colors:
    """ANSI color codes for terminal output."""
    
    # Basic colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Reset
    RESET = '\033[0m'
    
    @staticmethod
    def red(text):
        """Return text in red."""
        return f"{Colors.RED}{text}{Colors.RESET}"
    
    @staticmethod
    def green(text):
        """Return text in green."""
        return f"{Colors.GREEN}{text}{Colors.RESET}"
    
    @staticmethod
    def yellow(text):
        """Return text in yellow."""
        return f"{Colors.YELLOW}{text}{Colors.RESET}"
    
    @staticmethod
    def blue(text):
        """Return text in blue."""
        return f"{Colors.BLUE}{text}{Colors.RESET}"
    
    @staticmethod
    def magenta(text):
        """Return text in magenta."""
        return f"{Colors.MAGENTA}{text}{Colors.RESET}"
    
    @staticmethod
    def cyan(text):
        """Return text in cyan."""
        return f"{Colors.CYAN}{text}{Colors.RESET}"
    
    @staticmethod
    def bold(text):
        """Return text in bold."""
        return f"{Colors.BOLD}{text}{Colors.RESET}"
    
    @staticmethod
    def bold_cyan(text):
        """Return text in bold cyan."""
        return f"{Colors.BOLD}{Colors.CYAN}{text}{Colors.RESET}"
    
    @staticmethod
    def bold_green(text):
        """Return text in bold green."""
        return f"{Colors.BOLD}{Colors.GREEN}{text}{Colors.RESET}"
    
    @staticmethod
    def bold_red(text):
        """Return text in bold red."""
        return f"{Colors.BOLD}{Colors.RED}{text}{Colors.RESET}"
