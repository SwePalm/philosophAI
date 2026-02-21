import json
from pathlib import Path
from typing import Literal, Optional, List, Dict, Any
from google.adk.tools import FunctionTool

# Define the local path for the memory file
MEMORY_FILE = Path("data/philosophy_memory.json")

class SharedMemoryTool(FunctionTool):
    """
    A persistent memory tool that allows agents to read and write key data 
    (like goals, virtues, and long-term plans) to a local JSON file.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ensure_memory_file_exists()

    def _ensure_memory_file_exists(self):
        """Creates the memory file and its directory if they don't exist."""
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not MEMORY_FILE.exists():
            # Initialize with an empty structure
            with open(MEMORY_FILE, 'w') as f:
                json.dump({}, f)

    def _load_data(self) -> Dict[str, Any]:
        """Loads all data from the memory file."""
        try:
            with open(MEMORY_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Handle empty or corrupted file by returning an empty dict
            return {}

    def _save_data(self, data: Dict[str, Any]):
        """Saves all data back to the memory file."""
        with open(MEMORY_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def write_key_value(
        self, 
        key: Literal["current_virtue", "weekly_focus", "long_term_goal", "last_bias_review"], 
        value: str
    ) -> str:
        """
        Writes a specific piece of data (key and value) to persistent memory.
        
        Args:
            key: The category of the data being stored (must be one of the defined literals).
            value: The string value to store (e.g., 'Courage' or 'Finish the new design').
        
        Returns:
            A confirmation message that the key was written.
        """
        data = self._load_data()
        data[key] = value
        self._save_data(data)
        return f"Successfully updated persistent memory for key: {key}."

    def read_key_value(
        self, 
        key: Literal["current_virtue", "weekly_focus", "long_term_goal", "last_bias_review"]
    ) -> Optional[str]:
        """
        Reads a specific piece of data (value) from persistent memory using its key.
        
        Args:
            key: The category of the data to retrieve.
            
        Returns:
            The stored string value, or None if the key is not found.
        """
        data = self._load_data()
        return data.get(key, "The requested memory key was not found.")

    def get_all_goals(self) -> str:
        """
        Reads and summarizes all existing stored goals and focuses from memory.
        
        Returns:
            A formatted string containing all current goals for context.
        """
        data = self._load_data()
        summary = "Current Stored Memory:\n"
        for k, v in data.items():
            summary += f"- {k.replace('_', ' ').title()}: {v}\n"
        return summary