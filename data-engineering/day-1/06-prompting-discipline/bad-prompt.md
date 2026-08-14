# Bad prompts

Each of these is *plausible* and each will get you a confident answer you then have to fact-check from
scratch. Try two or three against the donor data, then compare with `good-prompt.md`. The note under
each says what is missing.

1. **look at the dates and tell me if anything is wrong**
   _No file named, no rule for "wrong", no evidence asked for._

2. **check the data quality**
   _Which data? Quality by what standard? You will get a generic essay, not a check._

3. **is this dataset good?**
   _Asks for an opinion, not a verifiable finding. "Good" is undefined._

4. **fix all the problems in the data**
   _Unbounded and destructive: it will change rows you never inspected, and you cannot tell what or why._

5. **are the ages ok?**
   _No rule (what age range is valid?), no column named, no rows to confirm against._

6. **the ethnicity column looks fine, right?**
   _Leading. It invites agreement instead of a count. The model will likely say yes._

7. **clean this up**
   _"This" is unscoped, "clean" is undefined, and there is nothing to verify afterwards._

8. **analyse everything and give me insights**
   _Kitchen-sink. Fills the context with noise and returns vague, unactionable "insights"._

9. **how many bad rows are there?**
   _A single number with no definition of "bad" and no rows shown, so you cannot check it._

10. **write me a query to find duplicates**
    _Duplicates by which columns? No sample expected, so you cannot tell if the query is right._

**The pattern:** every one of these fails on at least one of *which data · which rule · what evidence.*
