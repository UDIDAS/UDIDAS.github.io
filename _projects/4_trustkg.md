---
layout: page
title: TrustKG
description: Trustworthy Clinical Knowledge Graph Construction
img: assets/img/7.jpg
importance: 1
category: research
related_publications: false
---

**TrustKG** tackles a core problem in clinical AI: turning heterogeneous, unstructured clinical narratives into knowledge graphs you can actually trust downstream.

### Problem

LLM-based knowledge extraction from clinical text is powerful but unreliable — hallucinated triples, unsupported claims, and overconfident outputs are unacceptable when the graph feeds clinical reasoning or decision support.

### Approach

TrustKG builds ontology-aligned multimodal knowledge graphs from clinical narratives with trust as a first-class design goal:

- **Retrieval grounding** — every extracted fact is tied back to supporting evidence in the source text.
- **Uncertainty-aware validation** — calibrated confidence at the triple level, so downstream consumers know what to rely on.
- **Selective construction** — the pipeline abstains rather than guessing when evidence is insufficient.

### Status

Under review at **IEEE Big Data 2026**.
