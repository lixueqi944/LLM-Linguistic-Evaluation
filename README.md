# LLM Linguistic Evaluation Portfolio

An automated evaluation framework for assessing large language models understanding of English grammatical phenomena.

## Overview

This project evaluates four LLMs (Doubao 1.5 Pro, GPT-4.1, Qwen3-Max, Gemini 2.5 Pro) on three linguistic phenomena using 26 test sentences drawn from the British National Corpus and self-constructed examples.

### Phenomena Evaluated

- **Double Negation (6 items):** Distinguishing litotes (logical cancellation) from negative concord (emphatic negation)
- **Reciprocal Pronouns (12 items):** Participant quantity judgment and acceptability of "each other" vs "one another"
- **Double Genitive (8 items):** Possessive ambiguity (ownership vs depiction vs creation) and interchangeability with of constructions

## Results Summary

| Model | Type | Accuracy |
|---|---|---|
| GPT-4.1 | Manual (web interface) | 97.8% |
| Gemini 2.5 Pro | Manual (web interface) | 91.3% |
| Qwen3-Max | Manual (web interface) | 97.8% |
| Doubao 1.5 Pro | Automated (API) | 87.0% |

## Project Structure

```
AI-Linguist-Portfolio/
├── src/
│   ├── semantic_checker.py  - Automated Doubao evaluation (API + scoring + report)
│   └── import_manual.py     - Import manual results and generate comparison report
├── data/
│   ├── test_sentences.json
│   └── linguistics_rules.md
├── config/
│   ├── models_config.json   - API endpoint and model config
│   ├── manual_results.json  - Paste manually collected model responses here
│   └── .env.example         - Template for API key
├── prompts/
│   └── prompt_{model}.txt
└── reports/
    ├── evaluation_report_doubao_*.md
    ├── evaluation_report_full_plus.md   - With dimension comparison table and radar chart
    └── radar_chart.svg                 - Radar visualization by linguistic dimension
```

## How It Works

### Scoring Method

Each response is scored using a two-stage matching algorithm:

1. **Text containment (bidirectional):** If the response contains the expected answer text, or if the expected answer text contains a shortened version of the answer (e.g., "创作" matches "创作（Painter创作的图片）"), it is marked correct
2. **Option letter mapping:** If text matching fails, the response is checked for the correct multiple-choice letter (A/B/C/D), which is then mapped to its corresponding option text

For sentences with multiple tasks (e.g., reciprocal pronouns and double genitive), each task is scored against its own line of the response rather than the full text, preventing cross-task interference. This flexible approach ensures that formatting differences across models do not penalize linguistically correct answers.

### Key Findings

- Even at temperature=0, the same model gave different answers across multiple runs (Doubao ranged 84.8% to 87.0%)
- Different prompt formats also affected results (from 87.0% to 84.8%)
- Single-run LLM evaluations have inherent variability and should be interpreted with caution

## Requirements

- Python 3.8+
- Doubao API key (via Volcengine) for automated evaluation

## Usage

### 1. Automated Evaluation (Doubao)

```bash
python src/semantic_checker.py
```

This runs Doubao via API, scores all responses, and generates:
- `reports/evaluation_report_doubao_YYYYMMDD_HHMMSS.md` — detailed Doubao report
- `reports/_last_results.json` — structured results for multi-model comparison

### 2. Manual Evaluation (GPT-4.1, Qwen3-Max, Gemini)

Open the corresponding `prompts/prompt_{model}.txt`, paste into the web interface, copy the model response, and paste it into `config/manual_results.json` under the models `full_response` field.

### 3. Generate Full Comparison Report

```bash
python src/import_manual.py
```

This reads both the Doubao results (`reports/_last_results.json`) and your manual results (`config/manual_results.json`), scores everything, and generates a combined comparison report:

- `reports/evaluation_report_full_YYYYMMDD_HHMMSS.md` — all four models side by side

## Reports

| File pattern | Content |
|---|---|
| `reports/evaluation_report_doubao_*.md` | Automated Doubao evaluation results |
| `reports/evaluation_report_full_plus.md` | Final report with dimension comparison table and radar chart |
| `reports/radar_chart.svg` | Radar visualization of model performance by linguistic dimension |

## Author

Li Xueqi — MA in Language Studies

*This project was developed from a course assignment and adapted as a portfolio piece for AI + Linguistics roles.*

