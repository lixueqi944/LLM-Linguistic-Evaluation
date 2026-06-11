# LLM Semantic Evaluation Report

## Overview

- Test sentences: 26
- Phenomena: Double Negation (6), Reciprocal Pronouns (12), Double Genitive (8)
- Evaluation date: 2026-06-05

## Results Summary

| Model | Auto/Manual | Accuracy | Correct / Total |
|---|---|---|---|
| Doubao 1.5 Pro (Volcengine) | Auto | 84.8% | 39/46 |
| GPT-4.1 (School GenAI) | Manual | Pending | - |
| Qwen3-Max (School GenAI) | Manual | Pending | - |
| Gemini 2.5 Pro (School GenAI) | Manual | Pending | - |

## Manual Evaluation Results

The following models are evaluated manually via web interface:

- **GPT-4.1 (School GenAI)**: Paste `prompt_gpt41.txt` into the chat interface and paste the response back.
- **Qwen3-Max (School GenAI)**: Paste `prompt_qwen3max.txt` into the chat interface and paste the response back.
- **Gemini 2.5 Pro (School GenAI)**: Paste `prompt_gemini25pro.txt` into the chat interface and paste the response back.

Once responses are collected, update the script to generate a full comparison table.

## Detailed Results by Phenomenon

### Double Negation

**Doubao 1.5 Pro (Volcengine)**:

| ID | Sentence | Expected | Model Response | Score |
|---|---|---|---|---|
| DN-01 | It was not impossible for Mr Kinnock to form an ad... | 肯定 | 肯定 | ✓ |
| DN-02 | With an empire of such a size, it was a difficult ... | 肯定 | 肯定 | ✓ |
| DN-03 | And to the normal layman (pause) that sounds bette... | 比什么都不说好 | A | ✓ |
| DN-04 | At the Clothes Exchange, dear, you don’t need no m... | 不需要钱 | 不需要钱 | ✓ |
| DN-05 | We don’t need no education.... | 否定 | 否定 | ✓ |
| DN-06 | Nor did you nothing hear?... | 否定 | 否定 | ✓ |

### Reciprocal Pronouns

**Doubao 1.5 Pro (Volcengine)**:

| ID | Sentence | Expected | Model Response | Score |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 第一个任务：A
第二个任务：A | ✓ |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 第一个任务：A
第二个任务：A | ✓ |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 第一个任务：A
第二个任务：A | ✓ |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 第一题：B
第二题：A | ✓ |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 1. B
2. A | ✓ |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 1. B
2. A | ✓ |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 第一题：B
第二题：A | ✓ |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 第一题：B
第二题：A | ✓ |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 1. B
2. A | ✓ |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 1. B
2. A | ✗ |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | B
A | ✗ |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | 第一个任务答案：A
第二个任务答案：A | ✓ |

### Double Genitive

**Doubao 1.5 Pro (Volcengine)**:

| ID | Sentence | Expected | Model Response | Score |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 第一题：A
第二题：A | ✓ |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 第一题答案：A
第二题答案：A | ✓ |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 第一题答案：A
第二题答案：B | ✓ |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 第一题答案：A
第二题答案：B | ✓ |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | 第一题：B
第二题：B | ✗ |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | 第一题：C
第二题：A | ✗ |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | 第一题：D
第二题：A | ✗ |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | 第一题答案：B
第二题答案：A | ✗ |

## Appendix: Raw API Results

### Doubao 1.5 Pro (Volcengine) Raw Responses

```json
[
  {
    "id": "DN-01",
    "response": "肯定",
    "scores": {
      "semantic_judgment": 1
    }
  },
  {
    "id": "DN-02",
    "response": "肯定",
    "scores": {
      "semantic_judgment": 1
    }
  },
  {
    "id": "DN-03",
    "response": "A",
    "scores": {
      "semantic_judgment": 1
    }
  },
  {
    "id": "DN-04",
    "response": "不需要钱",
    "scores": {
      "semantic_judgment": 1
    }
  },
  {
    "id": "DN-05",
    "response": "否定",
    "scores": {
      "semantic_judgment": 1
    }
  },
  {
    "id": "DN-06",
    "response": "否定",
    "scores": {
      "semantic_judgment": 1
    }
  },
  {
    "id": "RP-01",
    "response": "第一个任务：A\n第二个任务：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-02",
    "response": "第一个任务：A\n第二个任务：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-03",
    "response": "第一个任务：A\n第二个任务：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-04",
    "response": "第一题：B\n第二题：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-05",
    "response": "1. B\n2. A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-06",
    "response": "1. B\n2. A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-07",
    "response": "第一题：B\n第二题：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-08",
    "response": "第一题：B\n第二题：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-09",
    "response": "1. B\n2. A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-10",
    "response": "1. B\n2. A",
    "scores": {
      "quantity_judgment": 0,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-11",
    "response": "B\nA",
    "scores": {
      "quantity_judgment": 0,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "RP-12",
    "response": "第一个任务答案：A\n第二个任务答案：A",
    "scores": {
      "quantity_judgment": 1,
      "acceptability_judgment": 1
    }
  },
  {
    "id": "DG-01",
    "response": "第一题：A\n第二题：A",
    "scores": {
      "interchangeability": 1,
      "pragmatic_focus": 1
    }
  },
  {
    "id": "DG-02",
    "response": "第一题答案：A\n第二题答案：A",
    "scores": {
      "interchangeability": 1,
      "pragmatic_focus": 1
    }
  },
  {
    "id": "DG-03",
    "response": "第一题答案：A\n第二题答案：B",
    "scores": {
      "interchangeability": 1,
      "pragmatic_focus": 1
    }
  },
  {
    "id": "DG-04",
    "response": "第一题答案：A\n第二题答案：B",
    "scores": {
      "interchangeability": 1,
      "pragmatic_focus": 1
    }
  },
  {
    "id": "DG-05",
    "response": "第一题：B\n第二题：B",
    "scores": {
      "ambiguity_identification": 0,
      "interchangeability": 1
    }
  },
  {
    "id": "DG-06",
    "response": "第一题：C\n第二题：A",
    "scores": {
      "ambiguity_identification": 1,
      "interchangeability": 0
    }
  },
  {
    "id": "DG-07",
    "response": "第一题：D\n第二题：A",
    "scores": {
      "ambiguity_identification": 0,
      "interchangeability": 0
    }
  },
  {
    "id": "DG-08",
    "response": "第一题答案：B\n第二题答案：A",
    "scores": {
      "ambiguity_identification": 1,
      "interchangeability": 0
    }
  }
]
```

---

*Report generated by `semantic_checker.py`*
*Date: 2026-06-05 18:57*