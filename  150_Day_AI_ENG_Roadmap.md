# Pro Max AI Engineer — 150-Day Complete Roadmap

> **Every skill from AI Engineering + ML/DL depth combined.**  
> After Day 150: deployed portfolio, certified, interview-ready, offer-ready.  
> Sourced from 500+ live 2026 job postings + Claude Certified Architect exam guide.

| Metric | Value |
|--------|-------|
| Total Days | 150 |
| Weeks | 22 |
| Projects Deployed | 8+ |
| Certification | Claude Certified Architect – Foundations |
| Target Salary | $140K–$185K base (2026 data) |

## Legend

| Tag | Meaning |
|-----|---------|
| 🟢 MILESTONE | Major deployed project — portfolio + resume + case study |
| 🟡 MINI | Focused assignment — commit to GitHub |
| 🔵 CERT PREP | Study / practice for Claude Certified Architect exam |
| 🟣 CONNECTS | ML depth day that feeds directly into main AI track |

## Roadmap Overview

| Phase | Days | Skills | Milestone Projects |
|-------|------|--------|-------------------|
| **Phase 1 — Foundations** | Days 1–35 | LLM APIs · Prompt Engineering · Embeddings · Vector DBs · RAG (4 variants) · Production SaaS · Auth · Billing · CI/CD · Observability | Chat with PDF SaaS + Production RAG SaaS |
| **Phase 2 — Agents & Orchestration** | Days 36–65 | Agentic loops · LangGraph · Claude Agent SDK · Hooks · Multi-agent · MCP (custom + community) · Voice AI · Vision AI | Multi-agent research system + Voice assistant + Custom MCP server |
| **Phase 3 — Production Systems** | Days 66–99 | Data AI · NL→SQL · LLMOps · Cost/latency optimisation · Security · Prompt injection · Structured output mastery · Batch processing | Data AI platform + Structured extraction pipeline |
| **ML Depth — Parallel Track** | Days 1–30 (run alongside Phase 1) | NumPy · Pandas · scikit-learn · PyTorch from scratch · CNNs · LSTMs · Transformer attention · Keras · HuggingFace · LoRA/QLoRA · MLOps | Fine-tuned Llama + Dockerised model endpoint |
| **Phase 4 — Deep ML** | Days 100–120 | Classical ML benchmarks · PyTorch Trainer · ResNet fine-tuning · BERT fine-tuning · QLoRA · RAG vs fine-tune · MLflow · Evidently drift | ML model serving pipeline + Drift monitoring system |
| **Phase 5 — Pro Tier** | Days 121–150 | System design at scale · Claude Code mastery · Capstone project · Portfolio · Resume · Blog · Certification · Interview mastery | Capstone (deployed, case study published) + Certified + Offers |

## Day 0 Setup Checklist

Complete all of these before Day 1:

- [ ] Python 3.12+ with pyenv
- [ ] VS Code + Pylance + Jupyter extension
- [ ] Git + GitHub account + SSH key configured
- [ ] Anthropic API key — claude.ai → Settings → API Keys
- [ ] OpenAI API key — platform.openai.com
- [ ] Pinecone account (free) — pinecone.io
- [ ] Neon PostgreSQL account (free) — neon.tech
- [ ] Vercel account (free) — vercel.com
- [ ] Railway account (free tier) — railway.app
- [ ] HuggingFace account (free) — huggingface.co
- [ ] Weights & Biases account (free) — wandb.ai
- [ ] Langfuse account (free) — langfuse.com
- [ ] Tavily API key (web search for agents) — tavily.com
- [ ] Cohere API key (reranking) — cohere.com
- [ ] Clerk account (auth) — clerk.com
- [ ] Stripe account (billing) — stripe.com
- [ ] Upstash Redis (rate limiting + queues) — upstash.com

## Free Resources Master List

### Courses (all free or audit-free)

| Course | Link | What you'll learn |
|--------|------|-------------------|
| Andrew Ng ML Specialization | coursera.org/specializations/machine-learning-introduction | Classical ML foundations |
| DeepLearning.AI Short Courses | learn.deeplearning.ai | RAG, agents, prompt eng, fine-tuning — all free |
| HuggingFace NLP Course | huggingface.co/learn/nlp-course | Transformers, fine-tuning, datasets |
| fast.ai Practical Deep Learning | fast.ai | PyTorch top-down approach |
| LangGraph Academy | academy.langchain.com | Stateful agents, free tier |
| W&B MLOps Course | wandb.ai/courses/mlops-course | Experiment tracking, sweeps |
| Karpathy Neural Networks Zero to Hero | youtube.com/@AndrejKarpathy | Build GPT from scratch |
| 3Blue1Brown Essence of Linear Algebra | youtube.com/3blue1brown | Math intuition for ML |
| StatQuest with Josh Starmer | youtube.com/@statquest | Classical ML explained clearly |

### Books (legally free online)

- **Hands-On ML with scikit-learn, Keras & TensorFlow** — Aurélien Géron (O'Reilly 3rd ed)
- **Deep Learning** — Goodfellow, Bengio, Courville — deeplearningbook.org
- **Anthropic docs** — docs.anthropic.com — primary reference for Claude APIs
- **promptingguide.ai** — comprehensive prompt engineering reference

---

## Phase 1 — Foundations

**Days 1–35 · 5 Weeks**

> LLM APIs → Prompt Engineering → Embeddings → RAG (4 variants) → Production SaaS with auth, billing, CI/CD, observability

### WEEK 1  ·  LLM Landscape & API Basics   ▸  GOAL: Build a streaming chatbot + understand the full AI landscape

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **1** | AI Landscape | AI vs ML vs DL vs LLM; what AI engineers build vs ML researchers; career paths overview | Karpathy 'Intro to LLMs' YouTube (1h); Anthropic docs home page | Write 1-page personal AI landscape doc; set up Python 3.12 env; install VS Code + Jupyter | Notes doc: AI landscape + career paths |
| **2** | LLM APIs | Anthropic SDK + OpenAI SDK setup; API keys; making first completion call; reading raw JSON response | Anthropic quickstart docs; OpenAI quickstart docs | Call Claude API + GPT-4o with same prompt; print raw response JSON; inspect stop_reason field | CLI: 'hello Claude' + 'hello GPT-4o' working |
| **3** | Tokens & Cost | Tokenisation mechanics; context windows (8K/32K/200K); cost per token; when context fills up | Anthropic tokeniser tool; OpenAI tokenizer playground | Tokenise 10 different inputs; count tokens; calculate cost; find where 32K context breaks | 🟡 MINI PROJECT: Token counter script + cost spreadsheet |
| **4** | Temperature & Params | temperature, top_p, top_k, max_tokens, stop sequences; determinism vs creativity tradeoffs | Anthropic API params docs; blog: 'LLM sampling strategies explained' | Test same prompt at temp 0.0 / 0.5 / 1.0 / 1.5; document output differences across 5 use cases | Temperature experiment log (markdown) |
| **5** | Streaming | Streaming API responses token-by-token; SSE (server-sent events); handling partial chunks in Python | Anthropic streaming docs; Python asyncio basics | Stream Claude response to terminal; measure time-to-first-token; add typing animation | Streaming terminal chatbot |
| **6** | Chat UI v1 | Next.js 15 scaffold; Vercel AI SDK useChat hook; streaming to browser; basic Tailwind styling | Next.js docs; Vercel AI SDK useChat docs | Scaffold Next.js app; wire AI SDK chat route; render streamed markdown responses in browser | Browser streaming chatbot (localhost) |
| **7** | Deploy + Review | Vercel deployment; environment variables; production vs dev API keys; fix bugs from days 1–6 | Vercel deploy docs; .env.local patterns | Deploy to Vercel; share live URL; review all week-1 code; write weekly learning notes | 🟡 MINI PROJECT: Live streaming chatbot (Vercel URL) |

### WEEK 2  ·  Prompt Engineering (Deep Dive)   ▸  GOAL: Master every prompting technique; build reusable prompt library of 30+ prompts

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **8** | System Prompts | System vs user vs assistant roles; persona injection; context setting; instruction hierarchy | Anthropic system prompt docs; Claude usage examples | Write 10 system prompts for different personas (teacher, code reviewer, customer support agent...) | 10 system prompt templates |
| **9** | Few-Shot Prompting | 1-shot, 2-shot, N-shot; example selection strategy; formatting examples; order effects | promptingguide.ai few-shot section; Anthropic cookbook examples | Write 5 few-shot prompts with 3 examples each; test with 0-shot baseline; measure consistency | Few-shot experiment notebook |
| **10** | Chain of Thought | CoT prompting; zero-shot CoT ('think step by step'); tree of thought; when CoT helps vs hurts | Wei et al. CoT paper (read abstract + examples); Anthropic CoT guide | Apply CoT to 5 reasoning tasks (math, logic, code); measure accuracy improvement over direct answer | 🟡 MINI PROJECT: CoT vs direct comparison doc |
| **11** | Structured Output (text) | Asking for JSON / XML / YAML in prompt; format instructions; parsing output; failure modes | Anthropic structured output docs; blog: 'Getting reliable JSON from LLMs' | Get Claude to return JSON for 5 different schemas using only prompt instructions (no tool_use yet) | JSON extraction from prompt (5 schemas) |
| **12** | Prompt Precision | Explicit criteria vs vague instructions; false positive reduction; severity levels; category-based filtering | Exam guide domain 4.1; real code review prompt examples | Write code review prompt v1 (vague); iterate to v3 (explicit category criteria); measure FP rate | Code review prompt v1 → v3 + FP comparison |
| **13** | Advanced Techniques | XML tags for structure; role play; negative instructions; prompt chaining basics; prefilling | Anthropic advanced prompting docs; Claude prompt library | Build prompt chain: step 1 extract → step 2 analyse → step 3 summarise on same document | 🟡 MINI PROJECT: 3-step prompt chain script |
| **14** | Prompt Library | Organise all prompts; test edge cases; document failure modes; version control prompts in Git | — | Compile 30-prompt library (10 system prompts + 10 task prompts + 10 chains); commit to GitHub | 🟢 MILESTONE: Prompt library repo (GitHub, 30 prompts) |

### WEEK 3  ·  Embeddings, Vector DBs & Semantic Search   ▸  GOAL: Build production-grade semantic search from scratch

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **15** | Embeddings Math | What embeddings are; cosine similarity derivation; dot product vs cosine; embedding dimensions | StatQuest 'Word Embeddings' YouTube; 3Blue1Brown 'Dot products' YouTube | Embed 50 sentences; compute cosine similarity matrix; find top-5 similar for each; visualise | Cosine similarity matrix (numpy) |
| **16** | Embedding Models | text-embedding-3-small vs large vs BGE vs E5; benchmark accuracy vs cost vs speed; choosing the right model | OpenAI embedding docs; MTEB leaderboard (huggingface.co) | Benchmark 3 embedding models on 100 sentence pairs; compare similarity scores + latency + cost | Embedding model benchmark report |
| **17** | ChromaDB | Local vector store; collections; add/query/update/delete; metadata filtering; persistent storage | ChromaDB docs quickstart | Build local semantic search on 500 Wikipedia paragraphs; query with 10 questions; return top-3 | 🟡 MINI PROJECT: Semantic search on Wikipedia corpus |
| **18** | Pinecone | Cloud vector DB; index types (dense/sparse/hybrid); namespaces; metadata; upsert + query at scale | Pinecone quickstart; Pinecone metadata filtering docs | Create Pinecone index; upsert 1000 embeddings; benchmark query latency; add metadata filter | Cloud semantic search (Pinecone) |
| **19** | pgvector | PostgreSQL vector extension; ivfflat index; combining SQL + vector search; when to use vs dedicated vector DB | pgvector GitHub docs; Neon pgvector tutorial | Set up pgvector on Neon; store 500 records; run hybrid SQL + vector queries | SQL + vector hybrid search |
| **20** | Chunking Strategies | Fixed-size; recursive character; semantic; document-aware; chunk overlap; metadata preservation | LangChain text splitter docs; blog: 'A guide to chunking strategies for RAG' | Split same 50-page PDF with 4 chunking strategies; compare retrieval quality on 20 test questions | 🟡 MINI PROJECT: Chunking strategy comparison (4 methods) |
| **21** | Re-ranking | BM25 hybrid retrieval; Cohere rerank; cross-encoder re-ranking; why re-ranking improves precision | Cohere rerank docs; blog: 'Improving RAG with re-ranking' | Add Cohere rerank to ChromaDB retrieval; test on 20 questions; compare precision@3 before/after | 🟢 MILESTONE: Semantic search + rerank (measured improvement) |

### WEEK 4  ·  RAG Systems (Full Build)   ▸  GOAL: Ship a production 'Chat with PDF' RAG app with eval pipeline

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **22** | Naive RAG (no framework) | Full RAG pipeline: load → chunk → embed → store → retrieve → augment → generate; no LangChain | Anthropic 'Building with Claude' docs; own prior work | Build complete RAG from scratch using only Anthropic SDK + ChromaDB; no LangChain | RAG v1: raw Python, no framework |
| **23** | LangChain RAG | LCEL (LangChain Expression Language); create_retrieval_chain; create_stuff_documents_chain; source docs | LangChain LCEL docs; RAG tutorial | Rebuild RAG v1 in LangChain LCEL; compare code length and readability; note LangChain abstractions | RAG v2: LangChain LCEL |
| **24** | LlamaIndex RAG | VectorStoreIndex; QueryEngine; NodeParser; Response synthesisers; when to use LlamaIndex vs LangChain | LlamaIndex quickstart docs; LlamaIndex vs LangChain comparison blog | Rebuild RAG in LlamaIndex; compare output quality with LangChain version on same 20 test questions | 🟡 MINI PROJECT: RAG v3: LlamaIndex + comparison table |
| **25** | Advanced RAG | Parent-child chunking; multi-query retriever; step-back prompting; HyDE (Hypothetical Document Embeddings) | LangChain advanced RAG docs; HyDE paper (skim abstract) | Add multi-query retriever + HyDE to LangChain RAG; test on hard questions; measure recall improvement | Advanced RAG v4 (measured improvement) |
| **26** | RAG Evaluation | RAGAS: faithfulness, answer relevance, context recall, context precision; setting up eval dataset | RAGAS docs; DeepLearning.AI 'Building + Evaluating Advanced RAG' | Create 50 Q&A eval set; run RAGAS on all 4 RAG versions; build comparison dashboard | RAGAS eval dashboard (4 RAG versions) |
| **27** | 'Chat with PDF' App | Full-stack: Next.js + FastAPI + ChromaDB + Claude; PDF upload UI; source citation; streaming answers | Vercel AI SDK; FastAPI docs; PyMuPDF docs | Build complete app: upload PDF → chunk → embed → chat with sources cited → stream answer | 🟡 MINI PROJECT: Chat with PDF app v1 (working, local) |
| **28** | Deploy + Eval Pipeline | Deploy to Vercel + Railway; add RAGAS eval as CI step; source citation UI polish; error handling | Railway deploy docs; Vercel docs | Deploy app to production; wire eval pipeline to run on PR; add proper error states + loading UI | 🟢 MILESTONE: Project 1: Chat with PDF (deployed, eval pipeline, source citations) |

### WEEK 5  ·  Production SaaS: Auth, DB, Billing, CI/CD   ▸  GOAL: Ship production RAG SaaS with real users and billing

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **29** | Authentication | Clerk auth: sign-up / sign-in / sign-out; protected routes; user object; session management; webhooks | Clerk docs; Clerk Next.js integration guide | Add Clerk to Chat with PDF; protect /chat; associate uploaded PDFs + chat history with user ID | Auth system (Clerk, protected routes) |
| **30** | Database Design | PostgreSQL schema design for AI apps; Drizzle ORM; migrations; storing chat history + messages | Drizzle ORM docs; Neon PostgreSQL free tier | Design + migrate schema: users / conversations / messages / documents; test CRUD operations | Database schema + migrations (Drizzle) |
| **31** | Persist Chat History | Store every message in DB; load history on page refresh; conversation list sidebar; delete conversation | Drizzle query docs | Wire message storage to chat API; load messages on mount; render conversation list; add delete | 🟡 MINI PROJECT: Persistent chat history UI |
| **32** | Rate Limiting | Upstash Redis rate limiter; per-user request limits; global API limits; 429 error handling + UX | Upstash rate limit docs; blog: 'Rate limiting Next.js APIs' | Add rate limiter (10 req/min free, 100 req/min pro); test with 15 rapid requests; show user-friendly error | Rate-limited API |
| **33** | Billing with Stripe | Stripe Checkout; subscription plans (Free/Pro); webhooks for subscription events; usage-based billing thoughts | Stripe Next.js docs; Stripe webhooks guide | Add Free (5 PDFs/mo) + Pro ($9/mo unlimited) plans; test full checkout → subscription → cancel flow | Stripe billing (Free + Pro plans) |
| **34** | Observability | Langfuse integration: trace every LLM call; track latency, cost, token usage; set up alerts | Langfuse docs; Langfuse Next.js integration | Instrument all Claude calls with Langfuse; create cost dashboard; set alert for >$0.50/day | 🟡 MINI PROJECT: Langfuse observability dashboard |
| **35** | Testing + CI/CD | Jest unit tests; Playwright E2E; GitHub Actions pipeline (lint → test → deploy); preview deployments | Playwright docs; GitHub Actions docs | Write 20 unit tests + 5 E2E tests; set up full CI pipeline; configure Vercel preview for every PR | 🟢 MILESTONE: Project 2: Production RAG SaaS (auth + billing + CI/CD + observability) |

---

## Phase 2 — Agents & Orchestration

**Days 36–65 · 5 Weeks**

> Agentic loops → LangGraph → Claude Agent SDK → Multi-agent → MCP (custom + community) → Voice AI

### WEEK 6  ·  Agentic Loops & Tool Use   ▸  GOAL: Build autonomous agent loop + reusable tool library

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **36** | Agentic Loop | stop_reason 'tool_use' vs 'end_turn'; loop control flow; appending tool_results to history; anti-patterns (NL termination, arbitrary caps) | Anthropic tool use docs; exam guide domain 1.1 | Build agentic loop from scratch in raw Python; test with calculator + search tools; handle both stop reasons | Raw agentic loop (pure Python, no framework) |
| **37** | Tool Schemas | JSON schema for tool input_schema; required vs optional params; description quality; tool naming conventions; edge case handling | Anthropic tool schema docs; exam guide domain 2.1 | Define 5 tools with excellent descriptions; test that Claude selects each correctly on 10 ambiguous queries | 5-tool library with selection test results |
| **38** | Tool Execution | Executing tool calls safely; error handling in tools; returning structured results; tool result format | Anthropic tool result docs | Add real execution to tools: web search (Tavily), calculator, Python REPL, file read, current time | 🟡 MINI PROJECT: 5 working tools with real execution |
| **39** | tool_choice | tool_choice: auto vs any vs forced; when to force a specific tool first; using any to guarantee tool call | Anthropic tool_choice docs; exam guide domain 2.3 | Implement all 3 tool_choice modes; force extract_metadata before enrichment; test 'any' for structured output | tool_choice demo (all 3 modes) |
| **40** | LangGraph Basics | StateGraph; nodes + edges; conditional edges; START / END nodes; state schema (TypedDict); checkpointing | LangGraph quickstart; LangGraph Academy free tier | Rebuild agentic loop in LangGraph StateGraph; add conditional routing based on tool result | LangGraph ReAct agent |
| **41** | LangGraph Advanced | Parallel branches; human-in-the-loop nodes; interrupt_before; subgraphs; streaming graph state | LangGraph 'How-to guides' docs | Add parallel tool execution branch; add human approval node for file writes; stream intermediate steps | 🟡 MINI PROJECT: LangGraph agent with HITL + parallel branches |
| **42** | Memory Systems | Short-term (conversation buffer); summary memory; long-term (vector DB); episodic memory; Mem0 | LangMem docs; Mem0 GitHub; LangGraph memory docs | Add long-term memory to LangGraph agent; store + retrieve user facts across 5 separate sessions | Agent with cross-session long-term memory |

### WEEK 7  ·  Claude Agent SDK & Hooks   ▸  GOAL: Master Anthropic's Agent SDK; build hooks + enforcement patterns

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **43** | Agent SDK Basics | AgentDefinition; system prompts; allowedTools config; running an agent; reading output | Claude Agent SDK docs | Install Claude Agent SDK; build first agent with 3 tools; run on 5 tasks; inspect output structure | First Claude Agent SDK agent |
| **44** | Hooks: PostToolUse | PostToolUse hook pattern; intercepting tool results; normalising data formats (Unix ts → ISO 8601, status codes → strings) | Claude Agent SDK hooks docs; exam guide domain 1.5 | Implement PostToolUse hook that normalises timestamps + status codes from 3 different mock MCP tools | 🟡 MINI PROJECT: PostToolUse normalisation hook |
| **45** | Hooks: Pre-execution | Tool call interception hooks; blocking policy-violating actions; redirecting to alternative workflows; deterministic vs probabilistic enforcement | Exam guide domain 1.4–1.5 | Implement refund-block hook (>$500 → escalate); test that it blocks 100% of the time vs prompt-only approach | Business rule enforcement hook (deterministic) |
| **46** | Session Management | --resume; fork_session; named sessions; stale context problem; when to resume vs start fresh with injected summary | Exam guide domain 1.7; Claude Code session docs | Practice --resume on a named session; use fork_session to compare 2 refactoring approaches; document findings | Session management practice log |
| **47** | Task Decomposition | Prompt chaining vs dynamic adaptive decomposition; per-file analysis passes + cross-file integration pass; adaptive investigation plans | Exam guide domain 1.6 | Build prompt chain for code review (per-file → cross-file → summary); test on 5-file PR | 🟡 MINI PROJECT: Multi-pass code review pipeline |
| **48** | Error Handling | Structured error responses: isError, errorCategory (transient/validation/permission/business), isRetryable; local recovery vs escalation | Exam guide domain 2.2; MCP error handling docs | Build mock tool with all 4 error types; test agent recovery behaviour for each; add retry logic for transient | Error-handling test suite (4 error types) |
| **49** | Escalation Patterns | Escalation triggers: explicit customer request, policy gap, inability to progress; structured handoff summaries; sentiment ≠ complexity | Exam guide domain 5.2 | Build customer support agent with explicit escalation criteria + few-shot examples; test on 10 escalation scenarios | 🟢 MILESTONE: Customer support agent with escalation (tested) |

### WEEK 8  ·  Multi-Agent Systems   ▸  GOAL: Build full coordinator + parallel subagent research pipeline

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **50** | Hub & Spoke Architecture | Coordinator-subagent pattern; context isolation; all communication routes through coordinator; observability benefits | Anthropic multi-agent docs; exam guide domain 1.2 | Design coordinator + 3 subagents on paper; implement coordinator that delegates to search + analysis subagents | Coordinator scaffold (2 subagents) |
| **51** | Context Passing | Subagents do NOT inherit parent context; passing structured context in prompt; separating content from metadata; attribution preservation | Exam guide domain 1.3 | Pass web search results + document analysis to synthesis subagent via structured JSON in prompt; verify attribution intact | 🟡 MINI PROJECT: Context passing demo (attribution preserved) |
| **52** | Parallel Subagents | Spawning multiple Task tool calls in single coordinator response; measuring speedup vs sequential; parallel vs sequential decision | Exam guide domain 1.3; Claude Agent SDK Task tool docs | Spawn 3 parallel subagents for 3 independent research topics; measure latency vs sequential; compare quality | Parallel subagent speedup benchmark |
| **53** | Iterative Refinement | Coordinator evaluates synthesis output for gaps; re-delegates to search with targeted queries; loops until coverage sufficient | Exam guide domain 1.2 | Build coordinator that checks synthesis output against required topic list; re-searches missing topics; max 3 loops | Iterative research refinement loop |
| **54** | Error Propagation | Structured error context (failure type, attempted query, partial results, alternatives); access failure vs empty result distinction; coverage annotations | Exam guide domain 5.3 | Simulate subagent timeout mid-research; test coordinator recovery; output coverage-annotated report | 🟡 MINI PROJECT: Error propagation + partial results demo |
| **55** | Multi-Agent Research System | Web search + document analysis + synthesis + report generation agents; provenance tracking; conflict annotation | — | Build 4-agent research system; configure .mcp.json with Tavily MCP; deploy; run on 3 real research topics | 🟢 MILESTONE: Project 3: Multi-agent research system (deployed, sourced reports) |
| **56** | Context Management | 'Lost in the middle' effect; case facts blocks; trimming verbose tool outputs; position-aware ordering; scratchpad files | Exam guide domain 5.1 + 5.4 | Reproduce lost-in-middle with 10K+ context; fix with case facts block; measure answer quality improvement | Context management benchmark (before/after) |

### WEEK 9  ·  MCP: Model Context Protocol   ▸  GOAL: Build custom MCP server + integrate 3 community MCP servers

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **57** | MCP Architecture | MCP protocol: servers, tools, resources, prompts; client-server architecture; JSON-RPC transport; tool discovery at connection time | MCP official docs (modelcontextprotocol.io); Anthropic MCP guide | Read full MCP spec overview; connect first community MCP server (filesystem); inspect discovered tools | MCP filesystem server connected |
| **58** | MCP Config | Project-level .mcp.json vs user-level ~/.claude.json; environment variable expansion (${GITHUB_TOKEN}); multi-server simultaneous access | Exam guide domain 2.4; MCP config docs | Configure .mcp.json with GitHub MCP server using env var for token; verify both filesystem + GitHub tools available | 🟡 MINI PROJECT: Multi-MCP config (.mcp.json) |
| **59** | MCP Resources | Resources as content catalogs (issue summaries, doc hierarchies, DB schemas); reducing exploratory tool calls; resource templates | MCP resources spec; Anthropic MCP resources guide | Build MCP server that exposes a resource catalog of 20 markdown files; test that agent reads catalog before searching | MCP server with resource catalog |
| **60** | Custom MCP Server v1 | Python MCP SDK; FastMCP; defining tools with input schemas; implementing tool handlers; testing locally | MCP Python SDK docs; FastMCP docs | Build custom MCP server with 3 tools (get_weather, search_products, create_ticket); test with Claude Desktop | Custom MCP server v1 (3 tools) |
| **61** | Custom MCP Server v2 | Structured error responses (isError, errorCategory, isRetryable); auth (API key via env var); input validation; logging | Exam guide domain 2.2 | Add all 4 error categories to MCP server; add API key auth; add input validation; add request logging | 🟡 MINI PROJECT: Custom MCP server v2 (errors + auth) |
| **62** | Tool Distribution | Max 4–5 tools per agent principle; scoped tool access; replacing generic tools with constrained alternatives; cross-role tools | Exam guide domain 2.3 | Audit Project 3 agent tool assignments; refactor to max 5 tools per agent; document tool assignment rationale | Tool distribution refactor + rationale doc |
| **63** | MCP Integration Project | Integrate custom MCP server into multi-agent research system; add GitHub + Jira community MCP servers; full end-to-end test | — | Add custom MCP + GitHub MCP to research system; add Jira ticket creation on report completion; full test | 🟢 MILESTONE: Project 4: Agent + custom MCP + 3 community MCP servers |

### WEEK 10  ·  Multimodal + Voice AI   ▸  GOAL: Build and deploy full voice assistant + vision pipeline

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **64** | Vision Basics | Claude vision API; image formats; base64 encoding; analyzing images in messages; vision use cases | Anthropic vision docs | Send 10 different images to Claude (charts, screenshots, diagrams, photos); extract structured data from each | Vision extraction script (10 image types) |
| **65** | Document Vision | Invoice/receipt OCR with Claude vision; structured data extraction from PDFs as images; handling multi-page docs | Anthropic vision docs; PyMuPDF image extraction | Build invoice OCR pipeline: PDF → images → Claude vision → JSON; test on 20 sample invoices; measure accuracy | 🟡 MINI PROJECT: Invoice OCR pipeline (accuracy measured) |

---

## Phase 3 — Production Systems

**Days 66–99 · 5 Weeks**

> Data AI → LLMOps → Security → Structured output mastery → Batch processing → Red teaming

### WEEK 10  ·  Multimodal + Voice AI (continued)   ▸  GOAL: Build and deploy full voice assistant

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **66** | Image Generation | DALL-E 3 API; Stable Diffusion via Replicate; prompt-to-image; variation; inpainting; image editing | OpenAI image API docs; Replicate API docs | Build image generation tool: text prompt → DALL-E 3 image → display in UI; add style controls | Image generation tool (with UI) |
| **67** | Speech-to-Text | OpenAI Whisper API; audio file transcription; real-time mic input; language detection; diarisation basics | OpenAI Whisper docs; PyAudio docs | Build STT pipeline: mic input → WAV file → Whisper → transcript; test in 3 languages; measure WER | 🟡 MINI PROJECT: STT pipeline (3 languages tested) |
| **68** | Text-to-Speech | OpenAI TTS API; ElevenLabs for realistic voices; streaming audio; voice cloning concepts; SSML basics | OpenAI TTS docs; ElevenLabs API docs | Build TTS pipeline: Claude response → OpenAI TTS → audio playback; compare 5 voices for clarity | TTS pipeline (5 voices compared) |
| **69** | Voice Chat | Combine STT + LLM + TTS; interruption detection; voice activity detection (VAD); conversation turns | WebRTC MDN docs; Daily.co WebRTC quickstart | Build full voice chat: mic → Whisper → Claude → TTS → speaker; add VAD; test 10 full conversations | 🟡 MINI PROJECT: Voice chat (working, 10 test conversations) |
| **70** | OpenAI Realtime API | Realtime WebSocket API; streaming audio in/out; interruption handling; tool calling in real-time; sub-500ms latency | OpenAI Realtime API docs | Integrate Realtime API; achieve <500ms TTFR (time to first response); add interrupt handling | Realtime API integration (<500ms TTFR) |
| **71** | Voice Assistant Deploy | Full voice assistant: wake word → STT → intent → agent tools → TTS → speaker; deploy as web app; mobile-responsive | — | Build complete voice assistant with 5 tools (weather, search, calculator, notes, reminders); deploy | 🟢 MILESTONE: Project 5: Voice AI assistant (deployed, 5 tools, <500ms) |

### WEEK 11  ·  Data AI & NL→SQL   ▸  GOAL: Build AI-powered data intelligence platform

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **72** | NL→SQL Basics | LLM text-to-SQL; schema injection in prompt; query validation before execution; SQL injection prevention; output format | Defog SQLCoder docs; vanna.ai docs; NSQL blog | Build NL→SQL tool on sample Northwind DB; validate with sqlparse; test 20 natural language queries | NL→SQL tool (20 queries tested) |
| **73** | NL→SQL Advanced | Multi-table joins; ambiguous column names; query explanation; error-and-retry loop; read-only DB connection | Blog: 'Production NL→SQL patterns'; LangChain SQL agent docs | Add retry loop (query fails → send error to Claude → fix → retry); add natural language explanation of result | 🟡 MINI PROJECT: NL→SQL with retry + explanation |
| **74** | pandas AI Agent | DataFrame agent; code execution sandbox (E2B); writing + running Python in sandbox; returning chart + insight | LangChain pandas agent; E2B docs; Code Interpreter API docs | Build agent that receives CSV → writes pandas code → executes in E2B sandbox → returns chart + insight | Data analysis agent (E2B sandbox) |
| **75** | Data Visualisation | Recharts in Next.js; Plotly Python; AI-narrated charts; chart type selection agent; accessible chart design | Recharts docs; Plotly Python docs | Build AI component: user asks question → agent selects chart type → renders Recharts → narrates insight | AI chart generator (6 chart types) |
| **76** | Analytics Dashboard | Full data intelligence UI: NL query input → SQL → data fetch → chart + table + narrative → export to CSV | — | Integrate NL→SQL + chart generator + table renderer into unified Next.js dashboard; connect to real DB | 🟡 MINI PROJECT: AI analytics dashboard (Next.js, live) |
| **77** | Knowledge Graph Basics | Neo4j or networkx; entities + relationships; building KG from unstructured text; GraphRAG overview | Neo4j Aura free tier; networkx docs; Microsoft GraphRAG paper (skim) | Build simple KG from 100 Wikipedia paragraphs using Claude entity extraction; visualise with networkx | Simple knowledge graph from text |
| **78** | Data AI Platform | Integrate analytics dashboard + NL→SQL + pandas agent + KG into one unified data AI platform; deploy | — | Wire all components; multi-database support; export results; add Langfuse tracing; deploy to Railway | 🟢 MILESTONE: Project 6: Data AI platform (deployed, multi-DB, traced) |

### WEEK 12  ·  LLMOps: Monitoring, Caching, Cost   ▸  GOAL: Production-grade observability and cost control

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **79** | Cost Optimisation | Prompt caching (cache_control); model routing (haiku for simple / sonnet for complex / opus for deep); token budget setting | Anthropic cost optimisation docs; prompt caching docs | Audit Project 2 costs; add cache_control to system prompts; add model router; target 40% cost reduction | Cost optimisation report (before/after) |
| **80** | Latency Optimisation | Streaming; speculative execution; connection pooling; parallel tool calls; measuring p50/p95/p99; latency budget design | Blog: 'LLM latency at scale'; Anthropic streaming docs | Profile Project 2 p95 latency; implement all optimisations; document gains with before/after metrics | 🟡 MINI PROJECT: Latency profiling report (p95 improved) |
| **81** | Advanced Langfuse | Custom evaluators in Langfuse; scoring LLM outputs; dataset management; A/B prompt testing in production | Langfuse docs: evaluations + datasets | Add 3 custom evaluators to Langfuse (faithfulness, tone, safety); run A/B test on 2 system prompt versions | A/B prompt test results (Langfuse) |
| **82** | Message Batches API | 50% cost savings; 24h processing window; custom_id for correlation; polling for completion; failure handling by custom_id | Anthropic Message Batches API docs; exam guide domain 4.5 | Process 100 doc extractions via Batches API; handle failures; calculate cost savings vs synchronous | Batch processing pipeline (100 docs, cost measured) |
| **83** | Queue Systems | BullMQ for async job processing; job priorities; retries with backoff; job progress; dead-letter queue; Redis connection | BullMQ docs; Upstash Redis docs | Add BullMQ queue to data AI platform for async PDF processing; test with 20 concurrent uploads | 🟡 MINI PROJECT: Async job queue (BullMQ + Redis) |
| **84** | Monitoring + Alerting | PostHog product analytics; Prometheus + Grafana for infra; Sentry for errors; PagerDuty / alerting on cost/latency spikes | PostHog docs; Sentry Next.js docs | Add PostHog events to all user actions; add Sentry error tracking; set cost alert ($1/day threshold) | Full observability stack (PostHog + Sentry + Langfuse) |
| **85** | Drift Detection | Data drift with Evidently; prompt drift; model output drift; embedding drift; retraining triggers; monitoring cadence | Evidently AI docs; blog: 'Monitoring LLM apps in production' | Simulate embedding drift; detect with Evidently; write runbook for drift response; set weekly monitor cron | 🟢 MILESTONE: Drift detection runbook + monitor |

### WEEK 13  ·  Security & Reliability   ▸  GOAL: Harden all systems; prompt injection defence; compliance basics

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **86** | Prompt Injection | Direct injection; indirect injection (via retrieved docs); jailbreaking; defence: input sanitisation, content filtering, instruction hierarchy | OWASP LLM Top 10 (read all 10); Anthropic safety docs | Attempt 10 prompt injection attacks on Project 2; fix all vulnerabilities; document attack → defence pairs | Security audit report (10 attacks + fixes) |
| **87** | PII & Data Privacy | PII detection (Presidio library); redaction before sending to LLM; data residency; GDPR considerations; audit logs | Microsoft Presidio docs; GDPR summary for devs | Add Presidio PII detection + redaction to all user input pipelines; test on 20 PII-containing messages | 🟡 MINI PROJECT: PII redaction pipeline (tested) |
| **88** | API Security | API key rotation; JWT validation; CORS; rate limiting per user + global; input size limits; SSRF prevention | OWASP API Security Top 10; NextAuth security docs | Audit all APIs; add input size limits; add CORS whitelist; rotate all API keys; document security posture | API security checklist (all items resolved) |
| **89** | Reliability Patterns | Circuit breakers; bulkheads; graceful degradation; fallback chains (Claude → GPT-4o → cached); health checks | Blog: 'Reliability patterns for LLM apps'; tenacity docs | Implement circuit breaker on Anthropic client; add GPT-4o fallback; add /health endpoint; chaos test with 429s | Resilient LLM client (circuit breaker + fallback) |
| **90** | Guardrails | Guardrails AI; input validators; output validators; toxic content detection; hallucination detection; custom validators | Guardrails AI docs; Anthropic safety features | Add Guardrails validators to Project 2: profanity filter + JSON schema validator + relevance checker | 🟡 MINI PROJECT: 3 guardrails validators (tested) |
| **91** | Compliance Basics | SOC2 basics for AI apps; data retention policies; user consent; deletion workflows; AI transparency disclosures | Anthropic usage policy; blog: 'Building GDPR-compliant AI apps' | Write data retention policy; add GDPR deletion endpoint; add AI disclosure to UI; document compliance posture | Compliance doc + deletion endpoint |
| **92** | Red Team Exercise | Structured red team: adversarial prompts, data exfiltration attempts, model abuse, rate limit bypass, DoS simulation | OWASP LLM Top 10; blog: 'Red teaming LLM applications' | Run 20-case red team exercise on all projects; fix all P0 vulnerabilities; write red team report | 🟢 MILESTONE: Red team report (20 cases, all P0 fixed) |

### WEEK 14  ·  Advanced Prompt Engineering & Structured Output   ▸  GOAL: Master every structured output pattern + eval technique

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **93** | Few-Shot Mastery | 2–4 targeted examples for ambiguous cases; demonstrating output format; generalisation to novel patterns; example selection strategy | Exam guide domain 4.2 | Create 3 few-shot prompt libraries (code review / data extraction / escalation); test generalisation on 10 novel cases | 3 few-shot prompt libraries (generalisation tested) |
| **94** | tool_use + JSON Schemas | tool_use for guaranteed schema compliance; required vs optional fields; nullable fields to prevent hallucination; enums with 'other' + detail | Exam guide domain 4.3; Anthropic tool_use docs | Build invoice extractor with complex nested JSON schema; compare tool_use vs prompt-only on 20 invoices | 🟡 MINI PROJECT: Invoice extractor: tool_use vs prompt (accuracy table) |
| **95** | Validation + Retry Loops | Append specific validation errors to retry prompt; semantic validation (values sum correctly) vs syntax validation; retry limits; when to give up | Exam guide domain 4.4 | Build extraction pipeline with 3-attempt retry loop; test on 10 malformed documents; log retry success rates | Validation-retry pipeline (retry success rates logged) |
| **96** | Multi-Pass Review | Per-file local analysis + cross-file integration pass; attention dilution problem; independent review instances; self-review limitations | Exam guide domain 4.6 | Build 2-pass code review: per-file → integration; compare single-pass vs 2-pass on 5-file PR; measure coverage | Multi-pass code review (coverage comparison) |
| **97** | Confidence Calibration | Field-level confidence scores; calibration with labeled validation sets; stratified random sampling; routing by confidence | Exam guide domain 5.5 | Add confidence scores to invoice extractor; calibrate on 50 labeled invoices; route low-confidence to review queue | Confidence-calibrated extractor (routing working) |
| **98** | Information Provenance | Claim-source mappings; preserving attribution through synthesis; temporal data handling; conflict annotation; coverage gap reporting | Exam guide domain 5.6 | Refactor research system to output structured claim-source JSON; test citation accuracy on 20 claims | 🟡 MINI PROJECT: Provenance-tracking research system (citations verified) |
| **99** | Structured Data Extraction Pipeline | End-to-end: load varied documents → extract with tool_use → validate → retry → batch → human review routing → export | — | Build complete extraction pipeline for 3 document types (invoices, contracts, resumes); batch 50 docs; route 10% for review | 🟢 MILESTONE: Project 7: Structured extraction pipeline (3 doc types, batch, review routing) |

---

## ML Depth — Parallel Track

**Days 1–30 · Run ALONGSIDE Phase 1 (1–1.5h/day extra)**

> NumPy → Pandas → scikit-learn → PyTorch from scratch → CNNs → LSTMs → Transformers → Keras → HuggingFace → LoRA/QLoRA → MLOps

### WEEK 1  ·  Python for ML   ▸  GOAL: NumPy + Pandas + Matplotlib — data layer foundations

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **ML-D1** | Python for ML | NumPy: arrays, broadcasting, vectorised ops, linear algebra (matmul, dot, norm, SVD); no-loop philosophy | NumPy docs; 3Blue1Brown 'Essence of Linear Algebra' YouTube | Implement matrix multiply, cosine similarity, softmax from scratch — zero Python loops; benchmark vs loop | NumPy fundamentals + cosine similarity fn |
| **ML-D2** | Python for ML | Pandas: DataFrames, loc/iloc, groupby, merge, apply, method chaining, missing values, EDA workflow | Pandas docs; 'Effective Pandas' by Matt Harrison | Full EDA on Titanic: nulls, distributions, correlations, outliers; export clean CSV; 8 summary statistics | 🟡 MINI PROJECT: Titanic EDA notebook (clean CSV) |
| **ML-D3** | Python for ML | Matplotlib + Seaborn: line/bar/scatter/heatmap/pairplot; subplots; styling; data storytelling | Matplotlib + Seaborn docs | Build 10-chart EDA report on Airbnb dataset; write 1 insight sentence per chart; export as PDF | 10-chart EDA visual report |

### WEEK 2  ·  Classical ML   ▸  GOAL: scikit-learn: full ML workflow from raw data to deployed model

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **ML-D4** | Classical ML | ML workflow: train/test split, stratification, k-fold CV, data leakage, sklearn Pipeline, preprocessing (scaler + encoder) | Géron 'Hands-On ML' ch.2; sklearn user guide | Build full sklearn Pipeline on Titanic: StandardScaler + OneHotEncoder + SimpleImputer + LogisticReg; 5-fold CV | sklearn Pipeline (Titanic, 5-fold CV) |
| **ML-D5** | Classical ML | Regression: linear, ridge, lasso, ElasticNet; MSE/MAE/R²; regularisation intuition; bias-variance tradeoff; learning curves | StatQuest regression YouTube; sklearn linear_model docs | Train 4 regression models on California Housing; plot learning curves; compare RMSE + R² | 🟡 MINI PROJECT: Regression benchmark (4 models) |
| **ML-D6** | Classical ML | Classification: logistic reg, SVM, KNN, decision tree; precision/recall/F1/ROC-AUC; confusion matrix; class imbalance (SMOTE) | StatQuest classification YouTube; sklearn metrics docs | Train 4 classifiers on fraud detection (imbalanced); apply SMOTE; compare all metrics; pick best model | Classification benchmark (imbalance handled) |
| **ML-D7** | Classical ML | Ensemble: Random Forest, GradientBoosting, XGBoost, LightGBM; feature importance; Optuna tuning; W&B logging | XGBoost docs; LightGBM docs; Optuna docs; W&B quickstart | Train XGBoost + LightGBM on tabular dataset; tune 50 Optuna trials; log all runs to W&B dashboard | XGBoost vs LightGBM (W&B Optuna tuning) |
| **ML-D8** | Classical ML | Unsupervised: K-Means (elbow), DBSCAN, PCA, t-SNE, UMAP; dimensionality reduction use cases | sklearn clustering docs; StatQuest PCA YouTube | Cluster customer data with K-Means; reduce dimensions with PCA; visualise with UMAP + t-SNE | 🟢 MILESTONE: Customer segmentation (KMeans + UMAP) |

### WEEK 3  ·  Deep Learning   ▸  GOAL: PyTorch from scratch up to fine-tuned transformers

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **ML-D9** | PyTorch Basics | Tensors: creation/ops/GPU transfer; autograd; computation graphs; .grad; gradient flow; in-place gotchas | PyTorch 60-min blitz; fast.ai lesson 1 | Recreate NumPy exercises in PyTorch; move to GPU; inspect .grad; visualise computation graph | PyTorch tensor exercises (GPU) |
| **ML-D10** | Deep Learning | MLP from scratch: nn.Module, forward pass, CrossEntropy + MSE, SGD + Adam, batch training loop — MNIST | PyTorch nn docs; Karpathy 'micrograd' YouTube | Build 3-layer MLP from scratch (no high-level APIs) on MNIST; >98% accuracy; plot loss + accuracy curves | 🟡 MINI PROJECT: MLP from scratch (MNIST >98%) |
| **ML-D11** | Deep Learning | Training loop: DataLoader + Dataset; epochs; validation; early stopping; LR scheduler (CosineAnnealingLR); checkpoint | PyTorch DataLoader docs | Build reusable Trainer class with validation loop, early stopping, LR scheduler, checkpoint save/load | Reusable Trainer class (PyTorch) |
| **ML-D12** | Deep Learning | CNNs: conv, pooling, receptive fields, ResNet50 architecture; torchvision; transfer learning vs full fine-tune | CS231n CNN YouTube; torchvision docs | Fine-tune ResNet-50 on 5-class image dataset; compare full fine-tune vs frozen feature extractor | 🟡 MINI PROJECT: ResNet-50 fine-tuned (>90% val accuracy) |
| **ML-D13** | Deep Learning | RNNs + LSTMs: sequence modelling, vanishing gradient, LSTM gates (forget/input/output/cell), GRU | Colah 'Understanding LSTMs' blog | Build LSTM for IMDB sentiment; compare with simple RNN on accuracy + gradient norms | LSTM vs RNN sentiment (gradient norms compared) |
| **ML-D14** | Deep Learning | Transformer from scratch: scaled dot-product attention, multi-head, positional encoding, encoder | Karpathy 'Let's build GPT' YouTube (2h) | Implement full scaled dot-product + multi-head attention in PyTorch from scratch; test on toy task | 🟡 MINI PROJECT: Transformer attention from scratch (working) |
| **ML-D15** | Deep Learning | Keras: Sequential + Functional API; callbacks; dropout; batch norm; data augmentation; compare with PyTorch | Keras guides; TF tutorial | Rebuild MNIST MLP + IMDB LSTM in Keras; add batch norm + dropout; document code differences vs PyTorch | Keras implementations (compared with PyTorch) |

### WEEK 4  ·  HuggingFace + LoRA   ▸  GOAL: Fine-tune LLMs and connect to main AI track

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **ML-D16** | HuggingFace NLP | HuggingFace ecosystem: Transformers, pipeline API, AutoModel, AutoTokenizer, datasets library, model hub; Hub CLI | HuggingFace course ch.1–2 (free) | Run 6 pipelines: text-class, NER, QA, summarisation, translation, fill-mask; inspect tokeniser output | HuggingFace pipeline showcase (6 tasks) |
| **ML-D17** | HuggingFace NLP | Fine-tune BERT: TrainingArguments, Trainer, compute_metrics, datasets.map tokenisation, gradient accumulation | HuggingFace course ch.3; Trainer docs | Fine-tune BERT-base on SST-2 (>93% accuracy); log to W&B; push to HuggingFace Hub | 🟡 MINI PROJECT: Fine-tuned BERT on SST-2 (HuggingFace Hub) |
| **ML-D18** | HuggingFace NLP | LoRA / QLoRA with Unsloth: PEFT library, LoRA rank/alpha, 4-bit quantisation, Unsloth speedup, memory efficiency | Unsloth docs; PEFT docs; Raschka LoRA blog | Fine-tune Llama-3.2-1B-Instruct with QLoRA on 500-row instruction dataset; eval vs base model on 50 prompts | QLoRA Llama fine-tune (instruction follower) |
| **ML-D19** | HuggingFace NLP | Model evaluation: BLEU, ROUGE, BERTScore, perplexity; human eval; HELM benchmark; calibration | sacrebleu docs; BERTScore paper; HELM benchmark | Evaluate fine-tuned Llama vs base on 50 test prompts with ROUGE + BERTScore; write analysis report | 🟣 CONNECTS TO AI TRACK: Fine-tune eval report (ROUGE + BERTScore) |
| **ML-D20** | MLOps | W&B: runs, sweeps (grid/random/Bayesian), artefacts, dashboards, system monitoring | W&B quickstart; W&B 'Effective MLOps' course (free) | Add W&B to PyTorch Trainer; run Bayesian sweep over LR × batch × dropout; compare 30 runs | W&B Bayesian sweep dashboard (30 runs) |
| **ML-D21** | MLOps | MLflow: experiment tracking, model registry, staging → production promotion, model cards, FastAPI + ONNX serving | MLflow docs; ONNX runtime docs | Log 3 model versions to MLflow; export best to ONNX; build FastAPI endpoint; benchmark 2x latency target | 🟡 MINI PROJECT: MLflow registry + ONNX inference API |
| **ML-D22** | MLOps | Docker for ML: Dockerfile, multi-stage builds, GPU support; HuggingFace Endpoints; SageMaker basics; load testing | Docker docs; HuggingFace Endpoints docs | Dockerise FastAPI inference server; deploy to HuggingFace Endpoints; load test 100 concurrent requests | 🟢 MILESTONE: Dockerised model on HF Endpoints (load tested) |

### WEEK 5  ·  RAG vs Fine-Tune + Capstone   ▸  GOAL: Connect ML depth to AI track + ship ML capstone

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **ML-D23** | ML × AI Integration | RAG vs fine-tuning decision framework: latency, cost, data freshness, domain specificity, update frequency | Anthropic 'RAG vs fine-tune' blog; Raschka comparison | Run head-to-head: RAG (Phase 1) vs fine-tuned Llama on 50 domain Q&As; document decision framework | 🟣 CONNECTS TO AI TRACK: RAG vs fine-tune benchmark + decision doc |
| **ML-D24** | ML × AI Integration | Drift monitoring: Evidently data drift; model performance degradation; embedding drift; retraining triggers; Prometheus metrics | Evidently AI docs; Prometheus quickstart | Simulate embedding drift on RAG system; detect with Evidently; set Prometheus alert; write runbook | 🟣 CONNECTS TO AI TRACK: Drift detection for RAG system + alert |
| **ML-D25** | ML Capstone | End-to-end ML project: choose real dataset; EDA → model selection → training → eval → ONNX → Docker → deploy → monitor | All prior resources | Pick Kaggle dataset; run full pipeline from raw data to deployed API; aim for top-20% leaderboard score | ML Capstone v1 (raw data → deployed API) |
| **ML-D26** | ML Capstone | Hyperparameter optimisation: Optuna study on capstone model; Bayesian search; pruning; best trial analysis | Optuna docs; W&B sweeps docs | Run 100-trial Optuna study on capstone model; visualise optimisation history; document best params | 🟡 MINI PROJECT: Optuna study (100 trials, best params documented) |
| **ML-D27** | ML Capstone | Model interpretability: SHAP values; feature importance; partial dependence plots; LIME for local explanations | SHAP docs; interpretML docs; LIME docs | Add SHAP to capstone model; generate global + local explanations; build interpretability report | SHAP interpretability report |
| **ML-D28** | ML Capstone | Model compression: quantisation (INT8), pruning (unstructured magnitude), knowledge distillation concepts | PyTorch quantisation docs; blog: 'Model compression for inference' | Quantise capstone model to INT8; compare accuracy vs speed trade-off; document inference speedup | 🟡 MINI PROJECT: Quantised model (speed vs accuracy trade-off) |
| **ML-D29** | ML Capstone | Deploy + monitor full ML pipeline: data ingestion → preprocessing → model inference → output logging → drift detection | — | Wire complete pipeline: live data source → model → output → Langfuse/MLflow logging → Evidently drift | ML pipeline (end-to-end, monitored) |
| **ML-D30** | ML Capstone | Write-up: document full ML depth journey; connect findings to Phase 4 (Days 100–120); update portfolio + resume | — | Write ML depth technical post; add ML projects to portfolio; tag all ML skills on resume; prep for Phase 4 | 🟢 MILESTONE: ML Depth capstone: deployed + documented + portfolio updated |

---

## Phase 4 — Deep ML (Extended)

**Days 100–120 · 3 Weeks**

> Full classical ML benchmarks → PyTorch Trainer → ResNet + BERT fine-tuning → QLoRA → MLflow model registry → Docker deploy → Evidently drift

### WEEK 15  ·  Python for ML + Classical ML   ▸  GOAL: Master NumPy, Pandas, scikit-learn; build end-to-end ML pipelines

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **100** | NumPy | Arrays; broadcasting; vectorised ops; linear algebra (matmul, dot, norm, svd); no-loop philosophy; memory layout | NumPy docs; 3Blue1Brown 'Essence of Linear Algebra' YouTube | Implement matrix multiply, cosine similarity, softmax from scratch; no Python loops; benchmark vs naive | NumPy fundamentals + benchmarks |
| **101** | Pandas | DataFrames; indexing (loc/iloc); groupby; merge/join; missing values; apply; method chaining; EDA workflow | Pandas docs; 'Effective Pandas' by Matt Harrison | Load Titanic + Airbnb datasets; full EDA: nulls, distributions, correlations, outliers; export clean CSV | 2 EDA notebooks (Titanic + Airbnb) |
| **102** | Matplotlib + Seaborn | Line, bar, scatter, histogram, heatmap, pair plot, box plot; subplots; styling; telling data stories visually | Matplotlib + Seaborn docs; Data Visualization with Python course | Build 10-chart EDA report on Airbnb data; write 1 insight per chart; export as PDF | 🟡 MINI PROJECT: 10-chart EDA visual report (PDF export) |
| **103** | ML Workflow | Train/test split; stratification; cross-validation (k-fold, stratified); data leakage; sklearn Pipeline; feature preprocessing | Scikit-learn user guide; Géron 'Hands-On ML' ch.2 | Build full sklearn Pipeline (StandardScaler + OneHotEncoder + imputer + model) on Titanic; 5-fold CV | sklearn Pipeline (Titanic, 5-fold CV) |
| **104** | Regression | Linear, ridge, lasso, ElasticNet; loss functions (MSE, MAE, Huber); regularisation; learning curves; bias-variance tradeoff | StatQuest regression series YouTube; sklearn linear_model docs | Train all 4 regression models on California Housing; plot learning curves; compare RMSE + R² | Regression benchmark (4 models, learning curves) |
| **105** | Classification | Logistic regression, SVM, KNN, decision trees; precision/recall/F1/ROC-AUC; confusion matrix; class imbalance (SMOTE) | StatQuest classification series; sklearn metrics docs | Train 4 classifiers on breast cancer + imbalanced fraud dataset; compare all metrics; handle imbalance | 🟡 MINI PROJECT: Classification benchmark + imbalance handling |
| **106** | Ensemble Methods + MLOps Basics | Random Forest, GradientBoosting, XGBoost, LightGBM; feature importance; hyperparameter tuning (Optuna); W&B logging | XGBoost docs; LightGBM docs; Optuna docs; W&B quickstart | Train XGBoost + LightGBM on tabular dataset; tune with Optuna (50 trials); log all runs to W&B | 🟢 MILESTONE: XGBoost vs LightGBM Optuna tuning (W&B dashboard) |

### WEEK 16  ·  Deep Learning: PyTorch + Keras   ▸  GOAL: Build neural networks from scratch up to fine-tuned transformers

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **107** | PyTorch Tensors + Autograd | Tensor creation/ops/GPU; autograd; computation graphs; .grad; gradient flow; in-place operations gotchas | PyTorch 60-min blitz; fast.ai lesson 1 | Recreate NumPy cosine similarity + softmax in PyTorch; move to GPU; visualise computation graph | PyTorch tensor exercises (GPU) |
| **108** | MLP from Scratch | nn.Module; forward pass; CrossEntropy + MSE loss; SGD + Adam optimisers; batch training loop; MNIST | PyTorch nn docs; Karpathy 'micrograd' YouTube | Build 3-layer MLP from scratch (no high-level APIs) on MNIST; achieve >98% accuracy; plot loss curves | MLP from scratch (MNIST, >98%) |
| **109** | Training Loop + Validation | DataLoader + Dataset; epochs; validation loop; early stopping; LR scheduler (CosineAnnealing); model checkpoint | PyTorch DataLoader docs | Build reusable Trainer class with validation loop, early stopping, LR scheduler, checkpoint save/load | 🟡 MINI PROJECT: Reusable Trainer class (PyTorch) |
| **110** | CNNs + Transfer Learning | Conv layers; pooling; receptive fields; ResNet50 architecture; torchvision; transfer learning; fine-tuning vs feature extraction | CS231n CNN lecture YouTube; torchvision docs | Fine-tune ResNet-50 on 5-class custom image dataset; compare full fine-tune vs frozen feature extractor | ResNet-50 fine-tuned classifier (>90% val) |
| **111** | RNNs + LSTMs | Sequence modelling; vanishing gradient; LSTM gates (forget/input/output/cell); GRU; when to use vs Transformer | Colah 'Understanding LSTMs' blog; PyTorch RNN docs | Build LSTM for IMDB sentiment; compare vs simple RNN on accuracy + training speed + gradient norms | LSTM vs RNN sentiment classifier |
| **112** | Transformer from Scratch | Scaled dot-product attention; multi-head attention; positional encoding; encoder; decoder; layer norm; FFN | Karpathy 'Let's build GPT' YouTube (2h); 'Attention Is All You Need' paper (read carefully) | Implement full scaled dot-product attention + multi-head attention in PyTorch; test on toy sequence task | 🟡 MINI PROJECT: Transformer attention from scratch (tested) |
| **113** | Keras + Regularisation | Sequential + Functional API; callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau); dropout; batch norm; data augmentation | Keras guides; TF docs | Rebuild MNIST MLP + IMDB LSTM in Keras; add batch norm + dropout; test 3 dropout rates; document | 🟢 MILESTONE: Keras implementations + regularisation experiment |

### WEEK 17  ·  HuggingFace, Fine-Tuning & MLOps   ▸  GOAL: Fine-tune LLMs + build production ML serving pipeline

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **114** | HuggingFace Ecosystem | Transformers library; pipeline API; AutoModel/AutoTokenizer; model hub; spaces; datasets library; Hub CLI | HuggingFace course ch.1–2 (free) | Run 6 pipelines: text-class, NER, QA, summarisation, translation, fill-mask; inspect tokeniser outputs | HuggingFace pipeline showcase (6 tasks) |
| **115** | Fine-tune BERT (Trainer API) | TrainingArguments; Trainer; compute_metrics; evaluate library; datasets.map for tokenisation; gradient accumulation | HuggingFace course ch.3; Trainer docs | Fine-tune BERT-base on SST-2 sentiment; log to W&B; achieve >93% accuracy; push to HuggingFace Hub | 🟡 MINI PROJECT: Fine-tuned BERT on SST-2 (HuggingFace Hub) |
| **116** | LoRA / QLoRA with Unsloth | PEFT library; LoRA rank/alpha; QLoRA 4-bit quantisation; gradient checkpointing; memory efficiency; Unsloth speedup | Unsloth docs; PEFT docs; Sebastian Raschka LoRA blog | Fine-tune Llama-3.2-1B-Instruct with QLoRA on 500-row custom instruction dataset; eval vs base model | QLoRA fine-tuned Llama (500 examples, eval) |
| **117** | RAG vs Fine-Tuning | When to use each: latency, cost, data freshness, domain specificity, update frequency; hybrid approaches | Anthropic 'RAG vs fine-tune' blog; Sebastian Raschka comparison | Run head-to-head: RAG (from Phase 1) vs fine-tuned Llama on same 50 domain Q&As; document decision framework | 🟣 CONNECTS TO AI TRACK: RAG vs fine-tune benchmark + decision doc |
| **118** | MLflow + Model Serving | MLflow experiment tracking; model registry; staging → production promotion; model card; FastAPI inference endpoint; ONNX export | MLflow docs; ONNX docs; FastAPI docs | Log 3 model versions to MLflow; promote best to prod; export to ONNX; benchmark ONNX vs PyTorch latency | MLflow registry + ONNX API (2x latency improvement) |
| **119** | Docker + Cloud Deploy | Dockerfile for ML; multi-stage builds; GPU support; push to Docker Hub; HuggingFace Inference Endpoints; AWS SageMaker basics | Docker docs; HuggingFace Endpoints docs; SageMaker deploy docs | Dockerise FastAPI inference server; push to HuggingFace Endpoints; load test with 100 concurrent requests | 🟡 MINI PROJECT: Dockerised model on HuggingFace Endpoints (load tested) |
| **120** | ML Monitoring + Drift | Evidently for data drift; model performance degradation; embedding drift; retraining triggers; Prometheus metrics for model | Evidently AI docs; Prometheus docs | Simulate data drift; detect with Evidently; set Prometheus metric for prediction confidence; write runbook | 🟢 MILESTONE: Drift detection + Prometheus metrics + runbook |

---

## Phase 5 — Pro Tier

**Days 121–150 · 5 Weeks**

> System design at scale → Claude Code mastery → Capstone project → Portfolio + resume + blog → Certification exam → Interview mastery

### WEEK 18  ·  System Design for AI at Scale   ▸  GOAL: Design ChatGPT-scale systems + ace system design interviews

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **121** | AI System Design Fundamentals | Load balancing for LLM requests; horizontal scaling; stateless vs stateful; caching layers (Redis, CDN, prompt cache); async vs sync | YouTube 'System Design Primer'; blog: 'Designing AI apps at scale' | Design architecture for 10K DAU AI app: draw components, identify bottlenecks, write capacity estimates | System design doc: 10K DAU AI app |
| **122** | Scale to 100K DAU | Queue systems for long-running jobs; fan-out for multi-agent; read replicas; DB connection pooling; rate limiting at scale | YouTube 'Designing ChatGPT-scale systems'; blog: 'Scaling LLM APIs' | Redesign same architecture for 100K DAU: calculate tokens/sec, DB queries/sec, cache hit rate targets | 🟡 MINI PROJECT: System design doc: 100K DAU (capacity estimated) |
| **123** | Streaming Architecture | WebSocket vs SSE vs long polling for streaming; backpressure; client reconnection; load balancer SSE config; Vercel streaming limits | Blog: 'Streaming LLM responses at scale'; Vercel streaming docs | Build streaming architecture diagram; implement SSE with reconnection; test load balancer SSE passthrough | Streaming architecture (SSE + reconnection tested) |
| **124** | Multi-Tenant AI SaaS | Tenant isolation (DB-per-tenant vs schema-per-tenant vs row-level security); API key management; usage metering; billing integration | Blog: 'Multi-tenancy for AI SaaS'; Stripe metered billing docs | Design multi-tenant architecture for AI SaaS; implement row-level security in Postgres; add metered billing | Multi-tenant architecture + RLS + metered billing |
| **125** | Distributed Caching | Redis Cluster; cache invalidation strategies; cache warming; TTL design; semantic cache for LLM responses; cache hit rate SLAs | Redis Cluster docs; Upstash Redis docs | Implement 3-layer cache (exact match → semantic → prompt cache); measure cache hit rate on 100 queries | 🟡 MINI PROJECT: 3-layer LLM cache (hit rate measured) |
| **126** | System Design Interview Prep | Common AI system design questions: RAG chatbot, document processing pipeline, multi-agent system, recommendation engine | System design interview prep blog; Pramp.com | Do 3 timed system design sessions (45 min each): (1) RAG chatbot, (2) document pipeline, (3) multi-agent research | 3 system design mock sessions + diagrams |
| **127** | Advanced Architecture Patterns | CQRS for AI apps; event sourcing for agent actions; saga pattern for multi-step agent workflows; outbox pattern | Blog: 'Advanced patterns for AI systems' | Design event-sourced agent audit trail; implement saga for multi-step refund workflow; write ADR (Architecture Decision Record) | 🟢 MILESTONE: ADR + event-sourced agent audit log |

### WEEK 19  ·  Claude Code + CI/CD Mastery   ▸  GOAL: Master Claude Code config + build full AI-powered CI/CD pipeline

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **128** | CLAUDE.md Hierarchy | User (~/.claude/CLAUDE.md) vs project (.claude/CLAUDE.md) vs directory-level; @import syntax; .claude/rules/ directory | Claude Code docs; exam guide domain 3.1 | Configure 3-level CLAUDE.md hierarchy on real project; use @import for standards files; verify with /memory | 3-level CLAUDE.md hierarchy (verified) |
| **129** | Path-Specific Rules | YAML frontmatter paths glob patterns; load-on-match behaviour; reducing irrelevant context + token usage; vs directory CLAUDE.md | Exam guide domain 3.3 | Create 4 .claude/rules/ files (React, API, tests, terraform) with glob patterns; verify activation on file edit | 🟡 MINI PROJECT: 4 path-scoped rule files (activation tested) |
| **130** | Custom Slash Commands + Skills | Project-scoped .claude/commands/; context: fork; allowed-tools restriction; argument-hint; skills vs CLAUDE.md | Exam guide domain 3.2 | Create 4 project slash commands (review, test, refactor, document); build 1 skill with context:fork | 4 slash commands + 1 forked skill |
| **131** | Plan Mode + Iterative Refinement | Plan mode for complex tasks; direct execution for simple; input/output examples; TDD iteration; interview pattern; sequential vs parallel issues | Exam guide domain 3.4–3.5 | Practice plan mode on: (1) microservice refactor, (2) library migration; document plan vs execute phases | Plan mode practice log (2 tasks documented) |
| **132** | Claude Code in CI | claude -p flag; --output-format json; --json-schema; session context isolation (generator ≠ reviewer); prior review in context | Exam guide domain 3.6 | Set up full CI pipeline: Claude Code reviews every PR; posts structured JSON findings as inline GitHub comments | 🟡 MINI PROJECT: Claude Code CI/CD pipeline (GitHub Actions, inline PR comments) |
| **133** | AI-Powered Dev Workflow | Claude Code for codebase exploration (Grep → Read → Edit pattern); Glob for test files; scratchpad files; fork_session for alternatives | Exam guide domain 2.5 + 1.7 | Explore unfamiliar codebase with Claude Code; use fork_session to compare 2 refactoring approaches; document findings | Codebase exploration report + fork_session comparison |
| **134** | Advanced Agentic Patterns | Adaptive task decomposition; iterative synthesis refinement; multi-pass review architecture; independent review instances | Exam guide domain 1.6 + 4.6 | Build adaptive code review agent: per-file → integration pass → independent review instance; compare to single-pass | 🟢 MILESTONE: Multi-instance code review agent (coverage measured) |

### WEEK 20  ·  Capstone Project Build   ▸  GOAL: Build and deploy production-grade capstone project

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **135** | Capstone Planning | Choose capstone + design full architecture; write detailed PRD; draw system architecture; identify all tech choices + tradeoffs | — | Choose from: AI coding assistant / enterprise RAG SaaS / AI customer support platform / data intelligence suite; write PRD + architecture doc | Capstone PRD + architecture doc (ADR) |
| **136** | Capstone Backend Core | FastAPI/Next.js API layer; DB schema + migrations; authentication; multi-agent orchestration; MCP integration | — | Scaffold capstone; set up auth + DB; build core API endpoints; wire main agent loop; unit tests | Capstone backend v1 (auth + DB + core API) |
| **137** | Capstone AI Features | Multi-agent pipeline; RAG system; tool integrations; eval pipeline; structured output; confidence scoring; escalation logic | — | Build all AI features: agents, RAG, tools, evals; run RAGAS on RAG component; test edge cases | 🟡 MINI PROJECT: Capstone AI features (RAGAS score measured) |
| **138** | Capstone Frontend | Next.js UI; streaming responses; real-time updates; data visualisation; mobile-responsive; accessibility (a11y) | — | Build complete UI: chat interface, document upload, analytics dashboard, settings; test on mobile | Capstone frontend (mobile-responsive, a11y checked) |
| **139** | Capstone Observability | Langfuse full instrumentation; PostHog user analytics; Sentry errors; cost dashboard; latency SLA tracking | — | Instrument every LLM call; track all user events; add Sentry; build cost + latency dashboard | Capstone observability (full stack) |
| **140** | Capstone Deploy + Load Test | Deploy to Vercel + Railway; domain setup; load test with k6 (100 concurrent users); fix performance issues; runbook | k6 load testing docs; Railway deploy docs | Deploy to production domain; run k6 load test (100 concurrent, 10 min); fix P0 issues from load test | 🟡 MINI PROJECT: Capstone: production deployed (load tested) |
| **141** | Capstone Polish + Case Study | UX polish pass; performance budget; write 2500-word technical case study with architecture diagrams + metrics; publish | dev.to; Hashnode; Medium | Final UX review; write + publish technical case study; submit to Hacker News Show HN; respond to comments | 🟢 MILESTONE: Project 8: Capstone (deployed, case study published) |

### WEEK 21  ·  Portfolio, Personal Brand & Job Prep   ▸  GOAL: Build professional portfolio + personal brand + job pipeline

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **142** | Resume + LinkedIn | AI engineer resume template; quantifying impact (users, latency, cost, accuracy); ATS keyword optimisation; LinkedIn profile overhaul | AI engineer resume guide; LinkedIn optimisation guide | Write full resume with metrics on every project; optimise LinkedIn (headline, about, skills, featured); get peer review | AI engineer resume (ATS-optimised) + LinkedIn profile |
| **143** | Portfolio Website | Project case studies; live demo links; GitHub cleanup; README best practices; architecture diagrams; metrics badges | Next.js portfolio templates; GitHub profile README guide | Build portfolio site with 5 project case studies; clean all GitHub repos; add README to every project | 🟡 MINI PROJECT: Portfolio site (live URL, 5 case studies) |
| **144** | Technical Blog + SEO | 2 in-depth technical blog posts; SEO for developer blogs; building authority; cross-posting strategy; newsletter basics | dev.to; Hashnode; Substack | Write + publish 2 posts: 'Building multi-agent RAG at scale' + 'MCP: the protocol that changed AI tooling'; share on LinkedIn | 2 technical blog posts (published + promoted) |
| **145** | Community + Network | GitHub contributions; open-source PRs; Discord communities (Latent Space, HuggingFace, LangChain); Twitter/X technical presence | Latent Space Discord; HuggingFace Discord; r/MachineLearning | Submit 1 PR to LangChain or LlamaIndex; join 3 Discord communities; post 5 technical tweets/threads | 1 merged open-source PR + community presence |
| **146** | Job Applications Round 1 | LinkedIn, Wellfound, agentic-engineering-jobs.com, aijobs.com, direct company career pages; personalised outreach | LinkedIn Jobs; Wellfound; aijobs.com; company career pages | Apply to 15 targeted roles; write personalised cover letter for each with project evidence; track in spreadsheet | 15 applications submitted (tracked) |
| **147** | Certification Prep: Final Sprint | Claude Certified Architect domains 1–5 full review; all 5 domain practice tests (50Q each); anti-patterns drill; gotchas checklist | Full Claude exam guide; practice test links | Do full 5-domain review; sit 2 timed full mock exams (50Q, 60 min); review every wrong answer | 🔵 CERT PREP: Cert prep: 2 full mock exams (target 750+) |
| **148** | Sit Certification Exam | Claude Certified Architect – Foundations exam; 50 multiple choice questions; 60 min; minimum passing score 720/1000 | Anthropic exam portal | Sit the real Claude Certified Architect exam; if failed: review wrong domains + resit within 14 days | 🔵 CERT PREP: Claude Certified Architect – Foundations (PASSED) |

### WEEK 22  ·  Interview Mastery   ▸  GOAL: Ace every round: screening → technical → system design → behavioral → offer

| Day | Module | Topics Covered | Resources | Tasks | Project / Assignment |
|-----|--------|----------------|-----------|-------|----------------------|
| **149** | Technical Interview Prep | LLM fundamentals Q&A (transformers, RAG, embeddings, agents); live coding with AI tools (2026 format); AI-aware round practice | Interview Query AI engineer Q&A bank; Careery.pro AI interview guide | Drill 50 LLM technical Q&As; do 2 timed live-coding sessions (Pramp) using Claude as co-pilot | 50 Q&A drilled; 2 live-coding sessions done |
| **150** | System Design + Behavioral + Offer | Design a multi-agent customer support system (full 45-min session); 5 STAR behavioral stories; salary negotiation; offer evaluation framework | STAR method guide; Levels.fyi salary data; Haseeb Qureshi salary negotiation blog | Do timed system design (45 min, recorded); finalise 5 STAR stories; practice salary negotiation script | 🟢 MILESTONE: Day 150: OFFER-READY Pro Max AI Engineer |

---

## All 8 Portfolio Projects

| # | Day | Project | What it demonstrates |
|---|-----|---------|----------------------|
| 1 | Day 28 | **Chat with PDF** | RAG (LangChain + ChromaDB + Claude), source citations, streaming, RAGAS eval pipeline |
| 2 | Day 35 | **Production RAG SaaS** | Auth (Clerk), Stripe billing, PostgreSQL, Langfuse observability, GitHub Actions CI/CD |
| 3 | Day 55 | **Multi-Agent Research System** | 4 subagents (search + analysis + synthesis + report), MCP, provenance tracking, deployed |
| 4 | Day 63 | **Agent + Custom MCP Server** | Claude Agent SDK, custom MCP server (3 tools), GitHub + Jira community MCPs, hooks |
| 5 | Day 71 | **Voice AI Assistant** | Whisper STT + Claude + OpenAI TTS, <500ms TTFR, 5 tools, WebRTC, deployed |
| 6 | Day 78 | **Data AI Platform** | NL→SQL + pandas agent + Recharts dashboard + knowledge graph, multi-DB, Langfuse |
| 7 | Day 99 | **Structured Extraction Pipeline** | 3 doc types (invoices/contracts/resumes), batch API, confidence routing, human review |
| 8 | Day 141 | **Capstone Project** | Full-stack AI SaaS with all patterns combined, load tested, case study published on dev.to |

---

## Skills × Job Demand (500+ live 2026 postings)

| Skill | Demand | Day Learned | Tools / Frameworks | Notes |
|-------|--------|-------------|-------------------|-------|
| Python (async, OOP, packaging, testing) | ★★★★★ | Day 1 | Python 3.12+, pytest, ruff | Foundation for everything — used every single day |
| LLM APIs (Claude, OpenAI, Gemini) | ★★★★★ | Day 2 | Anthropic SDK, OpenAI SDK, Google AI SDK | Most common requirement in all AI engineer job postings |
| Prompt Engineering (all techniques) | ★★★★★ | Days 3–14 | promptingguide.ai, Anthropic docs | Few-shot, CoT, explicit criteria, few-shot — all exam domain 4 |
| RAG (Retrieval-Augmented Generation) | ★★★★★ | Days 22–28 | LangChain, LlamaIndex, RAGAS | #1 skill in LinkedIn 2026 data — required in 90%+ of postings |
| Embeddings + Vector Databases | ★★★★★ | Days 15–21 | ChromaDB, Pinecone, pgvector, BGE | Core to every RAG and semantic search system |
| LangChain / LCEL | ★★★★★ | Days 23–24 | LangChain v0.9, LCEL chains | Dominant orchestration framework — know it cold |
| LangGraph (stateful agents) | ★★★★★ | Days 40–41 | LangGraph, LangGraph Academy | Replacing plain LangChain for agents — fast-growing requirement |
| Agentic loops + tool use (function calling) | ★★★★★ | Days 36–38 | Claude Agent SDK, OpenAI function calling | Core to every agent role — stop_reason, tool schemas |
| MCP (Model Context Protocol) | ★★★★★ | Days 57–63 | MCP Python SDK, FastMCP, .mcp.json | 97M monthly SDK downloads Feb 2026 — industry standard |
| Multi-agent systems | ★★★★☆ | Days 50–55 | Claude Agent SDK, CrewAI, AutoGen | Growing fast — required at senior level |
| Structured output (tool_use + JSON schemas) | ★★★★☆ | Days 94–99 | tool_use, Pydantic, JSON Schema | Exam domain 4 — every production system needs this |
| Observability / LLMOps | ★★★★☆ | Days 34 + 81 | Langfuse, Helicone, PostHog | All production roles require tracing + cost dashboards |
| Evaluation frameworks | ★★★★☆ | Day 26 + 81 | RAGAS, Braintrust, Promptfoo | Separates junior from senior — build eval pipelines |
| Next.js + Vercel AI SDK | ★★★★☆ | Days 6 + 22 | Next.js 15, Vercel AI SDK, shadcn/ui | Standard AI SaaS frontend stack |
| PostgreSQL + ORM | ★★★★☆ | Days 30–31 | Drizzle, Prisma, Neon, pgvector | Required for any production backend |
| Vision / Multimodal | ★★★☆☆ | Days 64–65 | Claude Vision, GPT-4o Vision | Growing — document AI and invoice processing roles |
| Voice AI (STT + TTS + Realtime) | ★★★☆☆ | Days 67–71 | Whisper, ElevenLabs, OpenAI Realtime | Voice AI market accelerating — niche but well-paid |
| CI/CD with AI (Claude Code in GitHub Actions) | ★★★★☆ | Days 35 + 132 | GitHub Actions, Claude Code -p flag | Production workflow requirement at mid+ level |
| Security (prompt injection, PII, OWASP) | ★★★★☆ | Days 86–92 | OWASP LLM Top 10, Presidio, Guardrails AI | Enterprise and fintech requirement — non-negotiable |
| System Design (AI scale) | ★★★★☆ | Days 121–127 | System design primer, YouTube | Required from mid-level up in 2026 interviews |
| PyTorch (deep learning) | ★★★☆☆ | ML-D9–D15 + D108–D113 | PyTorch 2.x, torchvision | Required for ML engineer roles — AI engineer bonus skill |
| scikit-learn (classical ML) | ★★★☆☆ | ML-D4–D8 + D103–D106 | sklearn, XGBoost, LightGBM | Tabular data / data science hybrid roles |
| HuggingFace fine-tuning (BERT, LoRA) | ★★★☆☆ | ML-D17–D19 + D115–D116 | HuggingFace Transformers, PEFT, Unsloth | Required for ML engineer — AI engineer differentiator |
| MLOps (MLflow, Docker, W&B, Evidently) | ★★★☆☆ | ML-D21–D22 + D118–D120 | MLflow, Docker, Evidently AI, W&B | MLOps engineer path — bonus for AI engineers |
| NL→SQL | ★★★☆☆ | Days 72–73 | vanna.ai, SQLCoder, LangChain SQL agent | Data AI / analytics AI roles |
| Message Batches API | ★★★☆☆ | Day 82 | Anthropic Batches API | High-volume extraction systems — 50% cost saving |
| Claude Code configuration | ★★★★☆ | Days 128–134 | CLAUDE.md, .claude/rules/, .claude/commands/ | Growing requirement — developer productivity roles |
| Claude Certified Architect | ★★★★☆ | Days 147–148 | Anthropic exam guide, 5 domains | Strong differentiator — still rare in market |
| Cloud (AWS / GCP / Azure basics) | ★★★★☆ | ML-D22 + D119 | AWS Lambda, S3, SageMaker, Vercel, Railway | Deployment environment for all production systems |
| Redis (caching + queues) | ★★★☆☆ | Days 83 + 125 | Upstash Redis, BullMQ, Redis Cluster | Required for any production AI system at scale |

---

## Interview Prep Summary (Days 149–150)

### What to expect (2026 format)

- **Recruiter screen (30 min)**: Role fit, salary, timeline. Light LLM questions about your projects.
- **Technical phone screen (45–60 min)**: LLM fundamentals (transformers, RAG, embeddings, agents). Live coding with AI tools allowed.
- **Deep technical rounds (60 min × 1–2)**: RAG architecture deep dive, prompt engineering scenarios, evaluation strategies, multi-agent design.
- **System design (60 min)**: Design an AI product: RAG chatbot / document pipeline / multi-agent support system.
- **Behavioral (45 min)**: 5 STAR stories: (1) shipped AI feature, (2) handled hallucination in prod, (3) improved latency, (4) cross-functional collab, (5) learning from failure.

### Key 2026 interview insight

> AI engineer interviews are now **60–80% GenAI-focused** — RAG, agents, prompt engineering, system design for LLM apps. Classical ML (CNNs, gradient descent) accounts for only 20–30% of questions. The 2026 format allows AI tools in coding rounds — interviewers assess *how* you use AI, not whether you can code without it.

### Salary negotiation anchors (April 2026)

| Level | Base Salary | Total Comp |
|-------|-------------|-----------|
| Junior AI Engineer (0–2 yrs) | $95K–$130K | $110K–$150K |
| Mid AI Engineer (2–4 yrs) | $130K–$165K | $150K–$200K |
| Senior AI Engineer (4+ yrs) | $165K–$200K+ | $200K–$280K+ |
| ML Engineer (production) | $150K–$200K+ | $175K–$250K+ |
| Staff / Principal | $200K–$300K+ | $300K–$500K+ |

> Source: LinkedIn Salary, Glassdoor, Built In, Levels.fyi (April 2026).  
> PwC 2025 Global AI Jobs Barometer: **56% wage premium** for roles requiring AI skills.

---

## After Day 150 — What's Next

- **Keep applying daily** — hiring pipeline takes 4–8 weeks to convert to offer. Don't stop building while interviewing.
- **Contribute to open source** — target 1 merged PR in LangChain, LlamaIndex, or HuggingFace. It gets you recruiter inbound.
- **Write 1 technical post/week** — compounds fast. 12 posts = recognised authority in your niche.
- **Join communities** — Latent Space Discord, HuggingFace Discord, r/MachineLearning, r/LocalLLaMA.
- **Consider specialisation** — Computer Vision (YOLO + SAM + diffusion) / NLP research / MLOps / AI safety / voice AI.
- **Re-sit certification if needed** — you have the knowledge. It's just exam technique. Review wrong domains and resit within 14 days.
- **Target role titles**: `AI Engineer` · `LLM Engineer` · `ML Engineer` · `Applied AI Engineer` · `Forward Deployed Engineer` · `AI Solutions Architect`

---

*Roadmap version 1.0 · Built April 2026 · Sourced from 500+ live job postings + Claude Certified Architect exam guide + 2026 ML engineering hiring data*
