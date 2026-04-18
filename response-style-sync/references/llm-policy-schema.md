# LLM Policy Profile Schema

Use this profile for model-cost, backend, proxy, and research policy.

## Recommended keys
- `profile_id`
- `cloud_api_rules`
- `proxy_rules`
- `preferred_proxies`
- `proxy_selection_checks`
- `research_rules`
- `compliance_rules`
- `override_rules`

## Legacy aliases still accepted
- `profile_name`
- `cloud_api_policy`
- `proxy_policy`
- `preferred_proxy_repos`
- `proxy_selection_criteria`
- `research_policy`
- `compliance_policy`

## Recommended behaviors

### `cloud_api_rules`
- default deny or avoid
- allow only when unavoidable
- require explicit reason logging or user approval for paid usage

### `proxy_rules`
- prefer proxy-first implementation planning
- prefer local or OAuth-backed flows before direct paid API usage
- prefer project-specific proxy references when available

### `preferred_proxies`
Record stable references the agent should evaluate first.
Include repo URL and intended use if needed.

### `proxy_selection_checks`
Good criteria:
- Anthropic/OpenAI/Responses compatibility
- streaming behavior
- tool_call / tool_result history
- hosted tools support
- auth / logging / request tracing
- batch / capabilities
- human input behavior
- maintenance and operational clarity

### `research_rules`
- when a new proxy is needed, search current OSS first
- prefer primary sources such as official GitHub repos
- record why a proxy was selected

### `compliance_rules`
Recommend avoiding subscription-bypass or ToS-risky harnesses by default.
