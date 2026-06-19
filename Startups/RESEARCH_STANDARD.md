# Startup Research Standard

This directory contains twice-daily startup research reports. Create one
directory per date so the morning and evening Markdown reports stay together:

```text
Startups/YYYY-MM-DD/
├── YYYY-MM-DD-morning.md
└── YYYY-MM-DD-evening.md
```

Reports are Markdown only. Do not generate, modify, stage, or commit HTML.

## Selection rules

- Discover candidates only through Y Combinator, a16z, Sequoia Capital,
  Founders Fund, and General Catalyst. Analyze their newest batches, portfolio
  additions, launch announcements, and investments.
- Company websites, technical sources, founder profiles, government records,
  and credible reporting may be used to verify and analyze a candidate after
  discovery.
- Every selected startup must have a verified founding, public launch, or first
  accelerator/VC batch date on or after January 1, 2026. Exclude unverifiable
  dates and every company founded before 2026.
- Prioritize companies announced in the last 60 days. Widen only to earlier
  2026 companies when necessary.
- Include only pre-seed, seed, and Series A companies. Exclude Series B and
  later companies. A recent later-stage round does not make an older company
  eligible.
- Prefer companies with enough primary evidence to analyze.
- Do not repeat or publish update entries for a startup already covered.
- If the five discovery sources do not provide 10 eligible companies, state
  the shortfall rather than weakening the date, stage, or evidence gates.
- The majority of every report should be technology startups. Prefer companies
  where software, AI/ML, infrastructure, robotics, hardware, biotech platforms,
  developer tools, cybersecurity, data systems, or another substantive
  technical capability is central to the product rather than incidental.
- Maintain variety across technical domains, business models, geographies, and
  stages. Include non-technical businesses only when their problem, model, or
  execution is exceptionally instructive.
- Separate verified facts from analyst inference. Never invent financial,
  customer, founder, traction, or funding details.

## Required analysis for every startup

1. **Money:** funding amount, stage, investors, and verified user, customer, or
   revenue evidence when available. Do not add unsupported valuation or market
   claims.
2. **Technology:** this is the largest section. Explain the product workflow
   and technical system as deeply as public evidence
   permits: architecture, models or algorithms, data inputs and feedback loops,
   infrastructure, integrations, hardware or scientific components, deployment
   model, performance constraints, security, reliability, scalability, and
   unit-cost drivers. Distinguish disclosed architecture from analyst
   reconstruction. Identify what is genuinely difficult to build, what could
   be assembled from commodity components, and what technical claims require
   validation. When implementation details are unavailable, state that plainly
   and infer cautiously from product behavior, hiring, patents, papers,
   repositories, technical posts, demos, and founder backgrounds.
3. **Founders:** relevant prior work, founder-market fit, unusual insight,
   technical or distribution
   advantages, gaps, and whether the team is unusually suited to win.
4. **Verdict:** provide a short conclusion, numeric rating, and confidence
   level. Include competition, risks, market context, and unanswered questions
   only when they directly affect money, technology, founders, or the rating.
5. **Sources:** link primary sources first, then credible secondary reporting.
    Include publication dates and access date.

## Report-level requirements

- Begin with a short screening note: approximate candidates checked across the
  five discovery sources, newest batches or announcements reviewed, and
  confirmation that every selection passed the 2026 and stage gates.
- Include a compact ranked summary table.
- Write with high information density. Be concise, but never simplistic:
  remove repetition, throat-clearing, vague adjectives, and generic startup
  commentary while retaining evidence, mechanisms, causal reasoning,
  technical detail, uncertainty, and counterarguments.
- Target 3,500–5,500 words and do not exceed 6,000 words.
- Before researching, read at least the three most recent reports when
  available, including the current day's morning report before the evening run.
- Every material current fact must have a nearby citation or appear in the
  startup's source list.
