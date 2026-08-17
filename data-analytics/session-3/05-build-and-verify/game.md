# Game — what do you say to the stakeholder?

**5 minutes, out loud.** Replaces the share-back slot.

Five situations. Someone has two numbers in front of them and wants to know
which is right. **What do you say?**

The wrong answer available every time is *"let me go and check"* — because you
already know. That is what the last fifty-five minutes were for.

---

### 1

> *"Fundraising says £947,000. Your new report says £930,000. Which is right?"*

**Both.** Yours excludes refunded gifts; theirs does not. About £17,000 of gifts
were given and later returned.

Then the useful sentence: *"which of those two is the number you want depends on
whether you are reporting what people gave us or what we kept."*

### 2

> *"Two dashboards, two supporter counts, 615 apart. Is one broken?"*

**Neither.** One counts people whose record is marked active; the other counts
people who actually gave in the last twelve months. Different questions, same
word.

Never say *"it's a data issue"* — it is a definition issue, and calling it data
sends someone off to fix something that is not broken.

### 3

> *"Your click-through rate is over 100%. That's obviously wrong."*

**They are right to flag it, and the number is real.** 77 rows record a click
with no open — a tracking artefact. Across the whole dataset that only lifts
click-through to about 19%, but the measure divides clicks by opens, so for one
supporter or one campaign it can exceed 100%.

Say which denominator you used and why. Do not quietly change it to make the
number look sensible.

### 4

> *"Why is my supporter count different from the number of people in the
> donations table?"*

**Because 30 donations point at supporters who do not exist**, and 22 people
appear in the file twice. A distinct count of `supporter_id` in donations and a
count of supporters are never going to match.

### 5

> *"So which number do I put in the trustee report?"*

**Not a data question, and not yours to answer alone.** Say what each number
means and what it excludes; which one gets reported is theirs to choose with the
information you just gave them.

Handing them a single number without that is how the disagreement you spent
today untangling got created in the first place.

---

## The lesson

Not one of these was answered with *"that one is wrong."* Every one was answered
by **naming what each number counts and what it leaves out.**

That is what "a number you can defend" means. Not that you can prove it is
right — that you can say exactly what it is.
