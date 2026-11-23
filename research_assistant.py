
from pathlib import Path
from collections import Counter
import re

# AI server industry research example
research_text = """
The AI server market is driven by growing demand
for artificial intelligence computing infrastructure.

Major computing platforms include NVIDIA GPUs
and Huawei Ascend AI processors.

Key components include GPUs, CPUs, memory,
networking equipment, storage and cooling systems.

Important industry trends include increasing
computing demand, liquid cooling adoption,
and domestic AI chip development.

Business customers focus on computing performance,
procurement costs, energy efficiency,
delivery capability and technical support.
"""

keywords = [
    "AI", "GPU", "CPU", "NVIDIA", "Huawei",
    "Ascend", "cooling", "computing",
    "memory", "costs", "customers"
]

text_lower = research_text.lower()
counts = {
    word: len(re.findall(
        r"\b" + re.escape(word.lower()) + r"\b",
        text_lower
    ))
    for word in keywords
}

found = {k: v for k, v in counts.items() if v > 0}
sentences = [
    s.strip()
    for s in re.split(r"[.!?]+", research_text)
    if s.strip()
]

report = [
    "# AI Server Industry Research Report",
    "",
    "## 1. Overview",
    research_text.strip(),
    "",
    "## 2. Keyword Analysis",
]

for word, count in sorted(
    found.items(), key=lambda item: -item[1]
):
    report.append(f"- {word}: {count}")

report.extend([
    "",
    "## 3. Key Findings",
])

for sentence in sentences:
    if any(
        term in sentence.lower()
        for term in ["demand", "trends", "customers"]
    ):
        report.append(f"- {sentence}.")

report.extend([
    "",
    "## 4. Methodology",
    "Rule-based keyword extraction and sentence filtering.",
    "This version does not use a large language model.",
    "",
    "## 5. Disclaimer",
    "Demonstration using illustrative input text.",
    "Findings require verification against real sources."
])

output = Path("industry_research_report.md")
output.write_text(
    "\n".join(report),
    encoding="utf-8"
)

print("Research report generated successfully!")
print(f"Output file: {output}")
print(f"Keywords identified: {len(found)}")
