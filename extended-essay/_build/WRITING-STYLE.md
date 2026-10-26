# Plain-writing pass: brief for every editor

You are editing the student-facing text of "Extended Essay Central", a website that walks IB Diploma students at the American School of Dhahran (ASD, Saudi Arabia) through their Extended Essay (EE). The site owner is Michael Smith, the EE coordinator. Students read it on laptops.

## The reader
A 16-year-old in their first year of the IB Diploma. Many speak English as an additional language. They are bright but busy, and they have never written a 4,000-word research essay. When in doubt, speak plainly.

## What to change: only the human-readable text
Rewrite sentences so a 16-year-old understands them on first read and knows what to do. Do not touch anything else.

DO NOT change:
- code, HTML tags/attributes, CSS, JS logic, Python logic, JSON keys, ids, class names, URLs, file paths;
- numbers, dates, marks, page references "(guide p. 57)", "pages 43–47", sample names, subject names;
- facts or rules. Do not add advice or claims that are not already there; do not remove a rule or a requirement;
- text inside quotation marks that quotes the IB guide or an examiner (keep verbatim, even if it contains a dash);
- example research questions copied from the IB guide or from sample essays (keep verbatim);
- the meaning of thinking-tool prompts (you may simplify their wording; keep the same number of prompts, same ids, same options count);
- headings structure (you may reword a heading; don't add or remove sections).

## How to write
1. Short, common words. "use" not "utilise", "show" not "demonstrate", "help" not "facilitate", "about" not "regarding". Explain an IB term the first time a page uses it, in a few words, if the page does not already (e.g. "your RRS (researcher's reflection space: your own EE notebook)"). Keep the IB terms students must learn: research question, primary source, secondary source, criterion, RPF, reflection session, viva voce, supervisor.
2. Mostly short sentences (aim for 10–20 words). One idea per sentence. Break long sentences with several clauses.
3. Talk to the student as "you". Use contractions naturally: you'll, don't, it's, you're, can't, won't.
4. NO EM DASHES (—) anywhere in text you write. Replace with a comma, colon, full stop, or parentheses. (Ranges like 43–47 use an en dash: keep those.) Michael never uses em dashes.
5. Avoid these words: delve, underscore, tapestry, testament, pivotal, crucial, robust, showcase, foster, landscape (figurative), vibrant, intricate, meticulous, garner, boasts, enhance, leverage, holistic (except when naming the IB's "holistic" grade descriptors), multifaceted, nuanced, realm, embark, seamless, profound, genuinely, truly, essentially, "align with", "valuable insights", "deep dive", "key" used as filler.
6. No "not X, but Y" / "it's not X, it's Y" sentences. Say what is true directly.
7. No padding to three items. If two things are true, list two.
8. Cut sentence tails like ", ensuring that…", ", highlighting…", ", which helps you…" when the sentence is complete without them.
9. Use "is" and "has", not "serves as", "functions as", "represents".
10. Name the thing. Don't use "this", "that", "it", "these" when the reader could be unsure what is meant: write "your research question", "the guide", "your supervisor". Michael is strict about this.
11. Bold: keep only where it helps a student scan (a key term or the lead-in word of a bullet). Never more than one bold phrase per sentence.
12. Keep British/Commonwealth spelling as the site already uses (organise, analyse, colour, recognise).
13. Shorter is better. If a sentence doesn't help a student understand or act, cut it. But keep every rule, requirement, deadline-type instruction and example.
14. Instructions should sound like a good teacher talking: warm, direct, no hype, no exclamation marks except where one is already doing real work.

## Check before you finish
- Search your edited files for "—": zero, except inside quotations/RQs copied from the IB or samples.
- Search for the banned words above.
- The file must still parse: run the check given in your task (python build / JSON load / node --check).
- Report: files edited, roughly how many sentences changed, and anything you deliberately left (e.g. a quoted em dash), in under 10 lines.
