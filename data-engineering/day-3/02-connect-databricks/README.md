# 2 — Claude Code against a real workspace

**20 minutes, watch only**
*5 min the myth · 8 min live on the workspace · 7 min the boundary.*

> **Who does what:** I run it, you watch. **Nobody needs Databricks access for
> this part, or for any hands-on part today.** If you do have access and want to
> follow along, the commands are all here — but do not let a login problem cost
> you part 3.

## The myth worth killing first

> *"If we cannot reach Databricks over MCP, we cannot use Claude Code with
> Databricks."*

That is false, and believing it is expensive — it makes a tool you already have
look blocked on an IT ticket.

Claude Code's two real powers are **reading and writing files** and **running
shell commands**. Databricks sits on both:

| What you want to do | What it actually is | Needs a live connection? |
|---|---|---|
| Understand or refactor a notebook | Editing a `.py` file | **No** |
| Convert an ADF Mapping Data Flow | Editing a `.json` file | **No** |
| Author a job or a DAB bundle | Editing a `.yml` file | **No** |
| List catalogs, run a query, check a table | Calling the `databricks` CLI | Yes |
| Ask the warehouse in plain English | Genie, in the browser | Yes |

Two rows out of six. **Everything you asked for in June lives in the "no" rows**
— which is why parts 3 and 4 are hands-on for a room where half of you have no
workspace.

## What we run

**Scene.** One window on my screen: Claude Code in a terminal, in the
`data-engineering/` folder, fresh conversation. My own Databricks workspace is
already authenticated on this machine — that setup happened before today, and
the steps are below so you can repeat them.

### The setup, once per machine

```bash
databricks auth login --host https://<your-workspace>.azuredatabricks.net --profile an-workshop
```

That is an interactive browser login, fine for a person. For anything that runs
unattended — a job, a pipeline, a shared machine — you use a **service
principal** instead, and the CLI reads it from the environment:

```bash
export DATABRICKS_HOST=https://<your-workspace>.azuredatabricks.net
export DATABRICKS_CLIENT_ID=<service-principal-application-id>
export DATABRICKS_CLIENT_SECRET=<oauth-secret>
```

> **Why a service principal, not your own token.** A personal access token
> carries *your* permissions and dies when you leave. A service principal is
> scoped to exactly the catalog and warehouse you grant it, and it is auditable
> as itself. For a registry holding donor data, that difference is the whole
> conversation with your security people.

### Three things typed into Claude Code

**One — can you see it at all.**

> Using the `databricks` CLI with the `an-workshop` profile, list the catalogs I
> can see, then the schemas in the training catalog. Show me the commands you
> run.

Watch for what it does: it runs `databricks catalogs list`, reads the output,
then `databricks schemas list`. **It is using the shell, not a special
integration.** Everything you can do at that prompt, it can do.

**Two — a real question, answered in SQL.**

> Using the same profile and warehouse, how many donors are there per status in
> `training.<schema>.donor`? Run it as a SQL statement against the warehouse and
> show me both the SQL and the result.

**Three — the one that matters.**

> Now write what you just learned about this workspace into `docs/databricks.md`
> — the host, the catalog and schema, the warehouse id, the table names and
> their grain. No rows, no sample values.

That third prompt is the whole of Day 2 applied to a new surface. The next
person who opens this repo does not have to rediscover which catalog anything
is in.

## The boundary — the part to actually remember

Something changed the moment we connected, and it is easy to miss.

```
  reading a notebook file        Claude sees CODE
  reading pipeline JSON          Claude sees CODE
  running a query on the         Claude sees CODE      … and then
  warehouse                                            THE ROWS COME BACK
```

Query results land in the terminal, and the terminal is the model's context.
**A live connection is the one place in these four days where real data can
reach the model by accident.** Not through a screen-share, not through a paste —
through a helpful `select *`.

Three rules, and they are cheap:

1. **Aggregate, do not enumerate.** `count(*) group by status` is a fact.
   `select * from donor limit 100` is a hundred donors in a chat log.
2. **Grant the service principal only what the task needs.** Read on one
   schema beats read on the catalog, every time.
3. **Say it in `CLAUDE.md`.** *"Never run an unaggregated select against
   `training.*.donor`."* You wrote rules like this yesterday; this is the same
   move, on the surface where it matters most.

## The question to hold onto

**▸ Together, out loud.** Of the six rows in that first table, which two does
your team need a live connection for *this quarter* — and who owns the service
principal that makes them possible?

If the honest answer is "nobody yet", that is a useful thing to have said in
front of your team lead.

## If you have access and want to try it

Everything above, on your own workspace, in your own schema. If a login fails,
**stop and move on** — part 3 starts in a moment and it needs nothing but the
folder on your laptop.
