#!/usr/bin/env python3
"""Generate a deliberately flawed sample dashboard for Do Now 8.C (Critique This Dashboard).

Flaws baked in for learners to find:
- Truncated y-axis (starts at 80) making an 82->98 rise look dramatic
- No denominator or definition of "resolved"
- Slices with near-identical values in a hard-to-read pie
- Missing units, cherry-picked bright colors, no data source note
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pathlib

OUT = pathlib.Path(__file__).parent / "do-now-assets" / "dn-8.C-critique-this-dashboard" / "dashboard-sample.png"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
rate = [82, 85, 84, 90, 94, 98]
cats = ["Billing", "Potholes", "Permits", "Noise", "Parks", "Water", "Other"]
vals = [14, 13, 13, 13, 13, 13, 12]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.6))

ax1.bar(months, rate, color=["#ff2d2d", "#ff7b00", "#ffd400", "#2dff57", "#00c2ff", "#b400ff"])
ax1.set_ylim(80, 100)
ax1.set_title("Citizen Service Resolution Rate Soars!", fontsize=13, fontweight="bold", color="#0a8a00")
ax1.set_ylabel("Rate")
for i, v in enumerate(rate):
    ax1.text(i, v + 0.5, str(v), ha="center", fontsize=9, fontweight="bold")

ax2.pie(vals, labels=cats, autopct="%1.0f%%", startangle=90,
        colors=["#ff2d2d", "#ff7b00", "#ffd400", "#2dff57", "#00c2ff", "#b400ff", "#ff6ee4"])
ax2.set_title("Requests by Category", fontsize=11)

fig.suptitle("311 Service Dashboard - Q1/Q2", fontsize=12)
fig.tight_layout()
fig.savefig(OUT, dpi=140, bbox_inches="tight")
print("wrote", OUT)
