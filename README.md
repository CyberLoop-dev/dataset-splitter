<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=160&section=header&text=Dataset%20Splitter&fontSize=38&fontColor=ffffff" width="100%" alt="Dataset Splitter banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=0F766E&center=true&vCenter=true&width=820&lines=Make+repeatable+dataset+splits+in+one+command" alt="Animated project title" />
<p>Split CSV datasets into reproducible train, validation, and test files, with optional label-based stratification.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/dataset-splitter?style=for-the-badge" alt="MIT license" /> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/dataset-splitter?style=for-the-badge" alt="Top language" /> <img src="https://img.shields.io/github/stars/CyberLoop-dev/dataset-splitter?style=for-the-badge" alt="Stars" /> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/dataset-splitter?style=for-the-badge" alt="Last commit" /></p>
<img src="assets/illustration.svg" width="92%" alt="Dataset splitting illustration" /></div>

## 🎯 Overview

Dataset Splitter prepares a CSV file for machine-learning experiments by creating train, validation, and test files. A fixed random seed makes the result repeatable. When a label column is supplied, rows are split within each label group to keep class proportions as balanced as the dataset size allows.

## ✨ Features

- 📊 Creates train, validation, and test CSV files.
- ⚖️ Supports optional label-based stratification.
- 🎲 Uses a configurable seed for reproducible results.
- 🧾 Preserves the original CSV header and source file.
- ✅ Reports output row counts and split proportions.

## 🎬 Demo

<pre><code>python main.py examples/sample.csv --label-column category --seed 42 --output-dir split-data</code></pre>

No hosted demo is claimed; the sample CSV is included.

## 🚀 Quick Start

<pre><code>python main.py examples/sample.csv --label-column category --seed 42 --output-dir split-data</code></pre>

## 🧰 Tech Stack

- Python 3.10+ standard library
- csv and random modules; no third-party packages

## 🗂️ Folder Structure

<pre><code>dataset-splitter/
├── main.py
├── requirements.txt
├── examples/
│   └── sample.csv
└── assets/
    └── illustration.svg</code></pre>

## 🧭 Roadmap

- [ ] Add JSONL input support.
- [ ] Add configurable group-aware splitting.
- [ ] Add a machine-readable split summary.

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, explain behavior changes, and include a reproducible example for bug reports.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer" /></div>
