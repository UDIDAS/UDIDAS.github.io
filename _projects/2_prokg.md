---
layout: page
title: ProKG
description: Triplet-Level Bayesian Reasoning for Robust LLM Safety
img: assets/img/3.jpg
importance: 2
category: research
related_publications: true
---

**ProKG** is a probabilistic knowledge graph reasoning framework that treats LLM safety assessment as **Bayesian inference over ⟨subject, predicate, object⟩ triplets**.

### Key Idea

Rather than relying on keyword heuristics or fixed-hop knowledge graph traversal, each triplet is modeled as a random variable with an explicit posterior belief. Uncertainty is propagated through the relational structure using joint and conditional Bayesian updates — enabling adaptive, evidence-driven reasoning.

### Why It Matters

Current LLM safety defenses suffer from:
- Over-defense on benign inputs that happen to contain attack-related surface patterns
- Brittle decision boundaries under adversarial pressure
- Limited interpretability

ProKG's probabilistic, triplet-level reasoning addresses all three by making uncertainty a first-class citizen.

### Results

On **NOTINJECT** and **ADVBENCH**, ProKG substantially reduces false-positive refusals on benign trigger-containing inputs while maintaining strong robustness against adversarial jailbreak attacks — at practical inference cost.

*Under review at ACL 2026.*
