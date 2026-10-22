---
layout: page
title: WeListen
description: A community feedback & survey platform with live focus groups and an analytics dashboard
img: assets/img/welisten_logo.png
importance: 1
category: software
related_publications: false
---

<a href="https://www.welisten-ai.org/" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-primary">Visit welisten-ai.org →</a>

**WeListen** is a survey and community-feedback web platform built for **Our Health Jackson County**, supporting regional health-disparity initiatives in the Kansas City area. It lets community organizations run structured surveys and live, moderated focus-group sessions, then turns the collected responses into analytics that inform public-health decisions.

### Features

**For participants**

- **Account sign-up and sign-in** with Firebase Authentication
- **QR-code session joining** — participants scan a code to enter a focus group, with a confirmation flow that keeps onboarding friction low
- **Tiered surveys** — question sets are organized into tiers stored in Firestore, so organizers can stage questions across sessions
- **Live focus-group chat** — real-time moderated group discussions built on Stream Chat, with speech-to-text input (Web Speech API via `react-speech-recognition`) so participants can talk instead of type
- **Guided onboarding tour** of the interface (`reactour`)

**For organizers & moderators**

- **Focus-group management** — create sessions, assign moderators, and track moderator presence
- **Survey authoring** — manage survey tiers and questions directly from the admin console
- **Analytics dashboard** — word clouds, network graphs, and response charts summarizing what the community is saying (D3, Recharts, `react-wordcloud`)
- **Data export** — serverless Python Cloud Functions bundle focus-group transcripts and survey responses into CSV/ZIP archives (pandas) for downstream analysis

### Technology

| Layer     | Stack                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------- |
| Front end | React 18 (Create React App) · React Router 6 · Bootstrap 5 / Reactstrap · styled-components        |
| Real-time | Stream Chat API · `react-speech-recognition` (voice input) · QR flows (`qrcode.react`)             |
| Analytics | D3 · Recharts · `react-wordcloud` · `react-flip-numbers`                                           |
| Backend   | Firebase — Authentication, Firestore, Hosting · Python Cloud Functions (pandas, CSV/ZIP export)    |

### My Role

I contributed to the development of the platform as part of the UMKC team — a collaboration also serving the **United Way of Greater Kansas City** and the **Hispanic Development Fund** through companion deployments.
