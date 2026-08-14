# 1 — Data quality: what is wrong, how much, and what would catch it

**30 minutes, hands-on · Claude Code + SQL**

## Why this one is first

It was your top ask in June, and it is also the foundation for everything else
today. In part 3 you will find two reports disagreeing about how many active
supporters there are. One of the reasons will be sitting in this exercise.

We do it **in SQL, not Python**, because SQL is what most of your people use
every day.

## The principle — the generator is cheap, the judgement is the value

Ask Claude for data-quality rules and it will happily give you thirty. Getting
thirty rules is not the skill. **Keeping the six that matter and rejecting the
rest is the skill.**

A rule that fires on healthy data is worse than no rule at all, because it
teaches everyone to ignore the alerts. Within a month nobody reads them, and the
one real failure goes past unnoticed.

So the question to ask of every candidate rule is:

> **Does violating this mean the data is actually wrong for how we use it — or
> is it just different from how I would have typed it?**

Postcodes written `m19bh` instead of `M1 9BH` are not wrong. A supporter whose
`status` says `Activ` **is** wrong, and it is quietly shrinking a number
somebody reports to a trustee board.

## The other principle — Claude reads the query, not your data

Worth saying once, here, where it comes up naturally. When Claude answers a
question about the data, it does it by **writing a SQL query and running it**.
The rows come back to your machine. This matters for the version of this you
might one day run at work: the model is reading your *schema*, not your
supporters.

That is not permission to point it at live donor data — today is synthetic and
stays synthetic. It is the reason the boundary is worth understanding precisely
rather than vaguely.

## What you leave with

A file — `docs/data-quality-rules.md` — with the rules you decided were worth
keeping, written as something you could actually run. Plus a shorter list of the
ones you rejected, and why. The rejected list is the more interesting half.

→ **`exercise.md`**
