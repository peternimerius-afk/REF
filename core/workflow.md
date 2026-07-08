# Workflow

REF processing follows a defined sequence.

## 1. Import

Import source documents from Word, Excel, PDF, Markdown or text.

## 2. Parse

Transform source documents into a normalized document model containing headings, tables, paragraphs, rows, cells and lists.

## 3. Classify

Classify content as:

- requirement;
- evidence;
- explanation;
- background;
- scope;
- assumption;
- comment;
- question;
- duplicate;
- ignore.

## 4. Create requirement objects

Detected requirements become structured Requirement Objects.

## 5. Normalize

Apply engineering principles:

- split obligations;
- remove evidence;
- remove explanation;
- remove subjective wording;
- compress wording;
- preserve procurement intent.

## 6. Determine evaluation strategy

Apply the evaluation engine:

- binary;
- scoreable;
- reject;
- split;
- request clarification.

## 7. Map capabilities

Map each requirement to one or more capabilities in the catalog.

## 8. Run gap analysis

Compare expected capabilities from project configuration with capabilities covered by requirements.

## 9. Generate recommendations

Produce recommended actions:

- keep;
- rewrite;
- split;
- convert to binary;
- convert to scoreable;
- delete;
- add missing requirement.

## 10. Export

Export revised requirement set, review report and gap analysis.
