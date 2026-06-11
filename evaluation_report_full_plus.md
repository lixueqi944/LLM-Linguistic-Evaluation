# Linguistic Competence Across Four LLMs: An Evaluation Report
- Generated: 2026-06-07 17:40
- Models: GPT-4.1 (School GenAI), Qwen3-Max (School GenAI), Gemini 2.5 Pro (School GenAI), Doubao 1.5 Pro (Volcengine)

## 1. Results
| Model | Type | Accuracy | Correct / Total |
|---|---|---|---|
| GPT-4.1 (School GenAI) | Manual | 97.8% | 42/46 |
| Qwen3-Max (School GenAI) | Manual | 97.8% | 41/46 |
| Gemini 2.5 Pro (School GenAI) | Manual | 91.3% | 42/46 |
| Doubao 1.5 Pro (Volcengine) | Auto (API) | 87.0% | 40/46 |

### Double Negation
**GPT-4.1 (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DN-01 | It was not impossible for Mr Kinnock to form an ad... | 肯定 | 肯定 | ✓ |
| DN-02 | With an empire of such a size, it was a difficult ... | 肯定 | 肯定 | ✓ |
| DN-03 | And to the normal layman (pause) that sounds bette... | 比什么都不说好 | 比什么都不说好 | ✓ |
| DN-04 | At the Clothes Exchange, dear, you don’t need no m... | 不需要钱 | 不需要钱 | ✓ |
| DN-05 | We don’t need no education.... | 否定 | 否定 | ✓ |
| DN-06 | Nor did you nothing hear?... | 否定 | 否定 | ✓ |

**Qwen3-Max (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DN-01 | It was not impossible for Mr Kinnock to form an ad... | 肯定 | 肯定 | ✓ |
| DN-02 | With an empire of such a size, it was a difficult ... | 肯定 | 肯定 | ✓ |
| DN-03 | And to the normal layman (pause) that sounds bette... | 比什么都不说好 | 比什么都不说好 | ✓ |
| DN-04 | At the Clothes Exchange, dear, you don’t need no m... | 不需要钱 | 不需要钱 | ✓ |
| DN-05 | We don’t need no education.... | 否定 | 否定 | ✓ |
| DN-06 | Nor did you nothing hear?... | 否定 | 否定 | ✓ |

**Gemini 2.5 Pro (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DN-01 | It was not impossible for Mr Kinnock to form an ad... | 肯定 | 肯定 | ✓ |
| DN-02 | With an empire of such a size, it was a difficult ... | 肯定 | 肯定 | ✓ |
| DN-03 | And to the normal layman (pause) that sounds bette... | 比什么都不说好 | 比什么都不说好 | ✓ |
| DN-04 | At the Clothes Exchange, dear, you don’t need no m... | 不需要钱 | 不需要钱 | ✓ |
| DN-05 | We don’t need no education.... | 否定 | 否定 | ✓ |
| DN-06 | Nor did you nothing hear?... | 否定 | 否定 | ✓ |

**Doubao 1.5 Pro (Volcengine)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DN-01 | It was not impossible for Mr Kinnock to form an ad... | 肯定 | 肯定 | ✓ |
| DN-02 | With an empire of such a size, it was a difficult ... | 肯定 | 肯定 | ✓ |
| DN-03 | And to the normal layman (pause) that sounds bette... | 比什么都不说好 | A | ✓ |
| DN-04 | At the Clothes Exchange, dear, you don’t need no m... | 不需要钱 | 不需要钱 | ✓ |
| DN-05 | We don’t need no education.... | 否定 | 否定 | ✓ |
| DN-06 | Nor did you nothing hear?... | 否定 | 否定 | ✓ |

### Reciprocal Pronouns
**GPT-4.1 (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 两个 |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 两个 |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 两个 |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 三个及以上 |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 三个及以上 |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 三个及以上 |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 三个及以上 |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 三个及以上 |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 三个及以上 |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 两个 |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | 两个 |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | 两个 |

**Qwen3-Max (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 两个 |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 两个 |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 两个 |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 三个及以上 |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 三个及以上 |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 三个及以上 |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 三个及以上 |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 三个及以上 |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 三个及以上 |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 两个 |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | 两个 |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | 两个 |

**Gemini 2.5 Pro (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | A |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | A |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | A |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | B |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | B |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | B |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | B |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | B |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | B |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | A |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | A |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | A |

**Doubao 1.5 Pro (Volcengine)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 第一个任务：A |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 第一个任务：A |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 第一个任务答案：A |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 第一题：B |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 第一题：B |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 1. B |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 1. B |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 第一题：B |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 第一题：B |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 第一题：B |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | 1. B |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | A |

### Double Genitive
**GPT-4.1 (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 可以 |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 可以 |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 可以 |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 可以 |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | 主体 |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | 创作 |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | 主体 |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | 主体 |

**Qwen3-Max (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 可以 |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 可以 |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 不可以 |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 不可以 |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | B |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | C |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | B |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | B |

**Gemini 2.5 Pro (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | A |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | A |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | B |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | A |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | B |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | C |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | B |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | B |

**Doubao 1.5 Pro (Volcengine)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 第一题：A |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 第一题答案：A |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 第一题：A |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 第一题答案：A |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | 第一题：B |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | 1. C |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | 第一题：D |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | 第一题：B |

---
---



---

## 2. Performance by Linguistic Dimension


The table below breaks down each model accuracy by linguistic dimension, rather than by phenomenon.


| Dimension | Description | GPT-4.1 (School GenAI) | Qwen3-Max (School GenAI) | Gemini 2.5 Pro (School GenAI) | Doubao 1.5 Pro (Volcengine) |

|---|---|---|---|---|---|

| **Semantic Judgment** | Interpret meaning of target structure | 100.0% (6/6) | 100.0% (6/6) | 100.0% (6/6) | 100.0% (6/6) |
| **Quantity Judgment** | Identify number of participants | 100.0% (12/12) | 100.0% (12/12) | 100.0% (12/12) | 83.3% (10/12) |
| **Acceptability Judgment** | Judge naturalness in context | 100.0% (12/12) | 100.0% (12/12) | 100.0% (12/12) | 100.0% (12/12) |
| **Ambiguity Identification** | Recognize semantic ambiguity | 75.0% (3/4) | 75.0% (3/4) | 75.0% (3/4) | 50.0% (2/4) |
| **Interchangeability** | Judge interchangeability of structures | 100.0% (8/8) | 100.0% (8/8) | 75.0% (6/8) | 75.0% (6/8) |
| **Pragmatic Focus** | Identify pragmatic function | 100.0% (4/4) | 100.0% (4/4) | 75.0% (3/4) | 100.0% (4/4) |

*Semantic Judgment: tested on Double Negation items*

*Quantity & Acceptability: tested on Reciprocal Pronouns items*

*Ambiguity, Interchangeability & Pragmatic Focus: tested on Double Genitive items*




### Radar Chart Overview

![Model Performance Radar Chart](radar_chart.svg)

## 3. Discussion

### Double Negation (100% - all models)

All models achieved perfect scores on double negation.

**This might be because the semantic rules of double negation are relatively clear – either it cancels out the negation and turns it into a positive, or it emphasizes that it remains a negation. There are also plenty of such examples in the training data.**

### Reciprocal Pronouns

All models handled reciprocal pronouns well. The three manually tested models scored 12/12, while Doubao (tested automatically via API) showed minor variation.

**The only errors were on RP-10 and RP-11, where Doubao consistently answered 'three or more' instead of 'two' across all five runs. Both sentences contain explicit participant cues ('the two sexes', 'we'), yet the error persisted, suggesting this may not be random fluctuation.**

### Double Genitive (most challenging)

This phenomenon showed the most variation across models. The picture/photo category (DG-05 to DG-08) required distinguishing possession vs depiction vs creation readings.

**Most models handled the friend category (DG-01 to DG-04) correctly, but errors increased significantly in the picture/photo category (DG-05 to DG-08). From a linguistic perspective, picture/photo nouns allow three genitive readings (possession, depiction, creation), while friend nouns allow fewer. LLMs struggled more with the more ambiguous category, suggesting they are less reliable when multiple interpretations are possible.**

### Methodological Note

Even at temperature=0, the same model gave different answers across multiple runs (Doubao ranged 84.8% to 87.0%). Additionally, using a stricter prompt format also changed the results — accuracy dropped from 87.0% to 84.8%. This suggests that LLM evaluation results are sensitive to both prompt phrasing and inherent response variability, and single-run results should be interpreted as approximate rather than definitive.

---

## 4. Conclusion

**1.** The four models achieved accuracy rates between 87% and 97.8% across three linguistic phenomena, indicating a considerable understanding of English grammatical structures.

**2.** All models scored 100% on double negation. Errors mainly appeared in double genitive (ambiguous genitive readings) and reciprocal pronouns (collective noun distinction), suggesting that LLMs are less reliable when handling structures with semantic ambiguity.

**3.** This project demonstrates that combining linguistic knowledge with automated evaluation tools can effectively assess LLM language capabilities and provides a foundation for more systematic evaluations in the future.

---

*Results and analysis by the author using an automated evaluation framework*
*2026-06-07 17:40*