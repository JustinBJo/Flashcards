"""
Wordlist Manager Module
Handles loading and managing word lists from JSON files.
"""
import json
import os
from pathlib import Path
from typing import Dict, List, Optional


class WordlistManager:
    """Manages word lists for the flashcard application."""
    
    def __init__(self, wordlists_dir: str = "wordlists"):
        """
        Initialize the WordlistManager.
        
        Args:
            wordlists_dir: Directory containing JSON wordlist files
        """
        self.wordlists_dir = Path(wordlists_dir)
        self._ensure_wordlists_directory()
    
    def _ensure_wordlists_directory(self):
        """Create wordlists directory if it doesn't exist."""
        if not self.wordlists_dir.exists():
            self.wordlists_dir.mkdir(parents=True, exist_ok=True)
    
    def get_available_wordlists(self) -> List[str]:
        """
        Get list of available wordlist names.
        
        Returns:
            List of wordlist names (without .json extension)
        """
        if not self.wordlists_dir.exists():
            return []
        
        wordlists = []
        for file in self.wordlists_dir.glob("*.json"):
            wordlists.append(file.stem)
        
        return sorted(wordlists)
    
    def load_wordlist(self, name: str) -> Optional[Dict[str, List[Dict[str, str]]]]:
        """
        Load a wordlist from JSON file.
        
        Args:
            name: Name of the wordlist (without .json extension)
            
        Returns:
            Dictionary with wordlist data or None if error
        """
        file_path = self.wordlists_dir / f"{name}.json"
        
        if not file_path.exists():
            print(f"Error: Wordlist '{name}' not found.")
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validate that data is a dictionary
            if not isinstance(data, dict):
                print(f"Error: Invalid format in '{name}.json'. Expected key-value pairs.")
                return None
            
            # Convert to internal format
            pairs = [{"word": word, "meaning": meaning} 
                    for word, meaning in data.items()]
            
            if not pairs:
                print(f"Error: Wordlist '{name}' is empty.")
                return None
            
            return {
                "name": name,
                "pairs": pairs
            }
            
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{name}.json'.")
            return None
        except Exception as e:
            print(f"Error loading wordlist '{name}': {str(e)}")
            return None
    
    def get_wordlist_size(self, wordlist: Dict) -> int:
        """
        Get the number of word pairs in a wordlist.
        
        Args:
            wordlist: Wordlist dictionary
            
        Returns:
            Number of word pairs
        """
        return len(wordlist.get("pairs", []))
