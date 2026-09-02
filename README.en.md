<div align="center">

[中文](./README.md) · **English**

# huan-an-comment-ops

**Understand what a comment thread is becoming before deciding whether to reply, how to act, and when to stop.**

[![Trial](https://img.shields.io/badge/STATUS-0.1.0--trial-E6603D?style=flat-square&labelColor=1E2422)](./docs/evidence-base.md)
[![Agent Skill](https://img.shields.io/badge/AGENT-SKILL.md-4164A8?style=flat-square&labelColor=1E2422)](./skills/huan-an-comment-ops/SKILL.md)
[![Python](https://img.shields.io/badge/PYTHON-3-7C9B72?style=flat-square&labelColor=1E2422)](./skills/huan-an-comment-ops/scripts)
[![License](https://img.shields.io/badge/LICENSE-CC_BY--NC_4.0_%2B_MIT-C99A2E?style=flat-square&labelColor=1E2422)](./LICENSE)

</div>

![Comments are judged first, then routed into continue, observe, or stop](./docs/images/comment-ops-hero-v2.png)

`huan-an-comment-ops` is a comment-operations Agent Skill for creators, brands, and community teams.

Its strongest feature is not prettier wording. It identifies whether a comment is a question, a lived story, a useful counterexample, or a dispute taking over the thread—then chooses the smallest sufficient action and writes a stopping condition.

In short: **it upgrades “replying to comments” into explainable public judgment.**

## At a glance

![The four-step workflow from evidence and thread judgment to action and stopping condition](./docs/images/workflow-v2.svg)

| You provide | The Skill handles |
|---|---|
| Post context, screenshots, or exports | Separates parent/child comments, observed actions, and unknowns |
| Platform, objective, and allowed actions | Prioritizes threads, selects one objective, and chooses the minimum action |
| Voice and boundaries | Drafts replies, rationale, risks, and stopping conditions |
| A batch of comments | Samples by layer, builds a queue, and extracts content leads |

A reply is only one option. The Skill may recommend `reply / like / observe / close / hide / report / escalate-human`—or tell you plainly that a thread is not worth continuing.

## Where it helps

![Three cross-platform use cases: comment surge, spreading disagreement, and a concrete reader story](./docs/images/use-cases-v2.svg)

1. **A post suddenly attracts hundreds of comments.** Triage before replying at scale. Useful on Douyin/TikTok, Xiaohongshu, WeChat Channels, Bilibili, YouTube, and similar feeds.
2. **A disagreement starts spreading.** Separate correction, counterexample, and provocation; clarify once when useful, then stop chasing the last word. Especially useful on X, Bilibili, Reddit, and open reply networks.
3. **A reader shares a concrete experience.** Acknowledge the situation, ask only one question that adds understanding, and turn recurring questions into an FAQ or content lead—with permission and context.

All comments shown in the graphic are original synthetic demonstrations. They are not copied platform comments and were not sent.

## Same comment, different order

![Reply-first versus judgment-first handling of the same comment](./docs/images/case-compare-v2.svg)

> “Easy for you to say. I changed jobs three times and still found no way forward.”

A generic reply tool may comfort, explain, or argue first. This Skill first marks the comment as `dissent + story`, chooses `clarify` as the single objective, acknowledges the boundary of the original claim, asks at most one condition that could add information, and defines when to stop.

It cannot guarantee satisfaction. It can make every public action reasoned, bounded, and stoppable.

## Thread-first without the spaghetti diagram

![Three clear lanes for valuable growth, escalating disagreement, and overriding risk](./docs/images/thread-state-v2.svg)

The full state model still includes `seed / expanding / contending / polarizing / derailing / acute-risk / exhausted`. The README reduces it to three readable lanes:

- new facts and useful experience → continue;
- repetition, camps, and last-word competition → clarify once, then close;
- privacy, threats, fraud, minors, or self/other harm → leave the growth lane and escalate.

See [`thread-state-machine.md`](./skills/huan-an-comment-ops/references/thread-state-machine.md) for the full model.

## Four modes

| Mode | Best for | Main output |
|---|---|---|
| Quick triage | One or a few comments | Action, draft, rationale, risk, stop condition |
| Operations batch | Surges, backlogs, disputes | Priority queue, thread actions, close/escalate list, content leads |
| Research evaluation | Comparing posts or accounts | Comment vectors, within-account breakout ratios, evidence gaps, experiments |
| Safety handling | Threats, privacy, fraud, self/other harm | Minimal preservation, stop-questioning rule, platform action, human escalation |

## Install: Claude Code and Codex recommended

```bash
npx -y skills add hosemo-hub/huan-an-comment-ops -g --all
```

List the discoverable Skill without installing:

```bash
npx -y skills add hosemo-hub/huan-an-comment-ops --list
```

### Claude Code

Send the repository URL to Claude Code and ask it to install the Skill, or run the command above. For manual installation, copy `skills/huan-an-comment-ops` to `~/.claude/skills/huan-an-comment-ops/`, then start a new session.

### Codex

Run the universal command in the environment used by Codex CLI or Codex desktop. The manual directory is `~/.codex/skills/huan-an-comment-ops/`. Start a new task and ask Codex to use the Skill on your comment threads.

### CodeBuddy / WorkBuddy

For CodeBuddy Code, use `~/.codebuddy/skills/huan-an-comment-ops/` globally or `.codebuddy/skills/huan-an-comment-ops/` per project, then verify with `/skills`. Versions with a visual manager can use **Settings → Skills → Import Skill**. Import the complete folder, including `SKILL.md`, references, scripts, and assets. See the [Tencent Cloud Skills documentation](https://cloud.tencent.com/document/product/1831/137020) and [international CodeBuddy Skills documentation](https://intl.cloud.tencent.com/document/product/1256/77295?lang=en).

## Use it in Doubao now

Doubao does not need to natively install the package for the workflow to be useful. Upload a comment screenshot and paste:

```text
Use the huan-an-comment-ops order: separate observations from inference, then judge the thread.
A reply is not the default action. Return priority threads, minimum action, reply draft when needed,
rationale, risk, unknowns, and stopping conditions. Do not pretend to execute platform actions.
```

If your Doubao version exposes custom agents, place the full instruction in the agent background/settings. Otherwise, keep using a normal chat. The complete Chinese setup is in [`docs/doubao-quickstart.md`](./docs/doubao-quickstart.md).

## What it deliberately does not do

- no engagement farming, reciprocal-like rings, sockpuppets, or fake consensus;
- no humiliation, provocation, deliberate errors, or last-word contests;
- no automatic reply, like, pin, hide, delete, or report;
- no conversion of DMs, health details, addresses, phone numbers, or minors’ identities into public content;
- no promise of reach, comment volume, sales, or follower growth.

## Validation status

Current version: `0.1.0-trial`.

The Skill structure, deterministic scripts, anonymized regression cases, cross-platform discovery research, remote GitHub tree, and `npx skills --list` discovery have been checked. Forward platform A/B tests, clean-environment replay across every client, and causal claims about growth have not been completed.

Use it for judgment now, but do not treat a suggested action as already executed or attribute growth to the Skill. See [`docs/evidence-base.md`](./docs/evidence-base.md) for the full evidence boundary.

## License

Skill instructions, references, assets, and evals use [CC BY-NC 4.0](./LICENSE). Personal, research, and non-commercial adaptations require attribution; commercial use requires separate permission. This is `source-available`, not OSI-approved open source.

Deterministic Python scripts under `scripts/` use the [MIT License](./skills/huan-an-comment-ops/scripts/LICENSE).

## Feedback

I built this Skill because I do not want to hand a public comment section over to one generic “smart reply.” The difficult question is not merely what sounds nice—it is what this public action will amplify.

The most useful feedback is a wrong classification, a suggestion you rejected, or a stopping condition that arrived too early or too late. Submit only public or fully anonymized cases through [GitHub Issues](https://github.com/hosemo-hub/huan-an-comment-ops/issues).

---

Initiated by **HuanAn Talks About Ways Forward**: use AI to reduce production friction while keeping judgment, tradeoffs, and responsibility human.
