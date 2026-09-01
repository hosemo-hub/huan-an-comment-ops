<div align="center">

[中文](./README.md) · **English**

# huan-an-comment-ops

**Decide whether to respond, why, and when to stop—then draft the reply.**

[![Trial](https://img.shields.io/badge/STATUS-0.1.0--trial-e86f3c?style=flat-square&labelColor=262626)](./docs/evidence-base.md)
[![Agent Skill](https://img.shields.io/badge/AGENT-SKILL.md-2148b8?style=flat-square&labelColor=262626)](./skills/huan-an-comment-ops/SKILL.md)
[![Python](https://img.shields.io/badge/PYTHON-3-6b9f32?style=flat-square&labelColor=262626)](./skills/huan-an-comment-ops/scripts)
[![License](https://img.shields.io/badge/LICENSE-CC_BY--NC_4.0_%2B_MIT-f29a2e?style=flat-square&labelColor=262626)](./LICENSE)

</div>

![Comment threads branching into paths to continue, observe, or stop](./docs/images/comment-ops-hero-v1.png)

`huan-an-comment-ops` is an Agent Skill for cross-platform comment operations and community risk control. It treats a comment section as a public community and a research surface—not as a factory for polished replies.

It separates evidence, classifies thread state, chooses the minimum sufficient action, and makes stopping conditions explicit. By default it analyzes and drafts only. It does not post, like, hide, or report automatically, and it makes no promise of follower, recommendation, or comment growth.

## At a glance

| Common approach | huan-an-comment-ops |
|---|---|
| Generate a reply for every comment | First decide whether the comment and thread should continue |
| Read every comment in isolation | Preserve parent-child context and classify thread state |
| Treat more comments as success | Separate knowledge, relationship, noise, and harm |
| Return one suggested sentence | Return an action, rationale, risk, evidence state, and stop condition |
| Use provocation or engagement trading | Reject manipulation, impersonation, baiting, and automatic writes |

![Workflow from evidence state to stopping condition](./docs/images/workflow.svg)

## A hypothetical case

> Post: Start a career transition with a small public project.<br>
> Comment: Easy for you to say. I changed jobs three times and still found no way forward.

A generic reply tool may reassure, persuade, or immediately ask for more painful detail. This Skill first treats the comment as a relevant counterexample:

| Field | Candidate judgment |
|---|---|
| Evidence state | `observed` when visible in a screenshot or public page |
| Contribution type | `dissent` + `story` |
| Thread state | `seed` |
| Primary objective | `clarify` |
| Minimum action | Acknowledge the boundary; ask only if the answer adds a useful condition |
| Stop condition | The person declines, or the next turn only repeats positions |

A candidate reply might be:

> That counterexample matters. My post is about reducing the cost of one attempt, not claiming that a small project guarantees a transition. If you want to name just one factor, what most shaped those three changes? No need to share more than you want.

This is neither the only valid answer nor a message that was actually sent. It demonstrates the order of judgment: recognize the counterexample, clarify the boundary, and only then decide whether a question is warranted.

![Difference between generic reply generation and thread-first judgment](./docs/images/case-compare.svg)

## What it does

| Mode | Use it for | Main output |
|---|---|---|
| Quick triage | One or a few comments | Suggested action, draft, rationale, risk, evidence state, stop condition |
| Operations batch | High-volume comment sections or disputes | Stratified sample, priority queue, thread actions, no-reply/moderation/escalation list, content leads |
| Research evaluation | Comparing posts or accounts | Comment vectors, within-account breakout statistics, evidence gaps, experiment design |
| Safety handling | Threats, privacy, minors, self-harm, scams, and similar risks | Minimal evidence retention, no probing, moderation guidance, human escalation |

## Core decision system

### 1. Evidence separation

- `observed`: visible in a screenshot, export, or public page;
- `reported`: stated by the creator but not independently checked;
- `inferred`: concluded from context;
- `unknown`: not supported by available evidence.

A proposed reply is not an actual reply. A simulated action is not a platform action. More comments do not prove that an author reply caused growth.

### 2. Thread-first triage

Comments are labeled as `story / question / correction / insight / affiliation / play / dissent / provocation / spam / harm`. Threads move through `seed / expanding / contending / polarizing / derailing / acute-risk / exhausted`.

![Thread states can jump; acute risk overrides growth](./docs/images/thread-state.svg)

### 3. One primary objective

Each pass chooses one objective: `care / knowledge / clarify / community / research / conversion / stop`. “Get more comments” cannot be the sole objective.

### 4. Minimum sufficient action

Available actions include `reply / like / pin / observe / close / hide / remove-if-supported / report / escalate-human`. Replying is not the default.

### 5. Explicit stopping conditions

Stop when two turns add no new information, the thread becomes a fight for the last word, abuse or private information appears, the topic derails, the creator has already clarified enough, or operating cost exceeds the thread’s value to observers.

## Install

```bash
npx -y skills add hosemo-hub/huan-an-comment-ops -g --all
```

Inspect without installing:

```bash
npx -y skills add hosemo-hub/huan-an-comment-ops --list
```

Python 3 is required for the two deterministic analysis scripts. A simple single-comment triage may not need them.

### WorkBuddy

This repository does not claim that `npx --all` natively targets every WorkBuddy version. The safer manual path is to copy the complete `skills/huan-an-comment-ops` folder to:

- Windows: `%USERPROFILE%\.workbuddy\skills\huan-an-comment-ops\`
- macOS / Linux: `~/.workbuddy/skills/huan-an-comment-ops/`

Start a new session and verify that the client can load `SKILL.md`.

## Try it

```text
Use huan-an-comment-ops to triage these comments.
Separate original comments, actions the author actually took,
and drafts that have not been posted.
Then return the minimum action, a reply draft, and a stop condition per thread.
Do not publish anything.
```

Whenever possible, include the platform, post summary, parent-child relationships, observation time, actions already taken, allowed actions, and preferred tone. Missing context remains `unknown`; it is not invented.

## Structured input

For batches, start with [`comment-batch.example.json`](./skills/huan-an-comment-ops/assets/comment-batch.example.json):

```json
{
  "platform": "example-platform",
  "content_goal": "collect useful counterexamples",
  "observed_at": "2026-08-30T12:00:00+08:00",
  "allowed_actions": ["reply", "like", "observe", "escalate-human"],
  "comments": []
}
```

Raw fields are never silently rewritten. A sample is never presented as a full-population ratio when the complete thread set is unavailable.

## Platform boundaries

The core reasoning may transfer; platform features, community norms, and recommendation effects do not automatically transfer.

| Platform | Current focus | Evidence boundary |
|---|---|---|
| WeChat Official Accounts | Curated message walls, precise acknowledgment, trauma boundaries | Project-derived history; not a public cross-platform population |
| Xiaohongshu | Experience exchange vs. engagement-trading noise | Discovery samples; no production A/B |
| Bilibili | Top-level replies, nested threads, memes, knowledge co-creation, minor safety | Discovery samples; publication-time followers often unknown |
| YouTube | Sampling high-volume threads and using governance tools | Public samples and official moderation documentation |
| X | Fast diffusion, weak audience boundaries, one complete clarification first | Core rules applicable; outcomes unvalidated |
| Reddit | Community and moderator rules before author tactics | Discovery samples; subreddit rules remain authoritative |
| Douyin / TikTok / WeChat Channels | Transfer pending validation | No qualifying auditable corpus yet |

## Validation status

Current version: `0.1.0-trial`.

Completed:

- Skill structure and entry checks;
- deterministic examples and syntax checks for two Python scripts;
- anonymized regression cases;
- maximum-variation cross-platform discovery research and behavior smoke tests;
- remote-tree and `npx skills --list` discoverability checks.

Not completed:

- prospective production A/B tests;
- causal evidence that author replies increase recommendations, followers, or comments;
- qualifying corpora for Douyin, TikTok, or WeChat Channels;
- clean-environment installation replay across all clients and WorkBuddy versions.

See [`docs/evidence-base.md`](./docs/evidence-base.md) for the evidence boundary.

## Not this

- not engagement farming, reciprocal likes, sockpuppeting, or fake consensus;
- not humiliation, baiting, deliberate errors, or last-word contests for reach;
- not automatic reply, like, pin, hide, delete, or report actions;
- not a pipeline that turns DMs, medical records, addresses, phone numbers, or minors’ information into content;
- not a legal conclusion that similarity equals plagiarism or infringement;
- not a promise of recommendation, comment, revenue, or follower growth.

## Repository layout

```text
huan-an-comment-ops/
├── docs/
│   ├── evidence-base.md
│   └── images/
├── skills/huan-an-comment-ops/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── assets/comment-batch.example.json
│   ├── evals/evals.json
│   ├── references/
│   └── scripts/
├── README.md
├── README.en.md
└── LICENSE
```

## License

Skill instructions, references, assets, and evals are licensed under [CC BY-NC 4.0](./LICENSE). Non-commercial use, research, and adaptation require attribution; commercial use requires separate permission. This is source-available with a non-commercial restriction, not OSI open-source software.

Deterministic Python scripts under `scripts/` are separately licensed under the [MIT License](./skills/huan-an-comment-ops/scripts/LICENSE).

## Feedback

The most useful feedback is not “works great.” Tell us where the Skill made the wrong judgment, why you rejected its proposed action, or which stop condition arrived too early or too late.

Only submit public or properly anonymized comments. Do not upload private messages, personal contact details, medical records, minors’ identities, or other sensitive material.

---

Initiated by HuanAn: use AI to reduce sorting and production friction while keeping judgment, trade-offs, and responsibility human.
