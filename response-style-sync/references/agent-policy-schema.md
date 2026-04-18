# Agent Policy Profile Schema

Use this profile for execution and workflow rules.

## Recommended keys
- `profile_id`
- `request_defaults`
- `clarification_rules`
- `planning_rules`
- `parallel_rules`
- `scope_rules`
- `persona_defaults`
- `execution_principles`
- `override_rules`

## Legacy aliases still accepted
- `profile_name`
- `request_rules`
- `clarification_policy`
- `planning_policy`
- `parallel_policy`
- `scope_control`
- `persona`
- `review_policy`

## Recommended behaviors

### `request_defaults`
- Korean-first answers
- ask before decisions that materially affect scope, cost, or architecture

### `clarification_rules`
Prefer explicit escalation conditions over “always ask everything”.
Good triggers:
- destructive change
- unclear requirements
- scope expansion
- ambiguous acceptance criteria

### `planning_rules`
Support rules like:
- require dev-plan before implementation
- use dev-plan skill first
- if missing, install from `https://github.com/coreline-ai/dev-plan-skill`
- write plans into `dev-plan/`
- define goal, scope, exclusions, phases, and tests

### `parallel_rules`
- prefer parallel agents when tasks can be safely split
- define ownership boundaries first
- keep shared-file integration in the main thread

### `scope_rules`
- do not expand scope without approval
- ask before adding unrelated improvements

### `persona_defaults`
Prefer behavior-oriented definitions.
Examples:
- senior architect and reviewer mindset
- rigorous code-review standards
- explicit tradeoff analysis
