---
layout: page
title: KG-RAG
description: Clinical Knowledge Graph Construction with Multi-LLM Agents
img: assets/img/1.jpg
importance: 1
category: research
related_publications: true
---

**KG-RAG** is an end-to-end framework for constructing and evaluating clinical knowledge graphs from unstructured oncology narratives using multi-agent LLM pipelines.

### Problem

Constructing accurate, clinically grounded knowledge graphs from free-text medical narratives is hard: rigid schemas like FHIR lack semantic flexibility, and LLM outputs suffer from hallucinations and semantic drift — issues especially critical in oncology.

### Approach

The framework integrates four components:

1. **Prompt-driven extraction** — entity, attribute, and relation extraction using multiple LLMs (Gemini 2.0 Flash, GPT-4o, Grok 3) operating as specialized agents.
2. **Entropy-based uncertainty scoring** — quantifies extraction confidence at the triplet level.
3. **Ontology-aligned RDF/OWL schema generation** — aligns extracted entities with SNOMED CT, LOINC, and other biomedical ontologies.
4. **Multi-LLM consensus validation** — cross-checks outputs across models for hallucination detection and semantic refinement.

### Results

Applied to two oncology cohorts (PDAC and BRCA), KG-RAG produces interpretable, SPARQL-compatible, and clinically grounded knowledge graphs **without gold-standard annotations**, achieving consistent gains in precision, relevance, and ontology compliance over baselines.

[arXiv:2601.01844](https://arxiv.org/abs/2601.01844)
