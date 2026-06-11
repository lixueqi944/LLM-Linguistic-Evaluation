# Linguistic Competence Across Four LLMs: An Evaluation Report
- Generated: 2026-06-11 15:00
- Models: GPT-4.1 (School GenAI), Qwen3-Max (School GenAI), Gemini 2.5 Pro (School GenAI), Doubao 1.5 Pro (Volcengine)

## Results Summary
| Model | Type | Accuracy | Correct / Total |
|---|---|---|---|
| GPT-4.1 (School GenAI) | Manual | 97.8% | 45/46 |
| Qwen3-Max (School GenAI) | Manual | 97.8% | 45/46 |
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
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | 两个 可接受 | ✓ |

**Qwen3-Max (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 三个及以上 可接受 | ✓ |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | 两个 可接受 | ✓ |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | 两个 可接受 | ✓ |

**Gemini 2.5 Pro (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | A A | ✓ |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | A A | ✓ |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | A A | ✓ |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | B A | ✓ |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | B A | ✓ |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | B A | ✓ |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | B A | ✓ |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | B A | ✓ |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | B A | ✓ |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | A A | ✓ |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | A A | ✓ |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | A A | ✓ |

**Doubao 1.5 Pro (Volcengine)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| RP-01 | That meant he and Sara had hours and hours of hang... | 两个; 可接受 | 第一个任务：A 第二个任务：A | ✓ |
| RP-02 | I cry quietly because I don’t want to wake my mum.... | 两个; 可接受 | 第一个任务：A 第二个任务：A | ✓ |
| RP-03 | I went after him to ask him what his problem was -... | 两个; 可接受 | 第一个任务答案：A 第二个任务答案：A | ✓ |
| RP-04 | We are sending a message to the world that South A... | 三个及以上; 可接受 | 第一题：B 第二题：A | ✓ |
| RP-05 | It seems to me evident that a family will provide ... | 三个及以上; 可接受 | 第一题：B 第二题：A | ✓ |
| RP-06 | FOOTBALL’S new Premier League becomes more and mor... | 三个及以上; 可接受 | 1. B 2. A | ✓ |
| RP-07 | Women ran screaming with children in their arms, a... | 三个及以上; 可接受 | 1. B 2. A | ✓ |
| RP-08 | It is about creating an expectation that children ... | 三个及以上; 可接受 | 第一题：B 第二题：A | ✓ |
| RP-09 | Because few of us possess universal skills, we lea... | 三个及以上; 可接受 | 第一题：B 第二题：A | ✓ |
| RP-10 | How strangely you talk! Are not the two sexes made... | 两个; 可接受 | 第一题：B 第二题：A | ✗ |
| RP-11 | I leave for Tunbridge, my dear, and hope we shall ... | 两个; 可接受 | 1. B 2. A | ✗ |
| RP-12 | These two things exist independently of one anothe... | 两个; 可接受 | A A | ✓ |

### Double Genitive
**GPT-4.1 (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 可以 强调John这个已知人物 | ✓ |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 可以 强调Fergie这个已知人物 | ✓ |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 可以 强调friend这个新信息 | ✓ |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 可以 强调friend这个新信息 | ✓ |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | 主体 不可以 | ✗ |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | 创作 不可以 | ✓ |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | 主体 不可以 | ✓ |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | 主体 不可以 | ✓ |

**Qwen3-Max (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 可以 A | ✓ |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 可以 A | ✓ |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 不可以 B | ✓ |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 不可以 B | ✓ |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | B 不可以 | ✗ |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | C 不可以 | ✓ |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | B 不可以 | ✓ |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | B 不可以 | ✓ |

**Gemini 2.5 Pro (School GenAI)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | A B | ✗ |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | A A | ✓ |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | B B | ✗ |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | A B | ✓ |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | B B | ✗ |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | C B | ✓ |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | B A | ✗ |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | B B | ✓ |

**Doubao 1.5 Pro (Volcengine)**:
| ID | Sentence (abbreviated) | Expected Answer | Model Response | Correct? |
|---|---|---|---|---|
| DG-01 | He is John’s friend.... | 可以; 强调John这个已知人物 | 第一题：A 第二题：A | ✓ |
| DG-02 | The family is staying in a private apartment loane... | 可以; 强调Fergie这个已知人物 | 第一题答案：A 第二题答案：A | ✓ |
| DG-03 | Later, a friend of Hilton’s called and collected t... | 可以; 强调friend这个新信息 | 第一题：A 第二题：B | ✓ |
| DG-04 | However, since 1979 the company had employed Lina ... | 可以; 强调friend这个新信息 | 第一题答案：A 第二题答案：B | ✓ |
| DG-05 | The teacher knew that Sherman was combining the pr... | 以上都可以，取决于语境; 不可以 | 第一题：B 第二题：B | ✗ |
| DG-06 | The Brygos Painter’s picture is pure archaic; the ... | 创作（Painter创作的图片）; 不可以 | 1. C 2. A | ✗ |
| DG-07 | My mother’s picture shows only a drab, mouse-like ... | 主体（以母亲为主题的照片）; 不可以 | 第一题：D 第二题：A | ✗ |
| DG-08 | He couldn’t keep pretending that Viola and Eleanor... | 主体（以Viola为主题的照片）; 不可以 | 第一题：B 第二题：B | ✓ |

---
*Report structure adapted from linguistic evaluation methodology*
*2026-06-11 15:00*