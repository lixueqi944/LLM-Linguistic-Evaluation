import json, os, sys, time, re
from urllib.request import Request, urlopen
from urllib.error import URLError

sys.stdout.reconfigure(encoding="utf-8")

# ── 0. Load .env file ──
def load_env():
    """Read .env file and set environment variables."""
    env_file = ".env"
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                os.environ[key.strip()] = value.strip().strip("\"'")
load_env()

# ── 1. Load data ──
with open("data/test_sentences.json", "r", encoding="utf-8") as f:
    test_sentences = json.load(f)

with open("config/models_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

models = config["models"]

# ── 2. Define system prompt ──
SYSTEM_PROMPT = """You are a linguistics evaluation assistant. Your task is to answer questions about English sentences based on your linguistic knowledge.

For each sentence, you will be given one or more tasks. Answer each task concisely and precisely.

If asked for options (A, B, C...), respond with only the letter of your chosen answer.
If asked for a yes/no or judgment question, respond with the exact judgment term.
"""

# ── 3. Build evaluation prompts for each sentence ──
def build_evaluation_prompt(s):
    """Build the evaluation prompt for a given test sentence."""
    lines = []
    lines.append(f"Sentence: {s['sentence']}")
    if s.get("context") and s["context"].strip():
        lines.append(f"Context: {s['context']}")
    lines.append("")
    if s["phenomenon"] == "双重否定":
        t = s["task"]
        lines.append(f"Task: {t['question']}")
        if t.get("options"):
            for i, opt in enumerate(t["options"]):
                lines.append(f"  {chr(65+i)}) {opt}")
        lines.append("Answer only the judgment (one word).")
    elif s["phenomenon"] == "相互代词":
        for task in s["tasks"]:
            lines.append(f"Task: {task['question']}")
            for i, opt in enumerate(task["options"]):
                lines.append(f"  {chr(65+i)}) {opt}")
            lines.append("")
    elif s["phenomenon"] == "双重属格":
        for task in s["tasks"]:
            lines.append(f"Task: {task['question']}")
            for i, opt in enumerate(task["options"]):
                lines.append(f"  {chr(65+i)}) {opt}")
            lines.append("")
    return "\n".join(lines)

# ── 4. API call (OpenAI-compatible) ──
def call_api(model_cfg, prompt_text):
    """Call an OpenAI-compatible API."""
    api_key = os.environ.get(model_cfg["api_key_env"])
    if not api_key:
        return None, f"Error: {model_cfg['api_key_env']} not set"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = json.dumps({
        "model": model_cfg["model"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ],
        "temperature": 0,
        "max_tokens": 200
    }).encode("utf-8")
    
    url = model_cfg["api_base"].rstrip("/") + "/chat/completions"
    
    req = Request(url, data=payload, headers=headers, method="POST")
    try:
        resp = urlopen(req, timeout=30)
        result = json.loads(resp.read().decode("utf-8"))
        content = result["choices"][0]["message"]["content"].strip()
        return content, None
    except URLError as e:
        return None, f"API Error: {str(e)}"
    except Exception as e:
        return None, f"Error: {str(e)}"

# ---- 5. Score a response ----
def score_response(s, response):
    """Score a model response against expected answers.
    Rule: if the response contains the expected text, OR contains the correct
    option letter (for multiple-choice items), it's correct. Punctuation and
    formatting are ignored.
    """
    resp_lower = response.lower().strip()
    scores = {}
    
    def get_letters_in_order(resp):
        """Extract answer letters (A-D) in order, one per line of the response."""
        result = []
        for line in resp.splitlines():
            for c in line.strip().upper():
                if c in "ABCD":
                    result.append(c)
                    break
        return result
    
    def contains_text(text):
        """Check if expected text appears anywhere in the response."""
        t = text.lower().strip(); return t in resp_lower or resp_lower in t
    
    def correct_letter_for_task(task):
        """Given a task with options, return the letter (A/B/C/D) of the correct answer."""
        if not task.get("options"):
            return None
        try:
            idx = task["options"].index(task["expected"])
            return chr(ord("A") + idx)
        except ValueError:
            return None
    
    if s["phenomenon"] == "双重否定":
        t = s["task"]
        if contains_text(t["expected"]):
            scores[t["type"]] = 1
        elif t.get("options"):
            correct_letter = correct_letter_for_task(t)
            scores[t["type"]] = 1 if correct_letter and correct_letter.lower() in resp_lower else 0
        else:
            scores[t["type"]] = 0
    
    elif s["phenomenon"] in ["相互代词", "双重属格"]:
        letters = get_letters_in_order(response)
        resp_lines = response.splitlines()
        for i, task in enumerate(s["tasks"]):
            task_line = resp_lines[i].lower().strip() if i < len(resp_lines) else ""
            exp = task["expected"].lower().strip()
            if exp in task_line or task_line in exp:
                scores[task["type"]] = 1
            elif task.get("options"):
                correct_letter = correct_letter_for_task(task)
                if not correct_letter:
                    scores[task["type"]] = 0
                elif i < len(letters) and letters[i] == correct_letter:
                    scores[task["type"]] = 1
                elif correct_letter.lower() in task_line:
                    scores[task["type"]] = 1
                else:
                    scores[task["type"]] = 0
            else:
                scores[task["type"]] = 0
    else:
        for task in s.get("tasks", []):
            scores[task["type"]] = 1 if contains_text(task["expected"]) else 0
    
    return scores

# ── 6. Run evaluation ──
def run_evaluation():
    results = {}
    
    for model in models:
        name = model["name"]
        display = model["display_name"]
        print(f"\n{'='*60}")
        print(f"Evaluating: {display}")
        print(f"{'='*60}")
        
        if model.get("manual", False):
            print(f"  [MANUAL] Generate prompt template for web interface...")
            generate_manual_prompts(model)
            results[name] = {"status": "manual", "display": display}
            continue
        
        if not model.get("enabled", True):
            print(f"  [SKIPPED] Model disabled in config")
            continue
        
        # Auto API evaluation
        model_results = []
        correct_count = 0
        total_tasks = 0
        
        for i, s in enumerate(test_sentences):
            prompt = build_evaluation_prompt(s)
            print(f"  [{i+1}/{len(test_sentences)}] {s['id']}...", end=" ", flush=True)
            
            response, error = call_api(model, prompt)
            if error:
                print(f"ERROR: {error}")
                continue
            
            scores = score_response(s, response)
            resp_short = response.replace(chr(10), " | ")[:55]
            if len(scores) == 1:
                v = list(scores.values())[0]
                mark = chr(10003) if v == 1 else chr(10007)
                print(f"{mark}  {resp_short}")
            else:
                marks = "/".join(str(v) for v in scores.values())
                print(f"[{marks}]  {resp_short}")
            item_result = {
                "id": s["id"],
                "response": response,
                "scores": scores
            }
            model_results.append(item_result)
            for k, v in scores.items():
                total_tasks += 1
                correct_count += v
            
            time.sleep(0.5)  # Rate limiting
        
        if total_tasks > 0:
            accuracy = (correct_count / total_tasks) * 100
            print(f"\n  Accuracy: {correct_count}/{total_tasks} = {accuracy:.1f}%")
        else:
            accuracy = 0
        
        results[name] = {
            "status": "completed",
            "display": display,
            "results": model_results,
            "accuracy": accuracy,
            "correct": correct_count,
            "total": total_tasks
        }
    
    return results

# ── 7. Generate manual prompt templates ──
def generate_manual_prompts(model):
    output_file = f"prompts/prompt_{model['name']}.txt"
    lines = []
    lines.append("=" * 60)
    lines.append(f"EVALUATION PROMPT FOR: {model['display_name']}")
    lines.append(f"Copy the entire content below and paste into {model['display_name']}")
    lines.append("=" * 60)
    lines.append("")
    lines.append(SYSTEM_PROMPT)
    lines.append("")
    lines.append("-" * 40)
    lines.append("EVALUATION ITEMS")
    lines.append("-" * 40)
    lines.append("")
    lines.append("Please answer ALL of the following. For each item, respond concisely.")
    lines.append("")
    
    for i, s in enumerate(test_sentences):
        lines.append(f"--- Item {i+1}: {s['id']} ---")
        lines.append(build_evaluation_prompt(s))
        lines.append("")
    
    lines.append("=" * 60)
    lines.append("END OF EVALUATION PROMPT")
    lines.append("=" * 60)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Prompt template saved to: {output_file}")

# ── 8. Generate report ──
def generate_report(results):
    report_lines = []
    report_lines.append("# LLM Semantic Evaluation Report")
    report_lines.append("")
    report_lines.append("## Overview")
    report_lines.append("")
    report_lines.append(f"- Test sentences: {len(test_sentences)}")
    report_lines.append(f"- Phenomena: Double Negation (6), Reciprocal Pronouns (12), Double Genitive (8)")
    report_lines.append(f"- Evaluation date: {time.strftime('%Y-%m-%d')}")
    report_lines.append("")
    
    # Summary table
    report_lines.append("## Results Summary")
    report_lines.append("")
    report_lines.append("| Model | Auto/Manual | Accuracy | Correct / Total |")
    report_lines.append("|---|---|---|---|")
    
    for name, data in results.items():
        if data["status"] == "manual":
            report_lines.append(f"| {data['display']} | Manual | Pending | - |")
        else:
            acc = f"{data['accuracy']:.1f}%"
            report_lines.append(f"| {data['display']} | Auto | {acc} | {data['correct']}/{data['total']} |")
    
    report_lines.append("")
    
    # Manual models info
    manual_models = [m for m in models if m.get("manual", False)]
    if manual_models:
        report_lines.append("## Manual Evaluation Results")
        report_lines.append("")
        report_lines.append("The following models are evaluated manually via web interface:")
        report_lines.append("")
        for m in manual_models:
            report_lines.append(f"- **{m['display_name']}**: Paste `prompt_{m['name']}.txt` into the chat interface and paste the response back.")
        report_lines.append("")
        report_lines.append("Once responses are collected, update the script to generate a full comparison table.")
        report_lines.append("")
    
    # Detailed per-phenomenon results (if auto models completed)
    auto_results = [(n, d) for n, d in results.items() if d["status"] == "completed"]
    if auto_results:
        report_lines.append("## Detailed Results by Phenomenon")
        report_lines.append("")
        
        phenomena = [
            ("双重否定", "Double Negation"),
            ("相互代词", "Reciprocal Pronouns"),
            ("双重属格", "Double Genitive")
        ]
        
        for p_key, p_name in phenomena:
            p_sentences = [s for s in test_sentences if s["phenomenon"] == p_key]
            report_lines.append(f"### {p_name}")
            report_lines.append("")
            
            for model_name, data in auto_results:
                report_lines.append(f"**{data['display']}**:")
                report_lines.append("")
                report_lines.append("| ID | Sentence | Expected | Model Response | Score |")
                report_lines.append("|---|---|---|---|---|")
                
                for r in data["results"]:
                    s = next((x for x in test_sentences if x["id"] == r["id"]), None)
                    if s and s["phenomenon"] == p_key:
                        if s["phenomenon"] == "双重否定":
                            exp = s["task"]["expected"]
                            sc = "✓" if r["scores"].get(s["task"]["type"], 0) == 1 else "✗"
                            report_lines.append(f"| {r['id']} | {s['sentence'][:50]}... | {exp} | {r['response'][:40]} | {sc} |")
                        else:
                            exp = "; ".join(t["expected"] for t in s.get("tasks", [s.get("task")]))
                            all_correct = all(v == 1 for v in r["scores"].values())
                            sc = "✓" if all_correct else "✗"
                            report_lines.append(f"| {r['id']} | {s['sentence'][:50]}... | {exp} | {r['response'][:40]} | {sc} |")
                
                report_lines.append("")
    
    # Appendix: Raw results
    if auto_results:
        report_lines.append("## Appendix: Raw API Results")
        report_lines.append("")
        for model_name, data in auto_results:
            report_lines.append(f"### {data['display']} Raw Responses")
            report_lines.append("")
            report_lines.append("```json")
            report_lines.append(json.dumps(data["results"], ensure_ascii=False, indent=2))
            report_lines.append("```")
            report_lines.append("")
    
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("*Report generated by `semantic_checker.py`*")
    report_lines.append(f"*Date: {time.strftime('%Y-%m-%d %H:%M')}*")
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    auto_tag = next((n for n, d in results.items() if d.get("status") == "completed"), "all")
    filename = f"reports/evaluation_report_{auto_tag}_{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    
    print(f"\nReport saved to: {filename}")

# ── Main ──
if __name__ == "__main__":
    results = run_evaluation()
    generate_report(results)
    with open("reports/_last_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Results saved to _last_results.json")
    print("\nDone!")
