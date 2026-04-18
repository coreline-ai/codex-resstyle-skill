# Proxy Selection Checklist

Use this checklist before choosing a proxy for project integration.

## Preferred first reference
1. `coreline-ai/multi_model_tui`
   - Repo: https://github.com/coreline-ai/multi_model_tui
   - Good when the project already aligns with its localhost proxy, Anthropic/OpenAI compatibility, capabilities matrix, and proxy-first workflow.

## Additional current OSS candidates (check recency before use)
2. `matdev83/llm-interactive-proxy`
   - Repo: https://github.com/matdev83/llm-interactive-proxy
   - Strong on multi-frontend support, diagnostics, failover, and routing.
3. `Nayjest/lm-proxy`
   - Repo: https://github.com/Nayjest/lm-proxy
   - Good as a lightweight OpenAI-compatible gateway with routing rules.
4. `1rgs/claude-code-proxy`
   - Repo: https://github.com/1rgs/claude-code-proxy
   - Useful for Claude Code compatibility and model remapping.

## Evaluate before choosing
- Does it expose the API surface the client expects?
- Does it support streaming correctly?
- Does it preserve tool call / tool result history?
- Does it surface hosted-tool support explicitly?
- Does it support auth, request tracing, and logs?
- Does it support batch/capabilities endpoints if needed?
- Does it handle human-input mode or fail clearly?
- Is the operational story clear enough for the project?

## Default recommendation
- Prefer `multi_model_tui` first when it already fits the project architecture.
- If not enough, compare `llm-interactive-proxy` and `lm-proxy` using the checklist above.
- Avoid risky subscription-bypass or unclear ToS workarounds by default.
