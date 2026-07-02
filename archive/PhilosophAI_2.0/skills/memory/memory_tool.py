import os
from pathlib import Path
from typing import Optional, List
from google.adk.tools import FunctionTool

MEMORY_FILE = Path("data/memory.md")

class MarkdownMemoryTool(FunctionTool):
    """
    A persistent memory tool that manages a Markdown-based journal (`memory.md`).
    Allows reading recent context and appending new session summaries.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._ensure_memory_file_exists()

    def _ensure_memory_file_exists(self):
        """Creates the memory file with a header if it doesn't exist."""
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not MEMORY_FILE.exists():
            with open(MEMORY_FILE, 'w') as f:
                f.write("# User Journal & Context\n\n## User Profile\n- Name: User\n- Values: [To be discovered]\n\n## Journal Entries\n")

    def read_recent_entries(self, n_entries: int = 5) -> str:
        """
        Reads the last N entries (sections starting with '## ') from the journal.
        
        Args:
            n_entries: Number of recent entries to retrieve. Default is 5.
            
        Returns:
            A string containing the recent journal history.
        """
        if not MEMORY_FILE.exists():
            return "No memory file found."
            
        try:
            with open(MEMORY_FILE, 'r') as f:
                content = f.read()
                
            # Split by level 2 headers (## ) to separate entries
            # We filter out empty strings resulting from the split
            sections = [s for s in content.split("\n## ") if s.strip()]
            
            # The first section is usually the Profile, we might want to always include it
            # But specifically for "recent entries", we take from the end.
            
            # If we have less than N, return everything.
            if len(sections) <= n_entries:
                return content
            
            # Reconstruct the markdown for the last N sessions
            # We assume the profile is at the top, let's include it + last N
            header = sections[0] # Profile
            recent = sections[-n_entries:]
            
            result = f"## {header}\n\n...[Older entries omitted]...\n\n"
            for s in recent:
                result += f"## {s}"
                
            return result
            
        except Exception as e:
            return f"Error reading memory: {e}"

    def append_journal_entry(self, date: str, summary: str, tags: str) -> str:
        """
        Appends a new entry to the journal.
        
        Args:
            date: The date of the session (YYYY-MM-DD).
            summary: A concise philosophical summary of the session.
            tags: Comma-separated tags (e.g., "Stoicism, Anxiety, Daily").
            
        Returns:
            Success message.
        """
        entry = f"\n\n## {date} | Tags: {tags}\n{summary}\n"
        
        try:
            with open(MEMORY_FILE, 'a') as f:
                f.write(entry)
            return "Successfully appended new journal entry."
        except Exception as e:
            return f"Error writing to memory: {e}"

    def update_profile(self, key_insight: str) -> str:
        """
        Updates the User Profile section (simplistic implementation: appends to profile).
        Ideally, this would be smarter about rewriting the Profile section.
        """
        # For V1, we simply append a note to the profile area if we could parse it,
        # but since we are just appending to the file, let's just create a special entry type.
        # OR: We can just let the agent append a "Profile Update" entry.
        
        return self.append_journal_entry("PROFILE UPDATE", key_insight, "Profile")
