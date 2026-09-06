# Azam Ali Afzal

**AI / GenAI Engineer — agentic systems, RAG, and MLOps for production automation.**

MS Artificial Intelligence @ LUMS · Co-founder @ AZEKTRA · Automation consultant @ Multan Chemicals Ltd.

I build AI systems that hold up outside a notebook. The parts I care about are the
unglamorous ones: what happens when an agent is wrong, how you regression-test a
pipeline whose output changes every run, and where a human has to sit in the loop
before software spends someone's money. My research interest is CI/CD for
non-deterministic systems — which parts of an agent pipeline can safely gate a
build, and which can only be monitored.

---

## Featured work

**[agentic-ops-platform](https://github.com/azamali992/agentic-ops-platform)** — Multi-agent
back-office automation where every state-changing action is human-approval-gated *by
construction*. A supervisor routes to order/inventory/billing specialists; role-based
middleware controls which tools a caller can even see; one risk registry is enforced on
two surfaces — LangChain's `HumanInTheLoopMiddleware` and a real **MCP server**, so an
MCP client can't bypass the approval gate. MLflow tracing, and a CI gate that treats
safety violations as absolute. 88 tests.
`LangChain 1.4 · LangGraph · MCP · MLflow`

**[agentic-rag-eval-gate](https://github.com/azamali992/agentic-rag-eval-gate)** — A
LangGraph-style RAG agent (retrieve → grade → rewrite/retry → generate → self-check)
with an 18-case eval harness and a CI gate that blocks deterministic regressions while
tolerating normal LLM variance. Proven by deliberately breaking retrieval and watching
the gate fail the build.
`RAG · BM25 · CI quality gating · evaluation`

**[multichannel-order-to-erp-agent](https://github.com/azamali992/multichannel-order-to-erp-agent)** —
Turns informal multilingual chat orders (WhatsApp, code-switched Urdu/English) into
confirmed ERP orders: LLM extraction → fuzzy product matching → human confirmation →
ERP sync. Built from a real automation problem at a chemicals distributor.
`LLM extraction · RapidFuzz · FastAPI · Postgres · Docker`

**[streaming-cdc-medallion-pipeline](https://github.com/azamali992/streaming-cdc-medallion-pipeline)** —
Real-time CDC streaming pipeline: Bronze/Silver/Gold medallion architecture with
Delta-Lake-style change data feed, MERGE upsert/delete, windowed aggregation, and
checkpointed micro-batch consumers that resume without reprocessing.
`Spark/Delta patterns · structured streaming · data engineering`

**[diabetic-retinopathy-grading](https://github.com/azamali992/diabetic-retinopathy-grading)** —
Two-stage CORAL ordinal regression cascade for diabetic retinopathy grading (APTOS
2019), **QWK 0.917**. DenseNet121, focal/SORD/EMD losses, SAM + SWA, multi-scale TTA,
GradCAM interpretability, and the full experiment history rather than just the winning run.
`PyTorch · medical imaging · ordinal regression`

**[cnn-shortcut-learning-gradcam](https://github.com/azamali992/cnn-shortcut-learning-gradcam)** —
Diagnosing shortcut learning with a controlled biased/unbiased CNN setup, plus
GradCAM-based interpretability on a ResNet-18 transfer-learning task.
`interpretability · computer vision`

---

## Also on this profile

- **[mental-health-rag-chatbot](https://github.com/azamali992/mental-health-rag-chatbot)** — RAG chatbot backend (FastAPI + LangChain + ChromaDB) behind the TherapyLink app
- **[fyp_therapylink](https://github.com/azamali992/fyp_therapylink)** — Cross-platform Flutter mental-health app with an AI psychologist, sentiment analysis, and mood tracking
- **[cold-email-generator](https://github.com/azamali992/cold-email-generator)** — Scrapes a careers page, extracts postings with an LLM, retrieves matching portfolio work via vector search, drafts a tailored email
- **[haramtextile](https://github.com/azamali992/haramtextile)** · **[mhglobal](https://github.com/azamali992/mhglobal)** · **[mclwebsite](https://github.com/azamali992/mclwebsite)** — Production full-stack B2B sites + admin CMS (Next.js/TypeScript/Prisma, MERN), one with 162 unit + 19 E2E tests

---

## Working with

**AI/GenAI** — LangChain, LangGraph, MCP, RAG, agent middleware, human-in-the-loop design, LLM evaluation
**ML** — PyTorch, TensorFlow, scikit-learn, computer vision, ordinal regression, model interpretability
**MLOps / Data** — MLflow, Spark, Delta Lake, structured streaming, CI quality gates, Docker, GitHub Actions
**Backend / Product** — Python, FastAPI, Node.js, Next.js/TypeScript, PostgreSQL, MongoDB, Oracle APEX, Flutter

## Reach me

azamaliafzal992@gmail.com
