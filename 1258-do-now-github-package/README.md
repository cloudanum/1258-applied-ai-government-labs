# 1258 Do Now standalone package

Open `1258-Workbook-Standalone.html` first. It links each Do Now to its asset pack under `do-now-assets/`.

Contents:
- `1258-Workbook-Standalone.html` / `.pdf` (92 pages): searchable/linked master guide with activity↔solution links, relative asset-pack links, and the same enriched content as the asset folders (comprehensive goals, detailed run steps, key takeaways, Study Further links, sample rows, bonus tasks). No sandbox required; everything runs mentally on Mural or in Zoom chat.
- `1258-Workbook-Standalone_custom.html` / `_custom.pdf`: same guide plus a "Targeted students" block on every activity, naming up to 3 of the 11 enrolled students whose intake-sheet interests match the activity, with a short note on why it helps them. Built by `customize_guide.py`.
- `1258-Workbook-Standalone_custom_filter.html` / `_custom_filter.pdf`: student filter edition. Sticky filter bar shows only the activities relevant to one student (about 40 percent each), plus a static Student relevance map. Built by `filter_guide.py`.
- `do-now-assets/`: 41 numbered asset folders with enriched READMEs (comprehensive goal, detailed run steps for Mural/Zoom-chat delivery, key takeaway, validated Study Further links, optional bonus tasks), links, board-item TSVs, solutions, and generated sample images.
- `accuracy-validation.json` / `url-validation.json`: validation reports for activity coverage and URLs (including the Study Further and MITRE ATLAS links).
- `enrich_guide.py`: regenerates the master guide HTML from the asset-folder READMEs. `customize_guide.py`: builds the `_custom` student-targeted edition. Reprint PDFs with headless Chrome after running either.

Use in class: share one Mural link at activity start. Use `do-now-assets/manifest.tsv` as the index.
