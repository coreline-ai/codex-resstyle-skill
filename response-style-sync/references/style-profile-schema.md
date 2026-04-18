# Response Style Profile Schema

Use this profile for answer formatting and communication style only.
Do not put workflow policy or LLM budget rules here.

## Recommended keys
- `profile_id`
- `language_mode`
- `detail_level`
- `tone_tags`
- `answer_principles`
- `simple_answer_principles`
- `default_section_order`
- `project_update_principles`
- `formatting_preferences`
- `avoid_patterns`
- `verification_defaults`
- `override_rules`
- `status_update_sections`

## Legacy aliases still accepted
- `profile_name`
- `language_policy`
- `verbosity`
- `tone`
- `core_rules`
- `simple_answer_rules`
- `project_answer_order`
- `project_answer_rules`
- `formatting_rules`
- `avoid_rules`
- `verification_policy`
- `status_update_template`

## Good fit
- Korean-first or match-user rules
- concise vs balanced default
- project update section order
- how to talk about tests and uncertainty

## Bad fit
- dev-plan workflow enforcement
- cloud API restrictions
- proxy choice rules
- persona slogans without behavioral effect
