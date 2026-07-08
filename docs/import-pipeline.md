# Import Pipeline

**Version:** 0.1.0  
**Status:** Draft

The import pipeline converts documents into structured content units and Requirement Objects.

## Supported sources

REF should support:

- Word documents
- Excel workbooks
- PDF files
- Markdown
- Plain text
- YAML or JSON

## Pipeline

```text
File
 ↓
Parser
 ↓
Document model
 ↓
Content units
 ↓
Classification
 ↓
Requirement detection
 ↓
Requirement Objects
```

## Document model

The parser should preserve:

- Headings
- Paragraphs
- Tables
- Rows
- Columns
- Lists
- Numbering
- Page references where available
- Comments where available

## Content unit

```yaml
id: CU-001
type: paragraph
text: The solution shall support SAML 2.0 authentication.
source:
  document: requirements.docx
  section: 5.2
  paragraph: 4
```

For Excel:

```yaml
id: CU-EXCEL-001
type: cell
text: Monthly availability shall be at least 99.9%.
source:
  document: requirements.xlsx
  worksheet: NFR
  row: 12
  column: Re-written requirement
```

## Parser responsibilities

Parsers shall extract structure.

Parsers shall not rewrite, normalize, or evaluate requirements.

## Import quality

Import should report:

```yaml
import_summary:
  documents: 1
  content_units: 184
  requirements_detected: 96
  evidence_detected: 22
  low_confidence_items: 7
```
