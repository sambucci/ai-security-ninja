```text
 █████╗ ██╗    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
██╔══██╗██║    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
███████║██║    ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝
██╔══██║██║    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝
██║  ██║██║    ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║
╚═╝  ╚═╝╚═╝    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝

     ▄██████▄                                                        █▄
 ▄▄ ███▀██▀███      ███╗   ██╗██╗███╗   ██╗     ██╗ █████╗         ▄████
  ▀ ▀████████▀      ████╗  ██║██║████╗  ██║     ██║██╔══██╗     ▄███▀▀▀██▄
     ▄██████▄       ██╔██╗ ██║██║██╔██╗ ██║     ██║███████║    ▀▀███   ████▀
  ▄██▀▀██████▀▀▀    ██║╚██╗██║██║██║╚██╗██║██   ██║██╔══██║       ▀█████▀▀
 █▀    ██████       ██║ ╚████║██║██║ ╚████║╚█████╔╝██║  ██║        ▀██▀
      ▄██▀▀██▄      ╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚════╝ ╚═╝  ╚═╝          ▀
    ▄██▀    ▀██▄

ENTRIES  212              SECTIONS  7               LAST REVIEWED  2026-10-20
```

A curated, living map of AI security: frameworks, foundational papers, code, guides, courses and communities. This repository mirrors the curated sections of [aisecurity.ninja](https://aisecurity.ninja) and rebuilds itself from the site's data once a month.

I built the map as my own reference and made it public because it seemed useful. The site carries the whole thing, including a [papers feed](https://aisecurity.ninja/papers) that updates itself every day from arXiv; that stream is deliberately not mirrored here. What this repository holds is the slow-moving, human-reviewed layer, the part that benefits from being forkable, searchable and citable.

**Inclusion is not endorsement.** I am not affiliated with, endorsed by or connected to any of the projects, organisations, courses or communities listed. Entries are amended or removed on evidence; see [how to suggest a change](#about-this-repository) at the end.

212 entries in 7 sections. Sections last reviewed on the site: 2026-10-20.

## Contents

- [Frameworks and Governance](#frameworks-and-governance) (53)
- [Foundational papers](#foundational-papers) (11)
- [Code and PoCs](#code-and-pocs) (80)
- [Guides and Tutorials](#guides-and-tutorials) (25)
- [Courses](#courses) (24)
- [Communities](#communities) (7)
- [Links](#links) (12)

## Frameworks and Governance

A collection of guides and frameworks (not laws) from government-affiliated or otherwise noteworthy institutions.

- **[A Sensible Regulatory Framework for AI Security](https://www.mitre.org/news-insights/publication/sensible-regulatory-framework-ai-security)** (MITRE Corporation, USA)

  A comprehensive approach to regulating AI to ensure security and mitigate risks. It categorizes AI into three domains: as a subsystem, as human augmentation, and with autonomous agency. Each category presents unique risks that require tailored regulatory measures. Recommendations include improving AI assurance, developing robust audit mechanisms, and focusing on the interplay between AI components in complex systems. The paper emphasizes the need for continuous regulatory analysis and the creation of frameworks that align AI development with public safety, while avoiding regulatory overreach that could stifle innovation.

- **[Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2e2025)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf)** (National Institute of Standards and Technology (NIST), USA)

  This document presents a detailed taxonomy and standardized terminology for adversarial machine learning (AML), focusing on attacks and mitigation strategies for AI systems. It classifies attacks into categories based on learning methods, attacker goals, and stages of the machine learning lifecycle. The report emphasizes the importance of understanding adversarial risks across predictive and generative AI systems and outlines corresponding mitigation techniques. By providing a common language, the framework aids in securing AI systems against threats like evasion, data poisoning, and privacy violations. This entry points to the 2025 edition, NIST AI 100-2e2025, published in March 2025, which extends the 2023 taxonomy to generative AI, including attacks on large language models, retrieval-augmented generation and agents.

- **[Agent Control Standard (ACS)](https://genai.owasp.org/resource/agent-control-standard-acs/)** (OWASP, International)

  An open standard for runtime control of AI agents: it defines the hooks an agent platform exposes so that separate tooling can inspect an agent's intended actions and permit, deny or modify them before they execute, with policy enforcement and an audit trail. Where the agentic threat guides describe what to defend against, this specifies where the enforcement point sits. The specification, at version 0.1.0, is written as JSON Schemas with normative prose and is developed in the open on GitHub, code under Apache 2.0 and documentation under CC BY-SA 4.0. It joined the OWASP GenAI Security Project on 1 September 2026.

- **[Agent Name Service (ANS) for Secure AI Agent Discovery v1.0](https://genai.owasp.org/resource/agent-name-service-ans-for-secure-al-agent-discovery-v1-0/)** (OWASP, International)

  A proposed scheme for agents to discover and authenticate each other, addressing the question of how one agent knows which other agent it is talking to. Early work, published as version 1.0.

- **[Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)** (OWASP, International)

  Threat reference for agentic systems, working through what changes once a model can plan, remember and call tools: goal manipulation, misuse of delegated authority, and trust between agents. Paired mitigations for each.

- **[AI Assurance: A Repeatable Process for Assuring AI-Enabled Systems](https://www.mitre.org/news-insights/publication/ai-assurance-repeatable-process-assuring-ai-enabled-systems)** (MITRE Corporation, USA)

  The document presents a comprehensive framework for AI assurance, focusing on managing risks across the lifecycle of AI-enabled systems. The framework integrates risk management practices and emphasizes a repeatable engineering process to ensure AI systems operate effectively while managing safety, security, privacy, and other key trust factors. Through a detailed assurance plan, the process addresses system characterization, risk discovery, and evaluation, making it adaptable to various sectors. The approach leverages real-world pilot studies to highlight its applicability, and promotes sector-specific solutions for domain-specific outcomes.

- **[AI Controls Matrix](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix)** (Cloud Security Alliance (CSA), International)

  A control framework for AI systems in the same shape as the Cloud Controls Matrix: a list of controls with implementation guidance and mappings to other standards, meant for assessing an AI deployment rather than reasoning about it.

- **[AI Cyber Security Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice)** (Department for Science, Innovation and Technology (DSIT), UK)

  A voluntary code published on 31 January 2025 setting out baseline cyber security principles for the organisations that develop, deploy and operate AI systems. It runs across the lifecycle, from secure design and development to deployment, maintenance and end of life, and ships with an implementation guide. The department submitted it to ETSI, where it forms the basis of the technical specification TS 104 223 and the accompanying implementation guide TR 104 128.

- **[AI Data Security: Best Practices for Securing Data Used to Train and Operate AI Systems](https://www.cisa.gov/news-events/alerts/2025/05/22/new-best-practices-guide-securing-ai-data-released)** (Cybersecurity and Infrastructure Security Agency (CISA), National Security Agency (NSA) and Federal Bureau of Investigation (FBI), USA)

  A joint cybersecurity information sheet released on 22 May 2025 by CISA, the National Security Agency, the FBI and partner agencies in Australia, New Zealand and the United Kingdom. It sets out the risks that arise from data security and integrity problems across the AI lifecycle, from development and testing through deployment and operation, and the practices that address them: data protection measures, risk management, monitoring, threat detection and network defence. This CISA alert page links to the full PDF.

- **[AI Incident Response Framework](https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/AI-Incident-Response-1.pdf)** (Coalition for Secure AI (CoSAI), International)

  Incident response adapted to AI systems, from the Coalition for Secure AI. It sorts AI incidents into data, model, deployment, infrastructure and user-interaction incidents, then walks the familiar preparation, detection, containment and recovery, and post-incident phases with the AI-specific work added to each, including the split of responsibilities between a model provider and its consumer. Playbooks and a RACI for the roles involved are included. Version 1.0, dated 27 October 2025, from CoSAI's workstream on preparing defenders.

- **[AI Model Risk Management Framework](https://cloudsecurityalliance.org/artifacts/ai-model-risk-management-framework)** (Cloud Security Alliance (CSA), International)

  Framework for managing risk at the model level, covering how a model is selected, validated, monitored and retired. Aimed at organisations answerable for a model's behaviour in production rather than at the people training it.

- **[AI Risk Assessment for ML Engineers](https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment)** (Microsoft, USA)

  This document provides a framework for organizations to assess the security posture of their AI systems, aligned with existing information security efforts and business objectives. It covers various areas related to AI systems, including machine learning security policies, data collection, data processing, model training, model deployment, system monitoring, incident management, and business continuity planning. The document aims to provide a comprehensive perspective on AI system security, outline threats to critical AI assets, and enable organizations to conduct AI security risk assessments.

- **[AI Safety Governance Framework 2.0](https://www.cac.gov.cn/rootimages/uploadimg/1759653474200838/1759653474200838.pdf)** (National Technical Committee 260 on Cybersecurity of Standardization Administration of China (SAC/TC260; 全国网络安全标准化技术委员会) and National Computer Network Emergency Response Technical Team/Coordination Center of China (CNCERT/CC; 国家计算机网络应急技术处理协调中心), China)

  China's national framework for AI safety governance, covering risk management across the AI lifecycle. It sorts risks into three classes: risks inherent in the technology, such as weaknesses in models, algorithms and data, risks arising when the technology is applied, including its abuse for cyberattacks and the output of harmful content, and derivative risks that wide adoption creates for society. Each class gets technical countermeasures, followed by fourteen broader governance measures and security guidelines for those who develop, deploy, operate and use AI applications. Version 2.0 was issued jointly by TC260 and CNCERT/CC in September 2025 and released on 15 September 2025, replacing the September 2024 version 1.0. The PDF carries the Chinese text followed by an English translation.

- **[AI Security Concerns in a Nutshell](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/Practical_Al-Security_Guide_2023.pdf)** (Federal Office for Information Security, Germany)

  This guide introduces key security concerns associated with AI systems, particularly focusing on attacks and defenses relevant to machine learning models. It outlines categories such as evasion attacks, information extraction, and backdoor attacks, emphasizing the importance of secure AI system design. With AI being used in critical sectors like healthcare and autonomous driving, the guide stresses the importance of defensive measures against malicious manipulation, especially when using pre-trained models or public datasets. The document aims to provide initial guidance for developers on securing AI systems without claiming to be exhaustive.

- **[AI Security Verification Standard (AISVS)](https://github.com/OWASP/AISVS)** (OWASP, International)

  A verification standard for AI applications, structured as testable requirements at several levels of rigour, in the same shape as the ASVS for web applications. Intended for stating what was verified rather than claiming a system is secure. CC-BY-SA-4.0.

- **[AI Shared Responsibility Framework](https://www.coalitionforsecureai.org/wp-content/uploads/2026/05/CoSAI-Shared-Responsibility-Framework.pdf)** (Coalition for Secure AI (CoSAI), International)

  Sets out who is responsible for which security control when an AI system is assembled from several suppliers, in the manner of the cloud shared responsibility model. It names eight roles, from agentic platform, model and model-serving providers through platform provider, application developer and data provider to users and governance, and maps responsibilities across five layers and three operating models (AI software, platform and infrastructure as a service). Useful for vendor contracts and for finding the controls nobody has picked up. Version 1.0, dated 26 May 2026, from the Coalition for Secure AI.

- **[Artificial Intelligence Risk Management Framework (NIST AI 100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)** (National Institute of Standards and Technology (NIST), USA)

  NIST's voluntary framework for managing risk across the design, development, use and evaluation of AI systems, published on 26 January 2023. It is organised around four functions: govern, map, measure and manage. This is the base document that the generative AI profile (NIST AI 600-1) and other sector profiles build on, and NIST publishes a companion playbook, crosswalks to other standards, and a roadmap alongside it.

- **[Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)** (National Institute of Standards and Technology (NIST), USA)

  This document is a cross-sectoral profile of the AI Risk Management Framework (AI RMF 1.0), specifically tailored for generative artificial intelligence (GAI). It builds upon the guidelines from the 2023 Executive Order on Safe, Secure, and Trustworthy AI, helping organizations manage the unique risks of GAI across its lifecycle. The framework offers insights on governance, testing, and risk management for GAI, focusing on emerging risks like confabulation, harmful bias, and privacy issues while providing strategies for organizations to mitigate these risks. A companion https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/Playbook also has been published by NIST along with an https://www.nist.gov/itl/ai-risk-management-framework/roadmap-nist-artificial-intelligence-risk-management-framework-ai, https://www.nist.gov/itl/ai-risk-management-framework/crosswalks-nist-artificial-intelligence-risk-management-framework, and various https://www.nist.gov/itl/ai-risk-management-framework/perspectives-about-nist-artificial-intelligence-risk-management. In addition, NIST is making available a https://www.nist.gov/video/introduction-nist-ai-risk-management-framework-ai-rmf-10-explainer-video about the AI RMF.

- **[Careful Adoption of Agentic AI Services](https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services)** (Cybersecurity and Infrastructure Security Agency (CISA) and Australian Signals Directorate's Australian Cyber Security Centre (ASD's ACSC), USA)

  Joint guidance published on 1 May 2026 by CISA with the Australian Signals Directorate's Australian Cyber Security Centre and other international and US partners. It sets out the security challenges and risks that come with agentic AI systems and the steps for designing, deploying and operating them safely, with the stated aim of helping organizations align AI risk management with the cybersecurity frameworks they already run and strengthen oversight as agentic adoption grows.

- **[CSA’s Guidelines on Securing AI Systems](https://www.csa.gov.sg/Tips-Resource/publications/2024/guidelines-on-securing-ai)** (Cyber Security Agency (CSA), Singapore)

  The "Guidelines on Securing AI Systems," developed by the Cyber Security Agency of Singapore in October 2024, provides a comprehensive framework for securing AI systems across their lifecycle. These guidelines emphasize understanding AI-specific threats, conducting risk assessments, and applying security principles throughout AI development, deployment, and maintenance. Although non-mandatory, they aim to assist system owners in mitigating risks and implementing secure AI practices, alongside traditional cybersecurity measures. The document also serves as a foundation for further collaboration with the AI and cybersecurity community. The CSA also released a “Companion Guide on Securing AI Systems” to support AI system owners in securing their AI adoption across the systems’ lifecycle available at: https://www.csa.gov.sg/Tips-Resource/publications/2024/guidelines-on-securing-ai

- **[Cybersecurity Framework Profile for Artificial Intelligence (NIST IR 8596)](https://csrc.nist.gov/pubs/ir/8596/iprd)** (National Institute of Standards and Technology (NIST), USA)

  Applies the NIST Cybersecurity Framework 2.0 to AI, organised around three focus areas: securing AI systems, using AI for cyber defence, and building resilience against AI-enabled attacks. It complements the AI Risk Management Framework rather than replacing it. Published as an initial preliminary draft on 16 December 2025; the comment period closed on 30 January 2026 and NIST plans an initial public draft during 2026.

- **[ENISA’s View on Cybersecurity in the Frontier AI Era](https://www.enisa.europa.eu/publications/enisas-view-on-cybersecurity-in-the-frontier-ai-era)** (European Union Agency for Cybersecurity (ENISA), EU)

  A position note published on 7 July 2026 on what frontier AI models change for cybersecurity in the EU. In the agency's own words it gives national competent authorities in member states, EU policymakers, defenders and service providers "an initial set of recommendations to support them in their respective roles towards developing the necessary operational capabilities to face machine-speed threats". It is a short strategic document, so expect direction and priorities here and controls in ENISA's framework publications.

- **[Establish Risks and Controls for the AI Supply Chain](https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/risks-and-controls-for-the-ai-supply-chain-v1.pdf)** (Coalition for Secure AI (CoSAI), International)

  A map of the AI supply chain and what can go wrong along it, from the Coalition for Secure AI. It separates model generation (training data, training, infrastructure) from model integration and consumption (data, model, application, infrastructure), lists the threats at each stage, such as data poisoning and weaknesses in model training, and pairs them with existing mitigations and the documentation a consumer should expect from a supplier. It closes with separate takeaways for executives, security practitioners and ML engineers. Version 1.0, dated 12 June 2025.

- **[GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/)** (OWASP, International)

  Published by the OWASP Gen AI Security Project on 22 January 2025, this guide describes what red teaming a generative AI system involves in practice. It covers model evaluation, implementation testing, infrastructure assessment and runtime behaviour analysis, and treats red teaming as a programme rather than a one-off exercise. The PDF downloads without registration.

- **[GenAI Security Project Threat Defense COMPASS 1.0](https://genai.owasp.org/resource/owasp-genai-security-project-threat-defense-compass-1-0/)** (OWASP, International)

  A method for connecting observed threats to the defences that address them, so a programme can be described in terms of coverage rather than a list of tools. Released as version 1.0.

- **[Guidelines for secure AI system development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development)** (National Cyber Security Centre (NCSC), UK)

  Guidelines covering the whole lifecycle, from secure design through development, deployment and operation. Published by the UK NCSC with CISA and co-sealed by agencies from a further sixteen countries, which makes it one of the few pieces of AI security guidance with broad international sign-off.

- **[Inspect Framework](https://inspect.ai-safety-institute.org.uk/)** (UK AI Safety Institute, UK)

  Inspect,a framework for large language model evaluations created by the UK AI Safety Institute, provides many built-in components, including facilities for prompt engineering, tool usage, multi-turn dialog, and model graded evaluations. Extensions to Inspect (e.g. to support new elicitation and scoring techniques) can be provided by other Python packages.

- **[ISO/IEC 22989:2022 Information technology,  Artificial intelligence , Artificial intelligence concepts and terminology](https://www.iso.org/standard/74296.html)** (International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC), International)

  The vocabulary standard the other ISO AI documents build on, fixing what terms such as machine learning, model and AI system mean. Useful mainly when a contract or policy needs words that are defined somewhere other than a vendor's marketing. Published 2022.

- **[ISO/IEC 23894:2023 Information technology,  Artificial intelligence , Guidance on risk management](https://www.iso.org/standard/77304.html)** (International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC), International)

  Guidance on applying risk management to AI, mapping the general ISO 31000 approach onto AI-specific sources of risk. Guidance rather than requirements, so it is read alongside 42001 rather than certified against. Published 2023.

- **[ISO/IEC 42001:2023 Information technology,  Artificial intelligence , Management system](https://www.iso.org/standard/81230.html)** (International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC), International)

  The certifiable management-system standard for AI, in the same family as ISO/IEC 27001 for information security. It specifies how an organisation establishes, runs and improves an AI management system rather than how any model is built, which makes it the document auditors and procurement ask for. Published 2023.

- **[ISO/IEC CD 27090](https://www.iso.org/standard/56581.html)** (ISO, International)

  This document (still in draft status) offers guidance to organizations on managing security threats and failures in AI systems. It provides insights into the consequences of such threats throughout the AI lifecycle and offers strategies for detection and mitigation. The guidance is applicable to organizations of all sizes and sectors, including public and private companies, government agencies, and non-profits, that are involved in the development or use of AI systems.

- **[LLM and Gen AI Data Security Best Practices](https://genai.owasp.org/resource/llm-and-gen-ai-data-security-best-practices/)** (OWASP, International)

  Practices for the data side of generative AI: what goes into training and retrieval, how it is classified and retained, and where it can leak back out through a model. The half of AI security that is a data-governance problem.

- **[LLM Applications Cybersecurity and Governance Checklist](https://genai.owasp.org/resource/llm-applications-cybersecurity-and-governance-checklist-english/)** (OWASP, International)

  A checklist for organisations adopting LLM applications, covering governance, legal and regulatory questions as well as technical controls. Written for the people who have to sign off on a deployment.

- **[LLM Threats Taxonomy](https://cloudsecurityalliance.org/artifacts/csa-large-language-model-llm-threats-taxonomy)** (Cloud Security Alliance (CSA), International)

  A taxonomy of threats specific to large language models, giving named categories to sort findings into. Sits alongside the NIST adversarial-ML taxonomy already listed here, from an industry rather than a standards-body perspective.

- **[Managing Misuse Risk for Dual-Use Foundation Models (NIST AI 800-1 second public draft)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf)** (National Institute of Standards and Technology (NIST), USA)

  Guidelines for improving the safety and security of dual-use foundation models, focusing on mitigating the risks of deliberate misuse. It addresses the evolving threats posed by foundation models, such as their potential to aid in the development of harmful technologies, cyberattacks, and other dangerous outputs. The guidelines emphasize managing misuse risks across the AI lifecycle, offering best practices for developers and organizations involved in foundation model development. The recommendations build upon the NIST AI Risk Management Framework, focusing on both technical and social factors influencing misuse. This entry points to the second public draft, released on 15 January 2025, which NIST describes as an expanded version of the July 2024 initial draft, revised after public comment. No final version had been published as of October 2026.

- **[MITRE Adversarial Threat Landscape for AI Systems (ATLAS)](https://atlas.mitre.org/)** (MITRE Corporation, USA)

  MITRE's ATLAS is a knowledge base of adversarial tactics and techniques targeting AI systems, derived from real-world attacks and demonstrations by red teams. With the increasing adoption of AI, ATLAS highlights the unique risks, expanding attack surfaces, and vulnerabilities that traditional cyber defenses may not cover. Modeled after MITRE's ATT&CK framework, it provides valuable insights for security analysts, AI developers, and others involved in AI security, enabling effective threat assessments and red teaming. ATLAS also facilitates global collaboration through secure incident reporting and open-source tools to enhance AI threat mitigation strategies.

- **[Model Context Protocol (MCP) Security](https://www.coalitionforsecureai.org/wp-content/uploads/2026/09/model-context-protocol-security-v2.0.pdf)** (Coalition for Secure AI (CoSAI), International)

  A threat model and control set for systems built on the Model Context Protocol, from the Coalition for Secure AI's workstream on secure design patterns for agentic systems. It separates threats specific to MCP from general threats that MCP changes, then sets out controls covering agent identity, delegation and access control, input sanitisation, sandboxing, cryptographic verification of resources, transport security, human approval and logging. It also defines security assurance profiles, stating which controls each assurance level requires and mapping them to common deployment patterns. Version 2.0, dated 12 August 2026 and still marked as a draft.

- **[Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)** (European Union Agency for Cybersecurity (ENISA), EU)

  A scalable, three-layer framework for cybersecurity practices in AI systems, addressing both general ICT security and AI-specific risks. Layer I covers foundational cybersecurity practices for ICT infrastructures hosting AI systems. Layer II introduces AI-specific security controls, addressing dynamic risks throughout AI’s lifecycle. Layer III provides sector-specific practices for high-risk AI applications, such as in health and energy. The framework integrates existing standards, legislation, and cybersecurity measures, aiming to build trust and enhance the security and resilience of AI systems across various sectors.

- **[OCCULT: Evaluating Large Language Models for Offensive Cyber Operation Capabilities](https://arxiv.org/abs/2502.15797)** (MITRE Corporation, USA)

  OCCULT is a framework designed to quantify the risks of LLMs when used in offensive cyber operations. Instead of red-teaming the model to see how it might fail, OCCULT is about assessing how an LLM itself could be weaponized by attackers or used as a “cyber agent.”

- **[OWASP AI Exchange](https://owaspai.org/)** (OWASP, International)

  An open reference covering AI security threats, the controls that address them and the practices around both, written by a group of more than 170 contributors and published as a browsable site and a single PDF. It runs to over 300 pages and feeds into the standards work behind the EU AI Act and ISO, with mappings to other frameworks. Free, no registration, and the source repository was last updated on 31 August 2026.

- **[OWASP AI Testing Guide](https://owasp.org/projects/ai-testing-guide)** (OWASP, International)

  A testing methodology for AI and LLM systems, with repeatable test cases spanning the application, model, infrastructure and data layers. It covers adversarial manipulation, information leakage, data poisoning, bias, hallucination, unsafe autonomy and model degradation. Version 1 was published on 26 November 2025 and is available as a PDF and as browsable documentation. Led by Matteo Meucci and Marco Morana.

- **[OWASP LLM Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)** (OWASP, International)

  The OWASP Gen AI Security Project's list of the ten most critical security risks in applications built on large language models, with mitigations for each and mappings to NIST, MITRE ATLAS and the CSA AI Controls Matrix. The 2026 edition was published on 4 August 2026 and is the current one: prompt injection and sensitive information disclosure hold the first two places, excessive agency moves up to third, and hidden context exposure replaces system prompt leakage. The PDF downloads without registration. The older owasp.org project page is now kept as a historical archive and states that "active development has moved to the OWASP GenAI Security Project repository".

- **[OWASP Machine Learning Security Top 10](https://owasp.org/projects/machine-learning-security-top-ten)** (OWASP, International)

  The Top 10 for machine learning systems generally, covering input manipulation, data poisoning, model inversion, membership inference and supply-chain attacks. Distinct from the LLM Top 10 also listed here: this one is about ML systems rather than language-model applications.

- **[OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)** (OWASP, International)

  A companion list to the LLM Top 10, covering the risks that appear once a model plans, holds memory, calls tools and acts with delegated authority. The ten categories run from agent goal hijack and tool misuse through identity and privilege abuse, memory and context poisoning, insecure inter-agent communication and cascading agent failures, each mapped to reported incidents and to defences across the development lifecycle. The 2026 edition was published on 9 December 2025 and downloads without registration.

- **[Project CodeGuard](https://github.com/cosai-oasis/project-codeguard)** (Coalition for Secure AI (CoSAI), International)

  A model-agnostic set of security rules and skills for AI coding agents, from the Coalition for Secure AI, an OASIS open project. It puts secure-by-default practice in a form an agent consumes directly, so the guidance travels with the tooling instead of sitting in a document beside it.

- **[Red Teaming Methodology Guide for AI Safety](https://aisi.go.jp/output/output_information/250331_1/)** (Japan AI Safety Institute, Japan)

  The “Guide to Red Teaming Methodology on AI Safety” is intended to help developers and providers of AI systems to evaluate the basic considerations and implementation points of red teaming methodologies for AI systems from the viewpoint of attackers (those who intend to abuse or destroy AI systems). This guide was prepared based on domestic and international studies and precedents, taking international alignment into account. It summarizes the issues considered important when conducting red teaming.

- **[Risk Management Profile for Artificial Intelligence and Human Rights](https://2021-2025.state.gov/risk-management-profile-for-ai-and-human-rights/)** (Department of State, USA)

  This guide provides a framework for integrating human rights into the design, development, and governance of AI systems. It emphasizes the potential benefits of AI, while acknowledging risks such as bias and misuse for surveillance. The guide builds on the NIST AI Risk Management Framework, outlining how organizations can use it to respect international human rights throughout the AI lifecycle. It also recommends practices for risk assessment and mitigation, helping stakeholders across sectors incorporate human rights into their AI processes. The document now sits on the State Department's 2021-2025 archive site; the address on the main state.gov site returns 404.

- **[Roles and Responsibilities Framework for Artificial Intelligence in Critical Infrastructure](https://www.dhs.gov/publication/roles-and-responsibilities-framework-artificial-intelligence-critical-infrastructure)** (Department of Homeland Security, USA)

  The framework outlines the responsibilities for ensuring the safe and secure development of AI in critical U.S. infrastructure. It provides recommendations for five key roles: cloud infrastructure providers, AI developers, critical infrastructure operators, civil society, and the public sector. Addressing risks like cyber threats and operational failures, it advocates for voluntary responsibilities, transparency, and collaboration to enhance AI safety and security while safeguarding civil rights and liberties.

- **[Secure AI Framework (SAIF)](https://saif.google/)** (Google, USA)

  Google's public framework for AI security, written as a practitioner's guide. The site carries an interactive map of AI development seen through a security lens, a risk framework covering 15 risks inherent to AI development together with the controls that address them, and a self-assessment questionnaire that returns a list of relevant controls. SAIF 2.0 extends the material to agent security.

- **[Secure Software Development Practices for Generative AI and Dual-Use Foundation Models (NIST SP 800-218A)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)** (National Institute of Standards and Technology (NIST), USA)

  This document augments the https://csrc.nist.gov/projects/ssdf by providing specific practices and recommendations for developing secure generative AI and dual-use foundation models. It focuses on mitigating risks associated with AI model vulnerabilities throughout the software development lifecycle. The guidelines aim to assist AI model producers, AI system developers, and acquirers in applying secure practices, ensuring that models are protected from unauthorized access, tampering, and other potential risks. These additions address the evolving needs outlined in Executive Order 14110 regarding safe, secure AI development.

- **[Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models](https://www.rand.org/pubs/research_reports/RRA2849-1.html)** (RAND Corporation, USA)

  This report focuses on protecting the weights of frontier artificial intelligence models - those at the cutting edge of current capabilities - from theft and misuse. It highlights the critical role of model weights, which encode core AI capabilities derived from extensive data and computational resources. The report identifies 38 distinct attack vectors and estimates their feasibility for various adversaries, ranging from cybercriminals to state actors. Recommendations include prioritizing access control, defense-in-depth strategies, and insider threat prevention. The report aims to aid AI organizations in updating security models and guide policymakers on AI security practices.

- **[Securing Machine Learning Algorithms](https://op.europa.eu/publication-detail/-/publication/c7c844fd-7f1e-11ec-8c40-01aa75ed71a1)** (European Union Agency for Cybersecurity (ENISA), EU)

  This report by ENISA provides a comprehensive analysis of security challenges related to machine learning algorithms. It highlights emerging threats such as adversarial attacks, data poisoning, and model extraction. The report emphasizes the need for tailored security controls beyond traditional information system measures to address vulnerabilities specific to machine learning. It also offers a taxonomy of algorithms, maps threats to vulnerabilities, and suggests security controls from standards like ISO 27001 and NIST. Recommendations include raising cybersecurity awareness and developing benchmarks for security controls in machine learning.

- **[Signing ML Artifacts: Building towards tamper-proof ML metadata records](https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/signing-ml-artifacts-1.pdf)** (Coalition for Secure AI (CoSAI), International)

  A short paper on model signing as the basis for verifying where a model came from and that it has not been altered. It explains what makes signing a model different from signing ordinary software, sets out what model producers and model consumers each need from it, and proposes maturity levels for adoption. It closes with NVIDIA's work on the OpenSSF Model Signing standard, which supports both conventional PKI and keyless signing with Sigstore. A follow-on to the same workstream's paper on AI supply chain risks. Approved by the CoSAI governing board on 29 September 2025.

## Foundational papers

- **[Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://csrc.nist.gov/pubs/ai/100/2/e2023/final)** (Apostol Vassilev (NIST), Alina Oprea (Northeastern University), Alie Fordyce (Robust Intelligence, Inc.), Hyrum Anderson (Robust Intelligence, Inc.), 2024)

  This NIST Trustworthy and Responsible AI report develops a taxonomy of concepts and defines terminology in the field of adversarial machine learning (AML), surveying the AML literature to create a conceptual hierarchy that includes key types of ML methods, lifecycle stages of attack, attacker goals and objectives, capabilities and knowledge of the learning process, corresponding mitigation methods, and open challenges.

- **[When Your AI Becomes a Target: AI Security Incidents and Best Practices](https://ojs.aaai.org/index.php/AAAI/article/view/30347)** (Kathrin Grosse (École Polytechnique Fédérale de Lausanne), Lukas Bieringer (QuantPi), Tarek R. Besold (Technical University Eindhoven), Battista Biggio (University of Cagliari), Alexandre Alahi (École Polytechnique Fédérale de Lausanne), 2024)

  This paper analyzes 32 real-world AI security incidents to understand the attackers' motives, influencing factors, causes, and mitigations, finding that many incidents stem from non-compliance with best practices in security and privacy-enhancing technologies.

- **[Adversarial Machine Learning in Industry: A Systematic Literature Review](https://www.sciencedirect.com/science/article/pii/S0167404824002931)** (Felix Viktor Jedrzejewski (Blekinge Institute of Technology), Lukas Thode (Blekinge Institute of Technology), Jannik Fischbach (Netlight Consulting GmbH, fortiss GmbH), Tony Gorschek (Blekinge Institute of Technology, fortiss GmbH), Daniel Mendez (Blekinge Institute of Technology, fortiss GmbH), Niklas Lavesson (Blekinge Institute of Technology), 2024)

  The paper discusses the Vulnerability of Machine Learning (ML) models to adversarial attacks, noting the critical need for developing robust defenses as these models become increasingly integral to software-intensive products across various industries.

- **[Broken Promises: Measuring Confounding Effects in Learning-based Vulnerability Discovery](https://dl.acm.org/doi/10.1145/3605764.3623915)** (Erik Imgrund (SAP Security Research), Tom Ganz (SAP Security Research), Martin Härterich (SAP Security Research), Lukas Pirch (Technische Universität Berlin), Niklas Risse (Max-Planck Institute), Konrad Rieck (Technische Universität Berlin), 2023)

  This work investigates spurious correlations as the main obstacle to transferability and generalization in learning-based vulnerability detection methods, resulting in performance losses of up to 30% for current models, and proposes a method to measure the impact of these spurious correlations on learning models and estimate their true, unbiased performance.

- **[Timing Black-Box Attacks: Crafting Adversarial Examples through Timing Leaks against DNNs on Embedded Devices](https://www.semanticscholar.org/paper/Timing-Black-Box-Attacks%3A-Crafting-Adversarial-DNNs-Nakai-Suzuki/2c47435498b8e67873cce1cc86cfbf8397b18286)** (Tsunato Nakai (Mitsubishi Electric Corporation, Ritsumeikan University), Daisuke Suzuki (Mitsubishi Electric Corporation), Takeshi Fujino (Ritsumeikan University), 2021)

  This paper proposes a novel black-box attack for crafting adversarial examples using differential processing time according to the input data of Deep Neural Networks (DNNs) on embedded devices, which is the first adversarial example attack using side-channel leaks.

- **[Securing Machine Learning Algorithms](https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms)** (Apostolos Malatras (ENISA), Ioannis Agrafiotis (ENISA), Monika Adamczyk (ENISA), 2021)

  This report provides a taxonomy for machine learning algorithms, highlighting core functionalities and critical stages, presents a detailed analysis of threats targeting machine learning systems, and examines mainstream security controls to understand how these controls can effectively detect, deter and mitigate harms from the identified threats.

- **[Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](https://ieeexplore.ieee.org/document/8835365)** (Bolun Wang (UC Santa Barbara), Yuanshun Yao (University of Chicago), Shawn Shan (University of Chicago), Huiying Li (University of Chicago), Bimal Viswanath (Virginia Tech), Haitao Zheng (University of Chicago), Ben Y. Zhao (University of Chicago), 2019)

  The paper presents the first robust and generalizable detection and mitigation system for DNN backdoor attacks, identifying backdoors and reconstructing possible triggers, and demonstrating their efficacy via extensive experiments on a variety of DNNs against two types of backdoor injection methods.

- **[Adversarial attack and defense in reinforcement learning-from AI security view](https://cybersecurity.springeropen.com/articles/10.1186/s42400-019-0027-x)** (Tong Chen (Beijing Jiaotong University), Jiqiang Liu (Beijing Jiaotong University), Yingxiao Xiang (Beijing Jiaotong University), Wenjia Niu (Beijing Jiaotong University), Endong Tong (Beijing Jiaotong University), Zhen Han (Beijing Jiaotong University), 2019)

  This paper provides a comprehensive survey on adversarial attacks and defense techniques in the context of reinforcement learning from an AI security perspective, highlighting the critical importance of building reliable reinforcement learning systems for security-critical AI applications.

- **[Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures](https://dl.acm.org/doi/10.1145/2810103.2813677)** (Matt Fredrikson (Carnegie Mellon University), Somesh Jha (University of Wisconsin-Madison), Thomas Ristenpart (Cornell Tech), 2015)

  The authors develop a new class of model inversion attack that exploits confidence values revealed along with predictions and explore its efficacy on decision trees for lifestyle surveys and neural networks for facial recognition, showing that it can estimate sensitive responses and recover recognizable images of people's faces, while also initiating experimental exploration of natural countermeasures.

- **[Can Machine Learning Be Secure?](https://www.semanticscholar.org/paper/Can-machine-learning-be-secure-Barreno-Nelson/5f198e9f1a6cace1fcee5ec53f5d35d9d83af6b7)** (Marco Barreno (University of California, Berkeley), Blaine Nelson (University of California, Berkeley), Russell Sears (University of California, Berkeley), Anthony D. Joseph (University of California, Berkeley), J. D. Tygar (University of California, Berkeley), 2006)

  The paper provides a taxonomy of different types of attacks on machine learning techniques and systems, discusses potential defenses against those attacks, explores ideas important to security for machine learning, presents an analytical model giving a lower bound on attacker's work function, and lists open problems.

- **[Adversarial Classification](https://homes.cs.washington.edu/~pedrod/papers/kdd04.pdf)** (Nilesh Dalvi (University of Washington), Pedro Domingos (University of Washington), Mausam (University of Washington), Sumit Sanghai (University of Washington), Deepak Verma (University of Washington), 2004)

  The paper formalizes the problem of adversarial classification, where an adversary actively manipulates the data to make the classifier produce false negatives, and extends the naive Bayes classifier to optimally detect and reclassify tainted instances by taking into account the adversary's optimal feature-changing strategy.

## Code and PoCs

Read, use, and live at your own risk.

- **[ADR (Agentic AI Detection and Response)](https://github.com/uber/ADR)**

  Uber's detection and response system for AI agents, covering both the coding agents employees run and customer-facing ones, through observability, security benchmarking and threat detection. Open sourced from a deployment inside Uber, which makes it one of the few tools here arriving with a production track record attached.

- **[Adversarial Robustness Toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox)**

  Python library for machine learning security, hosted by the Linux Foundation AI and Data Foundation. It implements evasion, poisoning, extraction and inference attacks together with the matching defences and robustness metrics, and works with TensorFlow, Keras, PyTorch, scikit-learn, XGBoost, LightGBM, CatBoost and GPy across images, tables, audio and video. MIT licence. The last commit on the main branch was on 13 November 2025.

- **[Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)**

  Microsoft's toolkit for running agents under policy: enforcement, zero-trust identity for the agent itself, execution sandboxing and reliability engineering, with the specifications published alongside the code.

- **[Agent Security Bench (ASB)](https://github.com/agiresearch/ASB)**

  Code for an ICLR 2025 benchmark that formalises attacks and defences against LLM-based agents and runs them across ten scenarios, from academic advising to investment and legal advice. Covers prompt injection, memory poisoning and tool misuse, and measures the defences on the same footing as the attacks. Last updated April 2026.

- **[Agent Threat Rules (ATR)](https://github.com/Agent-Threat-Rule/agent-threat-rules)**

  An open format for writing detection rules about AI agent threats. Rules are YAML against a versioned schema and carry public identifiers in the form ATR-YYYY-NNNNN, so a specific agent threat can be cited the way a CVE is. Ships a reference engine on npm and PyPI plus a GitHub Action, and the specification carries a Zenodo DOI.

- **[Agent Wiz](https://github.com/Repello-AI/Agent-Wiz)**

  Extracts the workflow out of an agent built on LangGraph, AutoGen or CrewAI, draws it, and runs an automated threat assessment over the result. Threat modelling for agentic systems is still mostly a whiteboard exercise, so a tool that reads the actual graph is worth knowing about. Last updated November 2025.

- **[AgentDojo](https://github.com/ethz-spylab/agentdojo)**

  A dynamic environment for evaluating prompt injection attacks and defences against LLM agents, from ETH Zurich's SPY Lab with Invariant Labs. It ships user tasks and injection tasks so that attacks and defences can be measured on the same ground, and accompanies a paper in the NeurIPS 2024 datasets and benchmarks track.

- **[Agentic Radar](https://github.com/splx-ai/agentic-radar)**

  Scans an agentic workflow and reports on its security posture, including which tools each agent can reach and where untrusted input enters the system. Produces a visual map alongside the findings. Last updated November 2025.

- **[AgenticSecurity](https://github.com/msoedov/agentic_security)**

  Vulnerability scanner aimed at LLM applications and agents, running a library of attack techniques against a target endpoint and reporting what got through. Configurable for custom integrations rather than assuming a particular provider. Apache-2.0.

- **[AgentPoison](https://github.com/AI-secure/AgentPoison)**

  Official implementation of the NeurIPS 2024 paper on backdooring an LLM agent through its memory or knowledge base, so that a trigger appearing in retrieved context steers the agent while ordinary queries behave normally. Relevant to anyone assessing a RAG pipeline whose retrieval corpus is not fully under their control.

- **[AI Infra Guard](https://github.com/Tencent/AI-Infra-Guard)**

  Tencent's red-teaming platform for AI systems, covering model endpoints, agents and MCP servers, with a scanner for known weaknesses in AI infrastructure components alongside the prompt-level testing. Apache-2.0.

- **[AI Prompt Fuzzer](https://github.com/PortSwigger/ai-prompt-fuzzer)**

  Burp Suite extension that brute-forces AI prompts straight from Intruder, easing integration of LLM testing into web-app pentest workflows.

- **[AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs)**

  This repository contains the challenges for the labs that were used in the course AI Red Teaming in Practice. The course was originally taught at Black Hat USA 2024.

- **[AI-BOM](https://github.com/Trusera/ai-bom)**

  Produces a bill of materials for AI: which agents, models and APIs are actually running across an infrastructure, including the ones nobody registered. Inventory is the step most AI security programmes skip, and nothing that has not been found can be secured. Last updated May 2026.

- **[AIGoat](https://github.com/orcasecurity-research/AIGoat)**

  Deliberately vulnerable AI infrastructure from Orca's research team, built to be attacked as a learning exercise. The AI equivalent of the older intentionally-insecure web apps, useful for practising against something you are allowed to break. Last updated in September 2025.

- **[AIMap](https://github.com/BishopFox/aimap)**

  Internet-scale discovery for exposed AI infrastructure, from Bishop Fox. It finds and fingerprints publicly reachable MCP servers, Ollama instances, vLLM and LiteLLM proxies, LangServe chains and Gradio apps, then security-tests what it finds. Useful for establishing what an organisation has left open before somebody else does. Last updated April 2026.

- **[AIRTBench](https://github.com/dreadnode/AIRTBench-Code)**

  Dreadnode's benchmark for measuring how far a language model can carry out an AI red teaming operation by itself, against capture the flag style challenges. It ships with the paper and a published dataset of the agents' own transcripts, so the failures can be read rather than only scored. Last updated April 2026.

- **[AIShield Watchtower](https://github.com/bosch-aisecurity-aishield/watchtower)**

  Bosch AIShield's scanner for model files and Jupyter notebooks, built on the argument that notebooks are part of the AI supply chain and are rarely included in a security review. Inspects models for unsafe serialisation and notebooks for secrets and risky code. Last updated March 2026.

- **[Anamorpher](https://github.com/trailofbits/anamorpher)**

  Implements image-scaling attacks for multimodal prompt injection: an image that looks innocuous at full size resolves into instructions once the pipeline downsamples it, so a human reviewer and the model see different content. Companion to the Trail of Bits write-up listed under guides and tutorials. Apache-2.0.

- **[Arcjet](https://github.com/arcjet/arcjet-js)**

  Security primitives called from inside application code rather than at the network edge, so the decision happens before the action does. Covers prompt injection detection, authorising an agent's tool calls, redacting sensitive data, and bot and abuse handling. JavaScript and TypeScript.

- **[Augustus](https://github.com/praetorian-inc/augustus)**

  A Go language vulnerability scanner for language models from Praetorian, testing against more than 210 adversarial attacks spanning prompt injection, jailbreaks, encoding tricks and data extraction, across 28 providers. Built for production security testing, with concurrent scanning and rate limiting, which puts it in different territory from the research-oriented scanners also listed here.

- **[Charcuterie](https://github.com/moohax/Charcuterie)**

  This is a collection of code execution techniques for ML or ML adjacent libraries and a sample attack on a blackbox model using Optuna.

- **[Corpus Poisoning Attack for Dense Retrievers](https://github.com/princeton-nlp/corpus-poisoning)**

  Corpus poisoning attack for dense retrieval models is where a malicious user generates and injects a small fraction of adversarial passages to a retrieval corpus to fool retrieval systems into returning them among the top retrieved results. Last commit December 2023.

- **[Counterfit](https://github.com/Azure/counterfit)**

  A CLI that provides a generic automation layer for assessing the security of ML models.

- **[Deep-Drop](https://github.com/moohax/Deep-Drop)**

  ML-enabled dropper. Last updated in May 2023.

- **[DeepTeam](https://github.com/confident-ai/deepteam)**

  Red teaming framework for LLMs and agents from the team behind DeepEval. Covers more than 50 vulnerability types across privacy, safety, security and agentic failure modes such as goal theft and excessive agency, and around 20 attack methods including linear and tree jailbreaks, crescendo, roleplay and encoding obfuscation. Runs locally and is scored by a model you choose, so it needs an LLM backend and an API key. Apache-2.0.

- **[Dioptra](https://github.com/usnistgov/dioptra)**

  Dioptra is a NIST software test platform for assessing the trustworthy characteristics of artificial intelligence. Dioptra provides a REST API, which can be controlled via an intuitive web interface, a Python client, or any REST client library of the user's choice for designing, managing, executing, and tracking experiments.

- **[dstack](https://github.com/Dstack-TEE/dstack)**

  A framework for confidential AI, running models inside trusted execution environments so that whoever operates the hardware cannot read the data or the weights. Addresses the deployment case where the infrastructure itself belongs in the threat model.

- **[EasyJailbreak](https://github.com/EasyJailbreak/EasyJailbreak)**

  Python framework for building and running jailbreak attacks against language models, assembling published methods into comparable components so techniques can be measured against each other rather than demonstrated one at a time. GPL-3.0.

- **[fickling](https://github.com/trailofbits/fickling)**

  A decompiler, static analyser and bytecode rewriter for Python pickle files, from Trail of Bits. Pickle is the format most model checkpoints still ship in and it executes code the moment it is loaded, so fickling exists to read what a given file will actually do before you run it, and to construct malicious ones when you are testing a defence.

- **[Foolbox](https://github.com/bethgelab/foolbox)**

  Long-running library for generating adversarial examples against neural networks, with a large collection of published attacks and support for PyTorch, TensorFlow and JAX. From the Bethge Lab. Last updated in December 2025.

- **[FuzzyAI](https://github.com/cyberark/FuzzyAI)**

  CyberArk’s coverage-guided fuzzer that auto-generates malicious prompts across 10+ attack families and logs jailbreak success rates. Ideal for CI red-team pipelines.

- **[Garak](https://docs.garak.ai/garak)**

  Garak is an open-source framework designed to identify vulnerabilities in Large Language Models (LLMs).

- **[Giskard](https://github.com/Giskard-AI/giskard-oss)**

  Evaluation, red teaming and test generation for agentic systems, with a focus on multi-turn testing where the failure only shows up several exchanges into a conversation. Version 3 is a rewrite built for dynamic testing.

- **[GPTFuzzer](https://github.com/hubertyoo/GPTFuzz)**

  Reference implementation of GPTFuzzer, which starts from human-written jailbreak templates and mutates them to find prompts that transfer across models. Accompanies the paper of the same name. Last updated in February 2026.

- **[Guardrails AI](https://github.com/guardrails-ai/guardrails)**

  YAML/Python DSL to validate or repair LLM outputs (regex, JSON Schema, semantic similarity, PII) and automatically re-ask on failure.

- **[HackAgent](https://github.com/AISecurityLab/hackagent)**

  A Python SDK and command line tool for testing AI agents as deployed, covering prompt injection, jailbreaks and goal hijacking against the running system rather than the model in isolation. Apache licensed, with a hosted app and API alongside the library.

- **[HarmBench](https://github.com/centerforaisafety/HarmBench)**

  The Center for AI Safety's standard evaluation framework for automated red teaming. It fixes the harmful requests and the judging, so that attack and defence results from different papers measure the same thing: 400 text behaviours split into standard, contextual and copyright types, across subjects from cybercrime to chemical and biological harm, a separate multimodal set, and classifier models that decide whether a response actually carried out the behaviour. The accompanying paper compares 18 red teaming methods against 33 target models and defences. Last updated August 2024; a benchmark that holds still is what keeps results comparable across papers.

- **[Julius](https://github.com/praetorian-inc/julius)**

  Fingerprints which AI serving software sits behind an address, covering Ollama, vLLM, LiteLLM and more than sixty others. A narrow tool that answers one question quickly, and a sensible first step before the broader scanning that AIMap does.

- **[L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S)**

  A collection of jailbreak prompts maintained by elder-plinius, organised into one file per provider or product, covering around forty of them from OpenAI, Anthropic, Google and Meta through to coding tools such as Cursor and Windsurf, plus material on special tokens and system prompts. Useful to red teamers as a corpus of known attacks to test a deployment against. The prompts target production models directly, so any given one may already have been patched. Last updated February 2026.

- **[Lakera PINT Benchmark](https://github.com/lakeraai/pint-benchmark)**

  The Prompt Injection Test (PINT) Benchmark provides a neutral way to evaluate the performance of a prompt injection detection system. Archived by its owner on 5 August 2026 and now read-only, so it receives no further updates. The last commit was on 16 April 2026.

- **[LLAMATOR](https://github.com/LLAMATOR-Core/llamator)**

  A Python red teaming framework for chatbots and generative AI systems, with a catalogue of attacks that can be run as a suite against a deployed assistant. Last updated May 2026.

- **[LLM Guard](https://github.com/protectai/llm-guard)**

  Drop-in Python/REST library that redacts PII, blocks jailbreak strings, enforces token limits, detects policy violations. Ships with a CLI and Hugging Face model hub presets. Archived by its maintainer on 9 July 2026 and now read-only, so it receives no further updates.

- **[MCP Context Protector](https://github.com/trailofbits/mcp-context-protector)**

  Security wrapper that sits between an MCP client and its servers, so tool descriptions and responses can be inspected and constrained rather than trusted by default. Aimed at the trust boundary an agent crosses whenever it calls a tool. Apache-2.0.

- **[MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner)**

  Scans MCP servers and the tools they expose for malicious behaviour, combining YARA rules, Cisco AI Defense's inspection API and model-based analysis. Aimed at the moment an agent is about to trust a third-party MCP server that nobody on the team wrote.

- **[Model Inversion Attack ToolBox](https://github.com/ffhibnese/Model-Inversion-Attack-ToolBox)**

  A toolbox of model inversion attacks and their defences implemented together, so the two can be measured against each other. Model inversion reconstructs training data from a model's outputs, and this gathers the main approaches into one place. Last updated June 2026.

- **[Model Transparency](https://github.com/sigstore/model-transparency)**

  Sigstore project for signing and verifying machine-learning models, so a model can be traced to who produced it and checked for tampering before it is loaded. Addresses the supply-chain half of model security rather than the model's behaviour. Apache-2.0.

- **[ModelScan](https://github.com/protectai/modelscan)**

  Scans serialised models for code that runs the moment the file is loaded, which is the risk in pickle-based formats where a model can carry a payload as legitimately as it carries weights. Handles H5, SavedModel and several PyTorch and TensorFlow serialisations. Built by Protect AI, since absorbed into Palo Alto Networks, and last updated February 2026.

- **[Moonshot](https://github.com/aiverify-foundation/moonshot)**

  Evaluation and red-teaming toolkit from Singapore's AI Verify Foundation, combining benchmark runs with interactive red teaming behind one interface. Institutional rather than vendor-backed. Apache-2.0.

- **[NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)**

  NVIDIA's open-source toolkit for adding programmable guardrails to LLM-based conversational systems. Rails are written in a dedicated modelling language and can hold a conversation to permitted topics, check inputs and outputs, and gate tool calls.

- **[OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS)**

  A toolkit for abliteration: locating the directions in an open-weight model's hidden states that drive refusal, and removing them without retraining, with the stated aim of keeping the model's general capability intact. Covers the pipeline from probing the hidden states to producing the modified model, and has a hosted demo on Hugging Face. Runs with telemetry enabled contribute anonymous benchmark data to a shared dataset. Relevant to the abliteration research in the papers archive, including work on defending against it. From the same author as L1B3RT4S.

- **[Offensive ML Playbook](https://wiki.offsecml.com/Welcome+to+the+Offensive+ML+Playbook)**

  An amalgam of TTP's on different offensive ML attacks encompassing the ML supply chain and adversarial ML attacks. It is focused heavily on attacks that have code you can use to perform the attacks right away, rather than a database of research papers. (PoC or GTFO type logic).

- **[OpenDP](https://github.com/opendp/opendp)**

  The core differential privacy library of the OpenDP project, a modular collection of algorithms with proofs behind them, for building analyses whose privacy loss is bounded and stated. The defensive counterpart to the membership inference and model inversion work covered elsewhere here.

- **[OpenPromptInjection](https://github.com/liu00222/Open-Prompt-Injection)**

  Open-source toolkit for attacks and defenses in LLM-integrated applications, which enables easy implementation, evaluation, and extension of attacks, defenses, and LLMs.

- **[OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard)**

  An OWASP incubator project defending against memory poisoning, where an agent is steered by something planted in its own long-term memory rather than in the prompt in front of it. It is built to catch the poisoning after a context window has rolled over, which is exactly when the original injection is no longer visible. Pairs with AgentPoison, the attack side, also listed here.

- **[Parley](https://github.com/dreadnode/Parley)**

  This is a minimal implementation of the "Tree of Attacks (TAP): Jailbreaking Black-Box LLMs Automatically" Research by Robust Intelligence. Last updated in February 2024.

- **[picklescan](https://github.com/mmaitre314/picklescan)**

  Scanner for Python pickle files that detects the imports and calls used to run code on load. Directly relevant because several model formats are pickles underneath, so loading a downloaded model can be equivalent to running its author's code. MIT.

- **[pipelock](https://github.com/luckyPipewrench/pipelock)**

  Firewall for AI agents, covering MCP traffic and outbound network access so an agent's tool use and egress can be constrained at runtime rather than only at the prompt. Apache-2.0.

- **[PoisonedRAG](https://github.com/sleeepeer/PoisonedRAG)**

  Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models

- **[promptfoo](https://github.com/promptfoo/promptfoo)**

  Command-line tool for testing prompts, agents and RAG pipelines, with a red-teaming mode that generates adversarial inputs and scans for vulnerabilities. Configuration is declarative and runs in CI alongside ordinary tests.

- **[PromptInject](https://github.com/agencyenterprise/PromptInject)**

  The framework from “Ignore Previous Prompt: Attack Techniques For Language Models”, the 2022 paper that named goal hijacking and prompt leaking. It assembles adversarial prompts from modular parts so attacks can be composed and measured rather than hand-written. Worth reading as the point the field started from, and separate from the Open-Prompt-Injection benchmark also listed here. Last updated April 2026.

- **[promptmap](https://github.com/utkusen/promptmap)**

  An automated prompt injection scanner for custom LLM applications. It reads the application's own system prompt, generates attacks aimed at that specific deployment, and reports which ones landed. Last updated December 2025.

- **[Proof Pudding](https://github.com/moohax/Proof-Pudding)**

  Model extraction attack for ProofPoint's e-mail scoring system by stealing scored datasets (core/data/\*.csv) and creating a copy-cat model for abuse. Last updated in April 2020.

- **[Purple Llama](https://github.com/meta-llama/PurpleLlama)**

  Meta’s umbrella repo ships ready-to-use models plus “PromptGuard 2” jailbreak detector and an agent-focused firewall with code-safety scans. Covers risks (prompt injection, insecure code) that classic chatbot guardrails miss.

- **[PyRIT](https://github.com/microsoft/PyRIT)**

  Microsoft's Python Risk Identification Tool for generative AI: an automation framework for red teaming that supplies attack strategies, scores model responses and keeps conversation history across runs. Documentation, including installation and worked examples, is at microsoft.github.io/PyRIT. The repository moved from the Azure organisation to microsoft, and the old location is archived. MIT licence.

- **[RAMPART](https://github.com/microsoft/RAMPART)**

  A pytest-native framework from Microsoft for writing safety and security tests against agentic applications, so that agent red teaming runs in the same place as the rest of a project's test suite instead of as a separate exercise.

- **[safetensors](https://github.com/safetensors/safetensors)**

  The storage format built to replace pickle for model weights, holding tensors with no code path that runs on load and with zero-copy reads so little is given up on speed. This is the mitigation that the model serialisation attacks described elsewhere on this site are aimed at, and it is now the default across much of the Hugging Face ecosystem.

- **[SCAM (Security Comprehension Awareness Measure)](https://github.com/1Password/SCAM)**

  A benchmark from 1Password measuring whether an AI agent notices security-relevant details during ordinary multi-turn work, which is a different question from whether it can be jailbroken on request. Comes with a leaderboard and replayable runs. Last updated February 2026.

- **[SecML-Torch](https://github.com/pralab/secml-torch)**

  A PyTorch library for evaluating the adversarial robustness of deep learning models, from the PRA Lab at the University of Cagliari, whose machine learning security course is also listed here. Built for running attacks carefully, which is where robustness claims usually come apart. Last updated July 2026.

- **[Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner)**

  Scans agent skills for prompt injection, data exfiltration and malicious code, using YARA-X pattern matching, AST and dataflow analysis, and an optional model acting as a judge. Skills get installed the way packages do and are rarely read first, which is the gap this addresses.

- **[SkillSpector](https://github.com/NVIDIA/SkillSpector)**

  NVIDIA's scanner for AI agent skills: it inspects skill definitions for prompt injection, unsafe tool use and permission problems before they are installed. Aimed at the packaging layer, which is newer than the model layer and less well covered. Apache-2.0.

- **[Snyk Agent Scan](https://github.com/snyk/agent-scan)**

  Scanner that discovers agent components on a machine, including MCP servers, agents and skills, and checks them for prompt injections and known vulnerabilities. It started as Invariant Labs' mcp-scan and is now maintained by Snyk under the name agent-scan.

- **[spikee](https://github.com/ReversecLabs/spikee)**

  Prompt injection toolkit from Reversec Labs for building test datasets, running them against a target and measuring what succeeded, so injection resistance can be tracked over time rather than probed once. Apache-2.0.

- **[Superagent](https://github.com/superagent-ai/superagent)**

  An SDK for guarding an AI application while it runs: classifying input for prompt injection and malicious instructions, stripping personal data and secrets out of what the model sees, and running red team scenarios against an agent. TypeScript and Python.

- **[TenSEAL](https://github.com/OpenMined/TenSEAL)**

  Homomorphic encryption over tensors, built on Microsoft SEAL with a Python interface, for running inference on data that the party doing the computing never decrypts.

- **[tensor-man](https://github.com/dreadnode/tensor-man)**

  tensor-man is a utility to inspect, validate, sign and verify machine learning model files.

- **[TensorFlow Privacy](https://github.com/tensorflow/privacy)**

  Optimisers for training models with differential privacy, together with the analysis tools for computing what guarantee a given training run actually achieved. Maintained by Google.

- **[TextAttack](https://github.com/QData/TextAttack)**

  Framework for adversarial attacks, data augmentation and adversarial training on NLP models, with published attack recipes reimplemented against a common interface. One of the established tools for text-domain adversarial work. MIT.

- **[TruLens](https://github.com/truera/trulens)**

  Instrumentation and eval library (OpenTelemetry style) that traces LLM chains, scores outputs with configurable feedback functions, and stores runs for comparison.

- **[Vigil-LLM](https://github.com/deadbits/vigil-llm)**

  Alpha-stage scanner and REST API that applies a configurable chain of detectors to find prompt injections, jailbreaks, and other threats in prompts/responses. Last updated in January 2024.

## Guides and Tutorials

Provided for informational purposes only. Read, use, and live at your own risk.

- **[Agentic AI Threat Modeling Framework: MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)**

  Cloud Security Alliance threat-modelling method aimed at agentic systems, where the usual approaches fit badly because the agent plans, calls tools and acts across trust boundaries. It works through seven layers, from the foundation model up to the agent ecosystem, and asks what can go wrong at each. Published February 2025.

- **[ClearML Vulnerabilities: Exploiting MLOps for Remote Code Execution](https://hiddenlayer.com/research/not-so-clear-how-mlops-solutions-can-muddy-the-waters-of-your-supply-chain/)**

  HiddenLayer write-up on reaching remote code execution through an MLOps platform rather than through the model. Useful as a concrete example of the argument that the pipeline around a model is as much of a target as the model, and easier to reach.

- **[Defending Against Vision Prompt Injection Attacks in Large Language Models](https://blog.roboflow.com/gpt-4-vision-prompt-injection/)**

  This article explores the concept of Vision Prompt Injection vulnerabilities in Large Language Models (LLMs) with image processing capabilities, where malicious instructions can be embedded within images, even invisibly, to make the model perform unauthorized actions or extract sensitive data. The article showcases real-life examples of Vision Prompt Injection attacks and discusses the challenges and potential strategies for defending against them as businesses start to build applications using multimodal LLMs.

- **[Embrace the Red: Machine Learning Attack Series](https://embracethered.com/blog/posts/2020/machine-learning-attack-series-overview/)**

  A series of blog posts focused on machine learning from a red teaming and security testing perspective. The author covers various topics, including machine learning basics, building a machine learning system called Husky AI, threat modeling, practical attacks, and defenses.

- **[Exploring Prompt Injection Attacks](https://www.nccgroup.com/research/exploring-prompt-injection-attacks/)**

  NCC Group primer from December 2022, written while prompt injection was still new. Explains what a prompt is in the machine-learning sense, how injection abuses that, what it can reach, and what to do about it. Still one of the clearer first explanations of the mechanism.

- **[Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning)**

  This document tabulates both intentional and unintentional failure modes in machine learning systems. Intentional failures are caused by an active adversary attempting to subvert the system to attain their goals, while unintentional failures occur when an ML system produces a formally correct but completely unsafe outcome. The document aims to provide a common vocabulary for engineers, lawyers, and policymakers to discuss these issues and build solutions.

- **[GenAI Incident Response Guide 1.0](https://genai.owasp.org/resource/genai-incident-response-guide-1-0/)**

  OWASP guide on responding to incidents involving generative AI, covering what differs from ordinary incident response: prompts and outputs as evidence, model and data rollback, and the fact that the same input may not reproduce the same failure.

- **[Hacking deep learning: model inversion attack by example](https://blogs.rstudio.com/ai/posts/2020-05-15-model-inversion-attacks/)**

  Worked example of a model inversion attack on the Posit (formerly RStudio) AI blog, reconstructing training data from a model's outputs with the code alongside. Reads as a tutorial rather than a paper summary.

- **[Machine Learning Models are Code](https://hiddenlayer.com/research/models-are-code/)**

  HiddenLayer research making the case that a serialised model is executable content, not inert data, and showing what that allows. Pairs with the Safetensors write-up already listed here.

- **[Managing the cyber risk of agentic AI](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)**

  Practical advice from the UK National Cyber Security Centre for teams deploying AI agents with real autonomy, organised as seven considerations: identify what could go wrong, prompt carefully, set oversight to match the risk, sandbox the agent's environment, log and monitor its activity, make its actions attributable, and keep the ability to shut it down. Published on 20 August 2026 as interim advice; the NCSC says formal guidance is in development and will supersede it.

- **[Microsoft AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team)**

  Microsoft's entry point for its AI red teaming material: how the team is organised, how it plans an operation, and what it looks for. The starting point for the failure-mode and threat-modelling documents also listed here.

- **[Multi-Agentic System Threat Modeling Guide v1.0](https://genai.owasp.org/resource/multi-agentic-system-threat-modeling-guide-v1-0/)**

  OWASP guide to threat modelling systems of several interacting agents, where the risks come from delegation, shared memory and trust between agents rather than from any one model.

- **[PIPE - Prompt Injection Primer for Engineers](https://github.com/jthack/PIPE)**

  This guide, by Joseph Thacker, assists developers in creating secure AI-powered applications and features by helping them understand the actual risks of prompt injection. Last updated in August 2023.

- **[PrivacyRaven: Implementing a proof of concept for model inversion](https://blog.trailofbits.com/2021/11/09/privacyraven-implementing-a-proof-of-concept-for-model-inversion/)**

  Trail of Bits write-up on building a working model inversion proof of concept, including what did not work. Useful for the engineering detail rather than the result.

- **[Prompt Injection Attacks Handbook](https://www.lakera.ai/ai-security-guides/prompt-injection-attacks-handbook)**

  A practical handbook on prompt injection: attack techniques, real-world examples, and the defensive measures available against them.

- **[Red-Teaming Large Language Models](https://huggingface.co/blog/red-teaming)**

  Hugging Face introduction to red teaming language models: what it is, how it differs from ordinary evaluation, and how findings feed back into training. A reasonable first read before picking up a red-teaming tool.

- **[Securing Agentic Applications Guide 1.0](https://genai.owasp.org/resource/securing-agentic-applications-guide-1-0/)**

  OWASP guide for people building agentic applications, covering tool access, permissions, memory and the places an agent can be induced to act against its operator.

- **[Silent Sabotage: Hijacking Safetensors conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)**

  This article demonstrates how an attacker could compromise the Hugging Face Safetensors conversion service and its associated bot to send malicious pull requests and hijack models submitted through the conversion service. The authors show how it's possible to persist malicious code inside the service, allowing models to be automatically hijacked during conversion, potentially leading to a widespread supply chain attack.

- **[The Beginner's Guide to Visual Prompt Injections: Invisibility Cloaks, Cannibalistic Adverts, and Robot Women](https://www.lakera.ai/blog/visual-prompt-injections)**

  This article explores the concept of visual prompt injection, a vulnerability in Large Language Models (LLMs) with image processing capabilities, where malicious instructions embedded within images can make the model perform unintended actions. The article showcases real-life examples of visual prompt injection attacks, such as invisibility cloaks, robot disguises, and ad suppression, and highlights the need for robust security measures as businesses adopt multimodal models.

- **[The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)**

  Simon Willison's post from 16 June 2025 naming the three properties that together make an AI agent exploitable: access to private data, exposure to untrusted content, and the ability to communicate externally. It is a short, concrete account of how prompt injection turns into data exfiltration once an agent holds tools, and the phrase has become common shorthand when reviewing agent designs.

- **[The Month of AI Bugs](https://embracethered.com/blog/tags/month-of-ai-bugs/)**

  Johann Rehberger published one vulnerability a day through August 2025, ending with 29 issues across AI coding agents and assistants including GitHub Copilot, Claude Code, Amazon Q Developer, Cursor, Windsurf, Devin, OpenHands and Google Jules. Most are prompt injection turning into data exfiltration or remote code execution, and each post carries the reproduction steps and the disclosure timeline. This tag page indexes the series; the wrap-up is dated 30 August 2025.

- **[The Waluigi Effect (mega-post)](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post)**

  The Waluigi Effect is a phenomenon in large language models (LLMs) where training an LLM to satisfy a desirable property makes it easier to elicit the opposite behavior. Using Simulator Theory, the author argues that LLMs produce a superposition of well-behaved "luigi" and misbehaving "waluigi" simulacra, suggesting that techniques like RLHF may fail to eliminate deceptive waluigis and could make chatbots more misaligned. This has important implications for AI security, as it highlights the challenge of aligning LLMs and suggests that misalignment risks could increase with model capability. Understanding the Waluigi Effect is crucial for developing robust alignment strategies to prevent negative outcomes and existential risks.

- **[Threat Modeling AI/ML Systems and Dependencies](https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml)**

  This document provides guidance on threat enumeration and mitigation specific to the AI and Machine Learning space. It supplements existing SDL threat modeling practices and is intended to be used as a reference during security design reviews of products/services interacting with or taking dependencies on AI/ML-based services, as well as products/services being built with AI/ML at their core.

- **[Using GPT-Eliezer against ChatGPT Jailbreaking](https://www.alignmentforum.org/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking)**

  This article proposes using a separate language model, acting as a suspicious AI safety engineer named "Eliezer Yudkowsky," to evaluate prompts before sending them to ChatGPT. The goal is to prevent jailbreaking attempts and filter out dangerous prompts that could lead to harmful or illegal behavior from the AI chatbot.

- **[Weaponizing image scaling against production AI systems](https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/)**

  Trail of Bits research from August 2025 on hiding instructions that appear only once an image is downscaled by the pipeline, so the model sees content a reviewer looking at the original never would.

## Courses

Do your own research and due diligence before enrolling.

- **[AI Red Teamer Path (Hack The Box Academy)](https://academy.hackthebox.com/path/preview/ai-red-teamer)** (3-Advanced, Above 5 hours)

  A job role path on Hack The Box Academy built in collaboration with Google and mapped to Google's Secure AI Framework. Twelve modules and 230 sections covering prompt injection, jailbreaks, adversarial machine learning, model privacy attacks, supply chain risk and deployment threats, worked through hands-on in the platform's labs. The curriculum outline is public; working through the modules needs an HTB Academy account. Rated hard.

- **[AI Red Teaming 101 (Microsoft Learn)](https://learn.microsoft.com/en-us/security/ai-red-team/training)** (1-Beginner, Self-paced)

  A limited video series from Microsoft Learn on red teaming generative AI, released in July 2025 and built from case studies and the tooling Microsoft's own AI red team uses. The videos are keyed to the AI Red Teaming Playground Labs challenges listed under Code and PoCs, so the series can be watched on its own or worked through against those labs.

- **[AI Security Essentials](https://www.udemy.com/course/ai-security-essentials/)** (1-Beginner, Under 5 hours)

  "AI Security Essentials" is an online course designed to deepen understanding of AI system security, covering threat modeling, anomaly detection, ethical considerations, and best practices in AI security. It offers practical exercises, case studies, and real-life examples to equip security professionals, business professionals, and students with the skills to protect AI models, datasets, and infrastructure, promoting trust in AI technology.

- **[AI Security Foundation Course](https://www.dnv.com/training/ai-security-foundation-course/)** (2-Intermediate, Above 5 hours)

  A two-day course for cybersecurity professionals covering how AI can be exploited, the threat vectors and risk analysis involved, and how AI-driven defences are designed, implemented and evaluated. The Security Academy that ran it was acquired by DNV, so the course is now delivered by DNV as tutored online or classroom training. The exam is supervised by SECO-Institute, which awards the S-AISF certification. Basic knowledge of IT security is recommended.

- **[Artificial Intelligence for Cybersecurity](https://www.linkedin.com/learning/artificial-intelligence-for-cybersecurity-22882411/)** (2-Intermediate, Under 5 hours)

  In "Artificial Intelligence for Cybersecurity," Sam Sehgal teaches how to apply AI to tackle complex cybersecurity challenges effectively, with proper preparation and safeguards. He clarifies AI's definition, its application in cybersecurity, and outlines the distinctions between discriminative and generative AI. The course emphasizes the critical cybersecurity principles of confidentiality, integrity, and availability, discusses existing cybersecurity gaps, and explores practical solutions using AI and machine learning to enhance security measures.

- **[Artificial Intelligence Risk and Cyber Security Course 2026](https://www.udemy.com/course/artificial-intelligence-ai-governance-and-cyber-security/)** (1-Beginner, Under 5 hours)

  This course is designed to address the unique risks introduced by AI and Machine Learning, focusing on governance, cyber-security frameworks, and risk management without requiring prior technical knowledge. It targets risk management professionals, cyber-security experts, and AI professionals, offering insights into AI risks, creating governance frameworks, addressing cyber-security risks in AI systems, implementing security controls throughout the Machine Learning lifecycle, and leveraging ChatGPT for enhanced security processes.

- **[Certified AI Security Management and Leadership (CAISML)](https://niccs.cisa.gov/training/catalog/tonex/certified-artificial-intelligence-ai-security-management-and-leadership-caisml)** (2-Intermediate, Above 5 hours)

  Tonex programme for leaders overseeing AI security work, covering governance frameworks, policy enforcement and building security practice around AI initiatives. Instructor-led online and scheduled on request, listed in the CISA NICCS catalogue.

- **[Certified AI Security Professional](https://niccs.cisa.gov/training/catalog/hysn/certified-ai-security-professional)** (2-Intermediate, Above 5 hours)

  Self-paced course from HYSN Technologies (Practical DevSecOps) on the risks in the AI supply chain. Covers adversarial machine learning, data poisoning, model inversion and evasion attacks, securing data pipelines and model integrity, and maps risks against MITRE ATLAS. Includes hands-on labs, differential privacy and federated learning. Listed in the CISA NICCS catalogue.

- **[Certified Chief AI Security Officer (CCASO)](https://niccs.cisa.gov/training/catalog/tonex/certified-chief-artificial-intelligence-ai-security-officer-ccaso)** (2-Intermediate, Above 5 hours)

  Tonex programme for those leading an AI security strategy, covering risk governance, compliance, AI cyber threats and organisational security planning at leadership level. Instructor-led online and scheduled on request, listed in the CISA NICCS catalogue.

- **[Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent)** (2-Intermediate, Self-paced)

  A deliberately vulnerable ReAct agent built with LangChain, for experimenting with Thought/Action/Observation injection, which targets an agent's reasoning steps rather than its final answer. Adapted from a challenge WithSecure ran at the BSides London 2023 capture the flag, and accompanied by the original write-up and video. Last updated June 2025.

- **[Damn Vulnerable Model Context Protocol (DVMCP)](https://github.com/harishsg993010/damn-vulnerable-MCP-server)** (2-Intermediate, Self-paced)

  A deliberately vulnerable MCP server carrying ten challenges of increasing difficulty, each showing a different way an MCP implementation can be attacked. Aimed at people shipping or reviewing MCP servers who want to meet the failure modes on a target where breaking things is the point.

- **[FinBot Agentic AI Capture The Flag](https://genai.owasp.org/resource/finbot-agentic-ai-capture-the-flag-ctf-application/)** (2-Intermediate, Self-paced)

  An OWASP Gen AI Security Project capture the flag built on a simulated financial services application, covering vulnerabilities specific to agentic systems. The setting is the useful part: these are the failure modes that appear once an agent holds tools and acts on data it did not author.

- **[Generative AI for Cybersecurity](https://coderedpro.com/products/generative-ai-for-cybersecurity-course)** (3-Advanced, Above 5 hours)

  This course dives into Generative AI and LLMs in cybersecurity, offering an understanding of their architecture, technology, and security implications. With hands-on experience using open-source models for cyber defense, participants learn to identify and mitigate AI-related security risks. It requires knowledge of cybersecurity, AI/ML principles, and programming in Python. The course covers LLM architecture, technology stacks, security considerations, and practical applications, empowering learners to enhance their organization's cyber resilience.

- **[Generative AI for Security Professionals](https://www.pluralsight.com/paths/generative-ai-and-cybersecurity)** (1-Beginner, Under 5 hours)

  This learning path, comprised of 4 courses spanning 2 hours, delves into how Generative AI can revolutionize cybersecurity. It covers the integration of Generative AI in security operations, addressing data privacy, security risks, and how to harness Generative AI's potential effectively. The courses explore the balance between enhancing security measures and the inherent risks of Generative AI, offering insights into leveraging AI for both offensive and defensive cybersecurity operations.

- **[Generative AI in Cybersecurity](https://www.gsdcouncil.org/certified-generative-ai-in-cybersecurity)** (3-Advanced, Above 5 hours)

  The Generative AI in Cybersecurity Certification by GSDC is designed for cybersecurity professionals to master the use of Generative AI in detecting and mitigating cyber threats. It covers generative models, ethical considerations, and AI application skills, aiming to enhance digital defenses and provide a competitive edge in cybersecurity. The program requires programming knowledge, involves a 60-minute exam, and offers a deep dive into Generative AI fundamentals, cybersecurity basics, GANs, VAEs, and ethical considerations in AI.

- **[LLMVault](https://github.com/CyberSunil/LLMVault)** (2-Intermediate, Self-paced)

  A self-hosted training platform covering the OWASP Top 10 for LLM applications, with a deliberately vulnerable scenario for each item, run locally through Docker. Every exercise is meant to be exploited and then defended, which makes it a practical counterpart to the OWASP list rather than a reading of it.

- **[Machine Learning Security (University of Cagliari)](https://github.com/unica-mlsec/mlsec)** (3-Advanced, Above 5 hours)

  The objective of this course is to provide students with the fundamental elements of machine learning security in the context of different application domains. The main concepts and methods of adversarial machine learning are presented, from threat modeling to attacks and defenses, as well as basic methods to properly evaluate adversarial robustness of a machine learning model against different attacks.

- **[SEC411: AI Security Principles and Practices: GenAI and LLM Defense](https://www.sans.org/cyber-security-courses/ai-security-principles-practices)** (1-Beginner, Above 5 hours)

  SANS course introducing generative AI and LLM security for practitioners with no prior AI experience. Covers tokenisation and attack surface, prompt injection, jailbreaking, RAG manipulation and MCP security, and applies the OWASP Top 10 for LLMs, MITRE ATLAS and the NIST AI RMF through hands-on labs.

- **[SEC495: Leveraging LLMs: Building and Securing RAG, Contextual RAG, and Agentic RAG](https://www.sans.org/cyber-security-courses/leveraging-llms-building-securing-rag)** (2-Intermediate, Above 5 hours)

  SANS self-paced course on building and securing retrieval-augmented generation systems, covering contextual and agentic RAG architectures and the security considerations specific to each.

- **[SEC535: Offensive AI - Attack Tools and Techniques](https://www.sans.org/cyber-security-courses/offensive-ai-attack-tools-techniques)** (3-Advanced, Above 5 hours)

  SANS course on the offensive side of AI security: the tools and techniques used to attack AI systems, aimed at red teams and penetration testers.

- **[SEC545: GenAI and LLM Application Security](https://www.sans.org/cyber-security-courses/genai-llm-application-security)** (3-Advanced, Above 5 hours)

  Five-day SANS course on securing generative AI and LLM applications, from threat modelling through to defending deployed systems.

- **[Security for Artificial Intelligence Software and Services](https://www.coursera.org/learn/security-for-artificial-intelligence-software-and-services)** (2-Intermediate, Under 5 hours)

  The course "Security Basics for Artificial Intelligence Software and Services" provides an overview at securing AI technologies. It covers ethical issues, common threats, and practical security strategies like secure coding and vulnerability assessments. Aimed at developers and security professionals, it equips participants with the skills to protect AI systems against emerging threats, ensuring their reliability and integrity.

- **[Security Risks in AI and Machine Learning: Categorizing Attacks and Failure Modes](https://www.linkedin.com/learning/security-risks-in-ai-and-machine-learning-categorizing-attacks-and-failure-modes/)** (1-Beginner, Under 5 hours)

  This course, led by Diana Kelley, explores the trust we place in AI and ML technologies despite their vulnerabilities to attacks and failures. Kelley uses real-world examples to demonstrate how ML and AI can falter, offering guidance on creating resilient systems. She covers both intentional attacks and unintentional failures, highlighting security and privacy risks. The course provides strategies for enhancing ML robustness, including dataset hygiene, adversarial training, and secure API access.

- **[Web LLM attacks (PortSwigger Web Security Academy)](https://portswigger.net/web-security/llm-attacks)** (1-Beginner, Self-paced)

  Free interactive labs on attacking applications that have a language model wired into them. It works through prompt injection, mapping the API and plugin surface a model has been given, insecure output handling, indirect injection through content the model reads, training data poisoning and leaking sensitive training data, then closes on defences. Each topic ends in a hosted lab solved in the browser with nothing to install, and a later section covers weaknesses in AI-powered scanners themselves.

## Communities

Join at your own risk. Lurk at your own risk. Interact at your own risk.

- **[AI Security](https://www.linkedin.com/groups/8196854/)** (Community, LinkedIn)

  A small LinkedIn group for AI security discussion, community run, with posts through 2026. Membership is under a thousand, which keeps it at conversation scale. LinkedIn shows the group to signed-in members only, so joining is the only way to read it.

- **[AI Security Forum](https://aisecurity.forum/)** (Nonprofit, Event series)

  An event series for people working across AI, cybersecurity and national security, with the stated aim of securing powerful models. Editions have run in Las Vegas, Washington DC, Paris and Tel Aviv since 2023, alongside a reading group in DC, and attendance is by application. It publishes a code of conduct and an information sharing policy, and is fiscally sponsored by Hack Club, a 501(c)(3) nonprofit.

- **[AI Village](https://aivillage.org/)** (Community, Discord)

  A hacker community for AI security that runs the AI Village at DEF CON along with workshops, capture-the-flag events and red-team exercises through the year. It describes itself as bringing hackers, researchers, engineers and policymakers together through hands-on AI security education. Day-to-day conversation happens on its Discord.

- **[CSA AI Safety Working Group](https://cloudsecurityalliance.org/research/working-groups/ai-safety)** (Nonprofit, Working group)

  A Cloud Security Alliance research working group building best practices for AI, with an initial focus on generative AI. Anyone can join, and the time commitment ranges from reviewing a near-final publication to co-authoring new research. Output is published as free CSA papers.

- **[Global AI Security Community](https://www.meetup.com/ai-sec/)** (Community, Meetup)

  A practitioner-led Meetup group covering LLM, agent and generative AI security, from prompt injection and data leakage through tool misuse, supply chain risk, model governance and runtime guardrails. It runs talks, workshops and community demos, and with over eleven thousand members it is one of the larger AI security groups on the platform. Organised from Pune, India, so check session times before planning around them.

- **[huntr](https://discord.com/invite/GBmmty82CM)** (Company, Discord)

  The Discord behind huntr, a bug bounty platform for AI and machine learning projects, where researchers discuss findings, triage and what is in scope. huntr was built by Protect AI, now part of Palo Alto Networks; the platform and this Discord carry on under the huntr name.

- **[OWASP Gen AI Security Project](https://genai.owasp.org/contribute/)** (Nonprofit, Slack)

  The working community behind the OWASP Top 10 for LLM applications and the project's other generative AI security output. Discussion happens in the OWASP Slack workspace, in channels such as #project-top10-for-llm and #team-llm-discuss, with regular open meetings. OWASP membership is not required to take part.

## Links

Useful references that do not fit neatly anywhere else on the map.

- **[AI Incident Database](https://incidentdatabase.ai/)**

  The AI Incident Database is dedicated to indexing the collective history of harms or near harms realized in the real world by the deployment of artificial intelligence systems. Like similar databases in aviation and computer security, the AI Incident Database aims to learn from experience so we can prevent or mitigate bad outcomes.

- **[Awesome AI Security (ottosulin)](https://github.com/ottosulin/awesome-ai-security)**

  Long-running community list of AI security resources, running since June 2023 and still updated. Covers frameworks and taxonomies, offensive and defensive tooling, papers and vulnerability databases. Broader and less selective than a curated map, which is the point: it is where to look when you want everything on a topic rather than a short answer. MIT licence.

- **[Awesome AI Security Tools (scadastrangelove)](https://github.com/scadastrangelove/awesome-ai-security-tools)**

  Tool-focused list covering AI security and AI-assisted security work: agent security, ML supply chain, pentest agents, AI SAST, LLM-driven fuzzing, SOC and SIEM triage, and LLM red teaming. It includes commercial products alongside open source and says so, so read it as an inventory rather than a recommendation. Started May 2026 and updated frequently.

- **[Awesome MLSecOps](https://github.com/RiccardoBiosas/awesome-MLSecOps)**

  MLSecOps list covering the operational side: model scanning, supply-chain protection, pipeline security, adversarial ML defence and AI red teaming. Running since April 2023, still updated, and mirrored at awesomemlsecops.com. The closest thing here to a map of securing the machine-learning pipeline itself rather than the model. MIT licence.

- **[Cybersecurity Risks of AI-Generated Code](https://cset.georgetown.edu/publication/cybersecurity-risks-of-ai-generated-code/)**

  This issue brief explores the cybersecurity risks of AI-generated code, highlighting challenges posed by large language models used in software development. The report categorizes risks into three areas: insecure code generation, model vulnerabilities, and downstream impacts like feedback loops in AI training. Experimental findings show that nearly half of the evaluated code snippets from five prominent LLMs contained impactful bugs, emphasizing the importance of comprehensive security assessments. It also discusses the unequal risk distribution across organizations, the need for multi-stakeholder mitigation strategies, and enhancements in existing cybersecurity frameworks to address these novel challenges.

- **[MIT AI Risk Repository](https://airisk.mit.edu/)**

  A living database of more than 1,700 AI risks extracted from 74 published frameworks and classifications, maintained by the AI Risk Initiative at MIT FutureTech. Each risk is filed twice: by cause (which entity, intentional or not, before or after deployment) and by domain, across seven domains and 24 subdomains that include malicious actors, privacy and AI system safety. Version 4 went live on 4 December 2025. The database is free to copy under CC BY 4.0, and the same group runs an AI incident tracker alongside it.

- **[NSA Artificial Intelligence Security Center](https://www.nsa.gov/AISC/)**

  The AISC will be a key part of NSA's cybersecurity mission, with the goal to defend the Nation's AI through Intel-Driven collaboration with industry, academia, the IC, and other government partners.

- **[OECD AI Incidents Monitor](https://oecd.ai/en/incidents)**

  The OECD AI Incidents Monitor (AIM) documents AI incidents to help policymakers, AI practitioners, and all stakeholders worldwide gain valuable insights into the incidents and hazards that concretise AI risks. Over time, AIM will help to show patterns and establish a collective understanding of AI incidents and their multifaceted nature and serve as an important tool for trustworthy AI.

- **[Open Source LLM Scanners](https://github.com/psiinon/open-source-llm-scanners)**

  A plain list of open-source LLM security scanners on GitHub ordered by stars, kept by the founder of OWASP ZAP. It says openly that it offers no analysis, which is what makes it useful as a completeness check against a curated selection like this one. Last updated February 2026.

- **[OWASP LLM Security Verification Standard](https://github.com/OWASP/www-project-llm-verification-standard)**

  The primary aim of the OWASP Large Language Model Security Verification Standard (LLMSVS) Project is to provide an open security standard for systems which leverage artificial intelligence and Large Language Models. The standard provides a basis for designing, building, and testing robust LLM backed applications, including architectural, model lifecycle, model training, model operation and integration, model storage and monitoring concerns.

- **[Policy Alignment on AI Transparency - Partnership on AI](https://partnershiponai.org/policy-alignment-on-ai-transparency/)**

  Partnership on AI’s Policy Alignment on AI Transparency conducts a comparative analysis of eight leading policy frameworks for foundation models, with a particular focus on documentation requirements, which are a critical lever for achieving transparency and safety.

- **[Prompt Hacking Resources](https://github.com/PromptLabs/Prompt-Hacking-Resources)**

  A curated list of material on prompt hacking from the Learn Prompting project, covering AI red teaming, jailbreaking, prompt injection and adjacent safety work. It leans towards the prompting community rather than the security industry, which makes it a useful second opinion against the other lists here.

## About this repository

The site is the source of truth. This README is generated by [`build_readme.py`](build_readme.py) from the site's `data/*.json` files, and a [monthly workflow](.github/workflows/rebuild.yml) rebuilds it, committing only when something changed. Do not edit README.md by hand: the next rebuild would overwrite your change.

To suggest an entry or a correction, [open an issue](https://github.com/sambucci/ai-security-ninja/issues) with a source. Accepted changes land on the site first and flow here at the next rebuild. An entry is amended or removed when a source shows it should be, never on a single failed link.

Kept by [Luca Sambucci](https://www.sambucci.com), founder of [Noctive Security](https://www.noctivesecurity.com). Curated through an agent, kept free of hype.

Text licensed under [CC BY 4.0](LICENSE); `build_readme.py` is MIT.
