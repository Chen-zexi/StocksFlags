from .env import (
    # Reasoning LLM
    REASONING_MODEL,
    REASONING_MODEL_PROVIDER,
    # Basic LLM
    BASIC_MODEL,
    BASIC_MODEL_PROVIDER,
    # Vision-language LLM
)

# Team configuration
TEAM_MEMBERS = ["researcher", "coder", "reporter"]

__all__ = [
    # Reasoning LLM
    "REASONING_MODEL",
    "REASONING_MODEL_PROVIDER",
    # Basic LLM
    "BASIC_MODEL",
    "BASIC_MODEL_PROVIDER",
    # Other configurations
    "TEAM_MEMBERS",
    "TAVILY_MAX_RESULTS",
]
