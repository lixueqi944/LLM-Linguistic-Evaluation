# Linguistics Evaluation Rules

## 1. Overview

This document defines the evaluation criteria for assessing large language models' (LLMs) understanding of three English grammatical phenomena. Each phenomenon is analysed from a descriptive linguistics perspective, drawing on corpus evidence from the British National Corpus (BNC).

### 1.1 Evaluation Dimensions

| Dimension | Description | Scoring |
|---|---|---|
| Semantic Judgment | Whether the model correctly interprets the semantic function of the target structure | 0/1 per item |
| Quantity Judgment | Whether the model correctly identifies the number of participants involved | 0/1 per item |
| Acceptability Judgment | Whether the model correctly judges naturalness in authentic contexts | 0/1 per item |
| Ambiguity Identification | Whether the model recognises semantic ambiguity in the target structure | 0/1 per item |
| Interchangeability | Whether the model correctly judges whether two structures are semantically interchangeable | 0/1 per item |
| Pragmatic Focus | Whether the model correctly identifies the pragmatic function of structural choice | 0/1 per item |

### 1.2 Scoring Formula

For each phenomenon, the overall score is calculated as:

`Accuracy = (Correct items / Total items) x 100%`

Results are reported by phenomenon, by dimension, and by model.

---

## 2. Double Negation

### 2.1 Linguistic Background

English double negation manifests two distinct functions (Huddleston & Pullum, 2002; Labov, 1972):

- **Function A (Litotes / Logical Cancellation)**: Two negatives cancel each other out, yielding an affirmative meaning (e.g., *it is not impossible* = it is possible). This construction is characteristic of formal written English and serves a hedging or euphemistic function.
- **Function B (Negative Concord / Emphatic Negation)**: Multiple negative elements co-occur to reinforce a single negation (e.g., *I don't know nothing* = I know nothing). This pattern is characteristic of vernacular speech, certain dialects (e.g., AAVE), and historical stages of English (Lowth, 1762).

### 2.2 Evaluation Task

| Task | Question | Scoring |
|---|---|---|
| Semantic Judgment | "Does this sentence express an affirmative or negative meaning?" | Correct = 1, Incorrect = 0 |

### 2.3 Judgment Criteria

- Sentences containing a negation-within-negation construction where the overall meaning is affirmative (Function A) should be judged as **Affirmative**.
- Sentences where multiple negatives serve to emphasise a single negation (Function B) should be judged as **Negative**.
- Contextual and register information, where provided, should inform the judgment.

### 2.4 Examples

| Sentence | Expected | Rationale |
|---|---|---|
| It was not impossible for Mr Kinnock to form an administration... | Affirmative | Function A: litotes, formal register |
| At the Clothes Exchange, dear, you don't need no money down there. | Negative | Function B: negative concord, colloquial register |

*The full test set (6 items) is maintained in `test_sentences.json`.*

---

## 3. Reciprocal Pronouns: each other vs. one another

### 3.1 Linguistic Background

Prescriptive grammar rules stipulate that (Quirk et al., 1985):

- **each other** should be used exclusively for **two** participants
- **one another** should be reserved for **three or more** participants

However, corpus evidence (Biber et al., 1999; also confirmed by the present author's BNC analysis) demonstrates that this distinction is not consistently observed in authentic usage. Both forms occur across participant numbers, with register and stylistic preference playing a more significant role than number restriction.

### 3.2 Evaluation Tasks

| Task | Question | Scoring |
|---|---|---|
| Quantity Judgment | "How many participants are involved in this action? Two, or three or more?" | Correct = 1, Incorrect = 0 |
| Acceptability Judgment | "Is this sentence natural and acceptable to a native speaker in authentic contexts?" | Correct = 1, Incorrect = 0 |

### 3.3 Judgment Criteria

**Quantity Judgment:**
- The number of participants should be determined from the semantic content of the sentence and contextual clues, NOT from prescriptive rules about which reciprocal pronoun is used.
- The expected answer reflects the actual referents in the clause.

**Acceptability Judgment:**
- Since all test items in the full set are sourced from the BNC (authentic, naturally occurring language), they are all considered **Acceptable**.
- This aligns with the descriptive linguistic principle that corpus-attested usage constitutes valid evidence of natural language.

### 3.4 Examples

| Sentence | Structure | Participants | Expected Qty | Expected Acceptability |
|---|---|---|---|---|
| ...we clung to each other and cried together. | each other | 2 (dyadic) | Two | Acceptable |
| ...millionaires vie with each other to buy the title. | each other | 3+ (league context) | Three or more | Acceptable |
| Are not the two sexes made for one another? | one another | 2 | Two | Acceptable |

*The full test set (12 items, balanced across 2x2 conditions) is maintained in `test_sentences.json`.*

---

## 4. Double Genitive: Sb's N vs. N of Sb's

### 4.1 Linguistic Background

English possesses two genitive constructions for expressing possession (Huddleston & Pullum, 2002):

- **Type A (Sb's N)**: The prenominal genitive (e.g., *John's friend*)
- **Type B (N of Sb's)**: The postnominal double genitive (e.g., *a friend of John's*)

The present author's BNC analysis (Assignment 2, LANG7640) reveals a crucial distinction based on noun category:

**Friend-class nouns** (friend, colleague, etc.):
- The two structures are semantically **interchangeable**
- However, they differ in **pragmatic focus**: Type A (Sb's friend) foregrounds the known referent, while Type B (a friend of Sb's) introduces the person-denoting noun as new information

**Picture-class nouns** (picture, photo, painting, etc.):
- The two structures are **NOT interchangeable**
- Type A (Sb's picture) exhibits **three-way ambiguity**: possession, subject-of-the-image, and authorship
- Type B (a picture of Sb's) unambiguously expresses **possession only**

### 4.2 Evaluation Tasks

| Task | Question | Scoring |
|---|---|---|
| Ambiguity Identification | "What relationship does the genitive NP express?" | Correct = 1, Incorrect = 0 |
| Interchangeability | "Can this be rewritten as the alternative genitive structure without changing core meaning?" | Correct = 1, Incorrect = 0 |
| Pragmatic Focus | "Why might a speaker choose one structure over the other?" | Correct = 1, Incorrect = 0 |

### 4.3 Judgment Criteria

**Friend-class:**
- Interchangeability: YES -- the two structures convey the same propositional meaning
- Pragmatic focus: Sb's N emphasises the known person; N of Sb's introduces the person-denoting noun as new information

**Picture-class:**
- Interchangeability: NO -- Sb's N allows multiple interpretations (possession/subject/creation), while N of Sb's is restricted to possession
- Ambiguity: Where the context disambiguates, the specific interpretation should be identified. Where context is absent or ambiguous, multiple interpretations are possible.

### 4.4 Examples

| Sentence | Category | Expected Ambiguity | Expected Interchangeability |
|---|---|---|---|
| He is John's friend. | friend | -- (possession only) | Interchangeable |
| Later, a friend of Hilton's called... | friend | -- (possession only) | Interchangeable |
| The Brygos Painter's picture is pure archaic... | picture | Creation | NOT interchangeable |
| My mother's picture shows only a drab... girl... | picture | Subject | NOT interchangeable |

*The full test set (8 items, balanced across noun categories) is maintained in `test_sentences.json`.*

---

## 5. References

- Biber, D., Johansson, S., Leech, G., Conrad, S., & Finegan, E. (1999). *Longman Grammar of Spoken and Written English*. Longman.
- Huddleston, R., & Pullum, G. K. (2002). *The Cambridge Grammar of the English Language*. Cambridge University Press.
- Labov, W. (1972). Negative attraction and negative concord. In *Language in the Inner City*. University of Pennsylvania Press.
- Lowth, R. (1762). *A Short Introduction to English Grammar*. London: J. Hughs.
- Quirk, R., Greenbaum, S., Leech, G., & Svartvik, J. (1985). *A Comprehensive Grammar of the English Language*. Longman.

---

*Document prepared by Li Xueqi | Codex-assisted formatting*
*Based on BNC corpus analysis conducted for LANG7640 Grammar of Modern English*

