# Section 2 — LLM essentials for engineers (1:00, ~20 min)

This section is mostly discussion, not typing. You did the prereq courses, so this is a **recast in
DE terms**, not a re-teach. Three ideas, one habit.

## 1. The context window is a fixed box

Everything the model can "see" at once — your files, your prompt, its own previous replies — shares
**one fixed-size box** measured in tokens. When the box is full, something has to give.

```
   ┌──────────────  context window (fixed size)  ──────────────┐
   │  system + CLAUDE.md │ your files │ conversation │ headroom │
   └───────────────────────────────────────────────────────────┘
                                          the model only reasons
                                          over what is IN the box
```

## 2. The model is stateless

Each turn, the model **re-reads the whole box from scratch**. It has no memory between turns beyond
what is in the window. "It forgot" really means "that fell out of the box, or was never in it."

```
   turn 1 ─▶ [reads box] ─▶ reply        (nothing is remembered...)
   turn 2 ─▶ [reads box again] ─▶ reply  (...it re-reads every time)
```

## 3. Context management is the whole skill

Since the box is fixed and the model is stateless, **your job is to curate what goes in the box**:
the right files, a `CLAUDE.md` that carries the standing facts, a scoped question. Good DE work with
AI is mostly good context management.

## Try it (2 min)

Paste a large file (or ask Claude to read several) and watch how quickly the useful signal gets
crowded by bulk. Then do the opposite: point it at *just* the one file and column that matter. Feel
the difference in answer quality. That contrast **is** the skill.

> Carry this into every later section: when an answer is bad, first ask *"what was in the box?"*
