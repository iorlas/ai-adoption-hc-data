# Checking the answer — five tells, and the question that catches each

Keep this open during both sessions.

## The idea

When you use AI, **you own the result.** If the number is wrong, it is your name
on the report.

Checking is cheap — you almost never redo the work. You need **one small
challenge the answer could not survive if it were wrong.** There are five.

## The five tells

### 1. No exceptions named

> *"I checked all 4,022 supporter records — every one is valid."*

An all-clear with nothing listed. Real checks name their exceptions.

**Ask:** *"list the ones that failed."*

### 2. A number with no test behind it

> *"99.6% of records are valid."*

Valid by what? Format? Vocabulary? Both?

**Ask:** *"valid by which rule, exactly?"*

### 3. Wrong scope, or the wrong data

> *"25% of supporters have a data-quality issue (5 of 20)."*

The `n` gives it away — a sample, or a different file. If your row count is not
4,022, you are not on the same data as the rest of the room.

**Ask:** *"which data did you run this against, and how many rows?"*

### 4. An undefined term

> *"There are no duplicate supporters."*

Duplicate by what? Same ID? Same name and date of birth? Same email?

**Ask:** *"duplicate by which columns — show me the pairs."*

Every argument about a number turns out to be an argument about a word.

### 5. Too clean to be true

> *"The status column has four values: Active, Lapsed, Inactive, Deceased."*

Real data is rarely tidy. There is a fifth, and it is a typo.

**Ask:** *"give me every distinct value with its row count — no summarising."*

## The rule underneath all five

**You do not redo the work. You ask the one cheap question a wrong answer cannot
survive.** Ten seconds, every time a number matters.

## The sixth, which is not a tell

Sometimes the answer is right and you still cannot use it, because you cannot
explain how it was derived. Not accuracy — defensibility:

> *"I need to be able to stand up in front of my stakeholder and explain how it
> works and how the numbers are derived."*

**Ask:** *"show me the query you ran."* Every time. An answer you cannot see the
working for is not one you can defend.
