---
layout: page
title: KG-QUEST
description: Diagnostic-Guided Graph Reasoning for Biomedical QA
img: assets/img/5.jpg
importance: 3
category: research
related_publications: true
---

**KG-QUEST** is a diagnostic-controlled knowledge graph reasoning framework that constructs **query-specific evidence graphs** at inference time and performs regulated multi-hop reasoning over structured biomedical relations.

### Departure From Prior Work

Unlike GraphRAG-style approaches that treat graphs as retrieval scaffolds, KG-QUEST uses the knowledge graph as the **primary reasoning substrate** and controls graph expansion via interpretable diagnostic signals.

### Pipeline

1. **Seed graph construction** — ontology-aligned triple extraction from the query.
2. **Diagnostic-guided expansion** — balances semantic coverage, ontology consistency, and uncertainty.
3. **Multi-hop aggregation** — with calibrated abstention for unanswerable questions.

### Results

Evaluated on **LiveQA, MedQA, MedMCQA, and MMLU-med**, KG-QUEST shows consistent improvements over retrieval-augmented and LLM-based baselines, particularly on multi-hop clinical reasoning tasks — while maintaining interpretable reasoning paths and low hallucination rates.

*Under review at IEEE TKDE 2026.*
