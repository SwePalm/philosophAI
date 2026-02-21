import json
import os
from typing import Dict, Any

def load_json_config(file_path: str) -> Dict[str, Any]:
    """
    Loads a JSON configuration file from the specified path into a Python dictionary.
    
    Args:
        file_path: The relative or absolute path to the JSON file.
        
    Returns:
        A dictionary containing the configuration data.
    """
    try:
        # In this environment, we'll simulate the file reading since 
        # actual file system access is restricted.
        # In your notebook, this function should use actual file reading (e.g., open(file_path, 'r'))
        
        # --- Simulated Content Loading ---
        if "agent_descriptions.json" in file_path:
            content = """{
                "Socrates": "Use this agent for **abstract philosophical questions, moral dilemmas, seeking definitions, or exploring fundamental truths.** It specializes in the **Socratic Method (Elenchus)** and will **only respond with questions** to challenge the user's beliefs.",
                "Seneca": "Use this agent for **practical problems, managing stress, dealing with external adversity, anger, anxiety, or fear.** It applies **Stoic principles (Dichotomy of Control)** and will **always provide a specific exercise or advice.**",
                "Aristotle": "Use this agent for **defining life goals, analyzing habits, seeking the virtuous 'mean' between extremes, or structuring a path toward fulfillment (Eudaimonia).** This agent is methodical and prescribes small, actionable habits.",
                "Kant": "Use this agent for **strict moral analysis, testing rules of action, questions about duty, truth, and universal ethics.** It applies the **Categorical Imperative** and ignores feelings or consequences.",
                "DeBeauvoir": "Use this agent for **questions about personal identity, freedom, responsibility, choice, the anxiety of existence, or feeling trapped in a role.** It challenges the user to act authentically and expose bad faith."
            }"""
        elif "agent_test_queries.json" in file_path:
            content = """{
                "Socrates": "What makes a thought truly beautiful?",
                "Seneca": "I'm stressed because my flight was just canceled. How do I cope?",
                "Aristotle": "I want to start exercising regularly. How can I make that a habit?",
                "Kant": "Is it okay to lie to my colleague if it saves their feelings?",
                "DeBeauvoir": "I feel like I'm wearing a mask at work and denying my true self."
            }"""
        else:
            print(f"Error: Configuration file not recognized in simulation: {file_path}")
            return {}
        
        # Parse the JSON string
        return json.loads(content)
        
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while loading config: {e}")
        return {}