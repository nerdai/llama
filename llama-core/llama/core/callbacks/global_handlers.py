"""Global eval handlers."""

from typing import Any

from llama.core.callbacks.base_handler import BaseCallbackHandler
from llama.core.callbacks.simple_llm_handler import SimpleLLMHandler


def set_global_handler(eval_mode: str, **eval_params: Any) -> None:
    """Set global eval handlers."""
    import llama.core

    llama.core.global_handler = create_global_handler(eval_mode, **eval_params)


def create_global_handler(eval_mode: str, **eval_params: Any) -> BaseCallbackHandler:
    """Get global eval handler."""
    if eval_mode == "simple":
        handler = SimpleLLMHandler(**eval_params)
    else:
        raise ValueError(f"Eval mode {eval_mode} not supported.")

    return handler
