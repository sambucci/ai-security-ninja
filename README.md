# AI Security Ninja

A curated, living map of AI security: frameworks, foundational papers, code, guides, courses and communities. This repository mirrors the curated sections of [aisecurity.ninja](https://aisecurity.ninja) and rebuilds itself from the site's data once a month.

I built the map as my own reference and made it public because it seemed useful. The site carries the whole thing, including a [papers feed](https://aisecurity.ninja/papers) that updates itself every day from arXiv; that stream is deliberately not mirrored here. What this repository holds is the slow-moving, human-reviewed layer, the part that benefits from being forkable, searchable and citable.

**Inclusion is not endorsement.** I am not affiliated with, endorsed by or connected to any of the projects, organisations, courses or communities listed. Entries are amended or removed on evidence; see [how to suggest a change](#about-this-repository) at the end.

108 entries in 7 sections. Sections last reviewed on the site: 2026-08-05.

## Contents

- [Frameworks and Governance](#frameworks-and-governance) (30)
- [Foundational papers](#foundational-papers) (11)
- [Code and PoCs](#code-and-pocs) (28)
- [Guides and Tutorials](#guides-and-tutorials) (11)
- [Courses](#courses) (17)
- [Communities](#communities) (5)
- [Links](#links) (6)

## Frameworks and Governance

A collection of guides and frameworks (not laws) from government-affiliated or otherwise noteworthy institutions.

- **[A Sensible Regulatory Framework for AI Security](https://www.mitre.org/news-insights/publication/sensible-regulatory-framework-ai-security)** (MITRE Corporation, USA)

  A comprehensive approach to regulating AI to ensure security and mitigate risks. It categorizes AI into three domains: as a subsystem, as human augmentation, and with autonomous agency. Each category presents unique risks that require tailored regulatory measures. Recommendations include improving AI assurance, developing robust audit mechanisms, and focusing on the interplay between AI components in complex systems. The paper emphasizes the need for continuous regulatory analysis and the creation of frameworks that align AI development with public safety, while avoiding regulatory overreach that could stifle innovation.

- **[Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2e2025)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf)** (National Institute of Standards and Technology (NIST), USA)

  This document presents a detailed taxonomy and standardized terminology for adversarial machine learning (AML), focusing on attacks and mitigation strategies for AI systems. It classifies attacks into categories based on learning methods, attacker goals, and stages of the machine learning lifecycle. The report emphasizes the importance of understanding adversarial risks across predictive and generative AI systems and outlines corresponding mitigation techniques. By providing a common language, the framework aids in securing AI systems against threats like evasion, data poisoning, and privacy violations. This entry points to the 2025 edition, NIST AI 100-2e2025, published in March 2025, which extends the 2023 taxonomy to generative AI, including attacks on large language models, retrieval-augmented generation and agents.

- **[AI Assurance: A Repeatable Process for Assuring AI-Enabled Systems](https://www.mitre.org/news-insights/publication/ai-assurance-repeatable-process-assuring-ai-enabled-systems)** (MITRE Corporation, USA)

  The document presents a comprehensive framework for AI assurance, focusing on managing risks across the lifecycle of AI-enabled systems. The framework integrates risk management practices and emphasizes a repeatable engineering process to ensure AI systems operate effectively while managing safety, security, privacy, and other key trust factors. Through a detailed assurance plan, the process addresses system characterization, risk discovery, and evaluation, making it adaptable to various sectors. The approach leverages real-world pilot studies to highlight its applicability, and promotes sector-specific solutions for domain-specific outcomes.

- **[AI Cyber Security Code of Practice](https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice)** (Department for Science, Innovation and Technology (DSIT), UK)

  A voluntary code published on 31 January 2025 setting out baseline cyber security principles for the organisations that develop, deploy and operate AI systems. It runs across the lifecycle, from secure design and development to deployment, maintenance and end of life, and ships with an implementation guide. The department submitted it to ETSI, where it forms the basis of the technical specification TS 104 223 and the accompanying implementation guide TR 104 128.

- **[AI Data Security: Best Practices for Securing Data Used to Train and Operate AI Systems](https://www.cisa.gov/news-events/alerts/2025/05/22/new-best-practices-guide-securing-ai-data-released)** (Cybersecurity and Infrastructure Security Agency (CISA), National Security Agency (NSA) and Federal Bureau of Investigation (FBI), USA)

  A joint cybersecurity information sheet released on 22 May 2025 by CISA, the National Security Agency, the FBI and partner agencies in Australia, New Zealand and the United Kingdom. It sets out the risks that arise from data security and integrity problems across the AI lifecycle, from development and testing through deployment and operation, and the practices that address them: data protection measures, risk management, monitoring, threat detection and network defence. This CISA alert page links to the full PDF.

- **[AI Risk Assessment for ML Engineers](https://learn.microsoft.com/en-us/security/ai-red-team/ai-risk-assessment)** (Microsoft, USA)

  This document provides a framework for organizations to assess the security posture of their AI systems, aligned with existing information security efforts and business objectives. It covers various areas related to AI systems, including machine learning security policies, data collection, data processing, model training, model deployment, system monitoring, incident management, and business continuity planning. The document aims to provide a comprehensive perspective on AI system security, outline threats to critical AI assets, and enable organizations to conduct AI security risk assessments.

- **[AI Safety Governance Framework](https://www.tc260.org.cn/upload/2024-09-09/1725849192841090989.pdf)** (National Technical Committee 260 on Cybersecurity of Standardization Administration of China (SAC/TC260; 全国网络安全标准化技术委员会), China)

  This framework presents a comprehensive strategy for AI safety governance, prioritizing risk management throughout AI's lifecycle. It identifies and addresses inherent risks in AI technologies, such as algorithmic bias, data security, and system vulnerabilities, as well as risks in AI applications, including cyberattacks and misinformation. The framework proposes coordinated efforts involving all stakeholders - developers, service providers, users, and governments - to ensure transparency, security, and ethical AI deployment. Emphasis is placed on international cooperation and the continuous improvement of governance mechanisms to safeguard both individual rights and national interests.

- **[AI Security Concerns in a Nutshell](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/Practical_Al-Security_Guide_2023.pdf)** (Federal Office for Information Security, Germany)

  This guide introduces key security concerns associated with AI systems, particularly focusing on attacks and defenses relevant to machine learning models. It outlines categories such as evasion attacks, information extraction, and backdoor attacks, emphasizing the importance of secure AI system design. With AI being used in critical sectors like healthcare and autonomous driving, the guide stresses the importance of defensive measures against malicious manipulation, especially when using pre-trained models or public datasets. The document aims to provide initial guidance for developers on securing AI systems without claiming to be exhaustive.

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

- **[GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/)** (OWASP, International)

  Published by the OWASP Gen AI Security Project on 22 January 2025, this guide describes what red teaming a generative AI system involves in practice. It covers model evaluation, implementation testing, infrastructure assessment and runtime behaviour analysis, and treats red teaming as a programme rather than a one-off exercise. The PDF downloads without registration.

- **[Inspect Framework](https://inspect.ai-safety-institute.org.uk/)** (UK AI Safety Institute, UK)

  Inspect,a framework for large language model evaluations created by the UK AI Safety Institute, provides many built-in components, including facilities for prompt engineering, tool usage, multi-turn dialog, and model graded evaluations. Extensions to Inspect (e.g. to support new elicitation and scoring techniques) can be provided by other Python packages.

- **[ISO/IEC CD 27090](https://www.iso.org/standard/56581.html)** (ISO, International)

  This document (still in draft status) offers guidance to organizations on managing security threats and failures in AI systems. It provides insights into the consequences of such threats throughout the AI lifecycle and offers strategies for detection and mitigation. The guidance is applicable to organizations of all sizes and sectors, including public and private companies, government agencies, and non-profits, that are involved in the development or use of AI systems.

- **[Managing Misuse Risk for Dual-Use Foundation Models (NIST AI 800-1 initial public draft)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd.pdf)** (National Institute of Standards and Technology (NIST), USA)

  Guidelines for improving the safety and security of dual-use foundation models, focusing on mitigating the risks of deliberate misuse. It addresses the evolving threats posed by foundation models, such as their potential to aid in the development of harmful technologies, cyberattacks, and other dangerous outputs. The guidelines emphasize managing misuse risks across the AI lifecycle, offering best practices for developers and organizations involved in foundation model development. The recommendations build upon the NIST AI Risk Management Framework, focusing on both technical and social factors influencing misuse.

- **[MITRE Adversarial Threat Landscape for AI Systems (ATLAS)](https://atlas.mitre.org/)** (MITRE Corporation, USA)

  MITRE's ATLAS is a knowledge base of adversarial tactics and techniques targeting AI systems, derived from real-world attacks and demonstrations by red teams. With the increasing adoption of AI, ATLAS highlights the unique risks, expanding attack surfaces, and vulnerabilities that traditional cyber defenses may not cover. Modeled after MITRE's ATT&CK framework, it provides valuable insights for security analysts, AI developers, and others involved in AI security, enabling effective threat assessments and red teaming. ATLAS also facilitates global collaboration through secure incident reporting and open-source tools to enhance AI threat mitigation strategies.

- **[Multilayer Framework for Good Cybersecurity Practices for AI](https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai)** (European Union Agency for Cybersecurity (ENISA), EU)

  A scalable, three-layer framework for cybersecurity practices in AI systems, addressing both general ICT security and AI-specific risks. Layer I covers foundational cybersecurity practices for ICT infrastructures hosting AI systems. Layer II introduces AI-specific security controls, addressing dynamic risks throughout AI’s lifecycle. Layer III provides sector-specific practices for high-risk AI applications, such as in health and energy. The framework integrates existing standards, legislation, and cybersecurity measures, aiming to build trust and enhance the security and resilience of AI systems across various sectors.

- **[OCCULT: Evaluating Large Language Models for Offensive Cyber Operation Capabilities](https://arxiv.org/abs/2502.15797)** (MITRE Corporation, USA)

  OCCULT is a framework designed to quantify the risks of LLMs when used in offensive cyber operations. Instead of red-teaming the model to see how it might fail, OCCULT is about assessing how an LLM itself could be weaponized by attackers or used as a “cyber agent.”

- **[OWASP AI Testing Guide](https://owasp.org/www-project-ai-testing-guide/)** (OWASP, International)

  A testing methodology for AI and LLM systems, with repeatable test cases spanning the application, model, infrastructure and data layers. It covers adversarial manipulation, information leakage, data poisoning, bias, hallucination, unsafe autonomy and model degradation. Version 1 was published on 26 November 2025 and is available as a PDF and as browsable documentation. Led by Matteo Meucci and Marco Morana.

- **[OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)** (OWASP, International)

  The OWASP LLM Top 10 provides a comprehensive list of the most critical security vulnerabilities in Large Language Model (LLM) applications. These vulnerabilities, such as prompt injections, training data poisoning, and insecure output handling, expose systems to risks including unauthorized access, privacy violations, and model theft. The guide aims to raise awareness, educate stakeholders, and offer remediation strategies to enhance the security of LLM systems, while mitigating potential risks in real-world applications. The goal is to improve the overall security posture of LLM deployments across industries.

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

- **[AgentDojo](https://github.com/ethz-spylab/agentdojo)**

  A dynamic environment for evaluating prompt injection attacks and defences against LLM agents, from ETH Zurich's SPY Lab with Invariant Labs. It ships user tasks and injection tasks so that attacks and defences can be measured on the same ground, and accompanies a paper in the NeurIPS 2024 datasets and benchmarks track.

- **[AI Prompt Fuzzer](https://github.com/PortSwigger/ai-prompt-fuzzer)**

  Burp Suite extension that brute-forces AI prompts straight from Intruder, easing integration of LLM testing into web-app pentest workflows.

- **[AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs)**

  This repository contains the challenges for the labs that were used in the course AI Red Teaming in Practice. The course was originally taught at Black Hat USA 2024.

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

- **[FuzzyAI](https://github.com/cyberark/FuzzyAI)**

  CyberArk’s coverage-guided fuzzer that auto-generates malicious prompts across 10+ attack families and logs jailbreak success rates. Ideal for CI red-team pipelines.

- **[Garak](https://docs.garak.ai/garak)**

  Garak is an open-source framework designed to identify vulnerabilities in Large Language Models (LLMs).

- **[Guardrails AI](https://github.com/guardrails-ai/guardrails)**

  YAML/Python DSL to validate or repair LLM outputs (regex, JSON Schema, semantic similarity, PII) and automatically re-ask on failure.

- **[Lakera PINT Benchmark](https://github.com/lakeraai/pint-benchmark)**

  The Prompt Injection Test (PINT) Benchmark provides a neutral way to evaluate the performance of a prompt injection detection system.

- **[LLM Guard](https://github.com/protectai/llm-guard)**

  Drop-in Python/REST library that redacts PII, blocks jailbreak strings, enforces token limits, detects policy violations. Ships with a CLI and Hugging Face model hub presets. Archived by its maintainer on 9 July 2026 and now read-only, so it receives no further updates.

- **[NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)**

  NVIDIA's open-source toolkit for adding programmable guardrails to LLM-based conversational systems. Rails are written in a dedicated modelling language and can hold a conversation to permitted topics, check inputs and outputs, and gate tool calls.

- **[Offensive ML Playbook](https://wiki.offsecml.com/Welcome+to+the+Offensive+ML+Playbook)**

  An amalgam of TTP's on different offensive ML attacks encompassing the ML supply chain and adversarial ML attacks. It is focused heavily on attacks that have code you can use to perform the attacks right away, rather than a database of research papers. (PoC or GTFO type logic).

- **[OpenPromptInjection](https://github.com/liu00222/Open-Prompt-Injection)**

  Open-source toolkit for attacks and defenses in LLM-integrated applications, which enables easy implementation, evaluation, and extension of attacks, defenses, and LLMs.

- **[Parley](https://github.com/dreadnode/Parley)**

  This is a minimal implementation of the "Tree of Attacks (TAP): Jailbreaking Black-Box LLMs Automatically" Research by Robust Intelligence. Last updated in February 2024.

- **[PoisonedRAG](https://github.com/sleeepeer/PoisonedRAG)**

  Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models

- **[promptfoo](https://github.com/promptfoo/promptfoo)**

  Command-line tool for testing prompts, agents and RAG pipelines, with a red-teaming mode that generates adversarial inputs and scans for vulnerabilities. Configuration is declarative and runs in CI alongside ordinary tests.

- **[Proof Pudding](https://github.com/moohax/Proof-Pudding)**

  Model extraction attack for ProofPoint's e-mail scoring system by stealing scored datasets (core/data/\*.csv) and creating a copy-cat model for abuse. Last updated in April 2020.

- **[Purple Llama](https://github.com/meta-llama/PurpleLlama)**

  Meta’s umbrella repo ships ready-to-use models plus “PromptGuard 2” jailbreak detector and an agent-focused firewall with code-safety scans. Covers risks (prompt injection, insecure code) that classic chatbot guardrails miss.

- **[PyRIT](https://github.com/microsoft/PyRIT)**

  Microsoft's Python Risk Identification Tool for generative AI: an automation framework for red teaming that supplies attack strategies, scores model responses and keeps conversation history across runs. Documentation, including installation and worked examples, is at microsoft.github.io/PyRIT. The repository moved from the Azure organisation to microsoft, and the old location is archived. MIT licence.

- **[Snyk Agent Scan](https://github.com/snyk/agent-scan)**

  Scanner that discovers agent components on a machine, including MCP servers, agents and skills, and checks them for prompt injections and known vulnerabilities. It started as Invariant Labs' mcp-scan and is now maintained by Snyk under the name agent-scan.

- **[tensor-man](https://github.com/dreadnode/tensor-man)**

  tensor-man is a utility to inspect, validate, sign and verify machine learning model files.

- **[TruLens](https://github.com/truera/trulens)**

  Instrumentation and eval library (OpenTelemetry style) that traces LLM chains, scores outputs with configurable feedback functions, and stores runs for comparison.

- **[Vigil-LLM](https://github.com/deadbits/vigil-llm)**

  Alpha-stage scanner and REST API that applies a configurable chain of detectors to find prompt injections, jailbreaks, and other threats in prompts/responses. Last updated in January 2024.

- **[WallBreaker](https://github.com/JailbrokenAI/wallbreaker)**

  Command-line harness for automated LLM red teaming, built around an agent loop that keeps refining prompts against a target until it succeeds or hands back to the operator. Bundles the HarmBench behaviour benchmark, the L1B3RT4S jailbreak library and the Parseltongue transform set, and implements published techniques including PAIR, TAP and Crescendo. Needs API keys for the attacking, target and judge models. AGPL-3.0, first released in June 2026.

## Guides and Tutorials

Provided for informational purposes only. Read, use, and live at your own risk.

- **[Defending Against Vision Prompt Injection Attacks in Large Language Models](https://blog.roboflow.com/gpt-4-vision-prompt-injection/)**

  This article explores the concept of Vision Prompt Injection vulnerabilities in Large Language Models (LLMs) with image processing capabilities, where malicious instructions can be embedded within images, even invisibly, to make the model perform unauthorized actions or extract sensitive data. The article showcases real-life examples of Vision Prompt Injection attacks and discusses the challenges and potential strategies for defending against them as businesses start to build applications using multimodal LLMs.

- **[Embrace the Red: Machine Learning Attack Series](https://embracethered.com/blog/posts/2020/machine-learning-attack-series-overview/)**

  A series of blog posts focused on machine learning from a red teaming and security testing perspective. The author covers various topics, including machine learning basics, building a machine learning system called Husky AI, threat modeling, practical attacks, and defenses.

- **[Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning)**

  This document tabulates both intentional and unintentional failure modes in machine learning systems. Intentional failures are caused by an active adversary attempting to subvert the system to attain their goals, while unintentional failures occur when an ML system produces a formally correct but completely unsafe outcome. The document aims to provide a common vocabulary for engineers, lawyers, and policymakers to discuss these issues and build solutions.

- **[PIPE - Prompt Injection Primer for Engineers](https://github.com/jthack/PIPE)**

  This guide, by Joseph Thacker, assists developers in creating secure AI-powered applications and features by helping them understand the actual risks of prompt injection. Last updated in August 2023.

- **[Prompt Injection Attacks Handbook](https://www.lakera.ai/ai-security-guides/prompt-injection-attacks-handbook)**

  A practical handbook on prompt injection: attack techniques, real-world examples, and the defensive measures available against them.

- **[Silent Sabotage: Hijacking Safetensors conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)**

  This article demonstrates how an attacker could compromise the Hugging Face Safetensors conversion service and its associated bot to send malicious pull requests and hijack models submitted through the conversion service. The authors show how it's possible to persist malicious code inside the service, allowing models to be automatically hijacked during conversion, potentially leading to a widespread supply chain attack.

- **[The Beginner's Guide to Visual Prompt Injections: Invisibility Cloaks, Cannibalistic Adverts, and Robot Women](https://www.lakera.ai/blog/visual-prompt-injections)**

  This article explores the concept of visual prompt injection, a vulnerability in Large Language Models (LLMs) with image processing capabilities, where malicious instructions embedded within images can make the model perform unintended actions. The article showcases real-life examples of visual prompt injection attacks, such as invisibility cloaks, robot disguises, and ad suppression, and highlights the need for robust security measures as businesses adopt multimodal models.

- **[The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)**

  Simon Willison's post from 16 June 2025 naming the three properties that together make an AI agent exploitable: access to private data, exposure to untrusted content, and the ability to communicate externally. It is a short, concrete account of how prompt injection turns into data exfiltration once an agent holds tools, and the phrase has become common shorthand when reviewing agent designs.

- **[The Waluigi Effect (mega-post)](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post)**

  The Waluigi Effect is a phenomenon in large language models (LLMs) where training an LLM to satisfy a desirable property makes it easier to elicit the opposite behavior. Using Simulator Theory, the author argues that LLMs produce a superposition of well-behaved "luigi" and misbehaving "waluigi" simulacra, suggesting that techniques like RLHF may fail to eliminate deceptive waluigis and could make chatbots more misaligned. This has important implications for AI security, as it highlights the challenge of aligning LLMs and suggests that misalignment risks could increase with model capability. Understanding the Waluigi Effect is crucial for developing robust alignment strategies to prevent negative outcomes and existential risks.

- **[Threat Modeling AI/ML Systems and Dependencies](https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml)**

  This document provides guidance on threat enumeration and mitigation specific to the AI and Machine Learning space. It supplements existing SDL threat modeling practices and is intended to be used as a reference during security design reviews of products/services interacting with or taking dependencies on AI/ML-based services, as well as products/services being built with AI/ML at their core.

- **[Using GPT-Eliezer against ChatGPT Jailbreaking](https://www.alignmentforum.org/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking)**

  This article proposes using a separate language model, acting as a suspicious AI safety engineer named "Eliezer Yudkowsky," to evaluate prompts before sending them to ChatGPT. The goal is to prevent jailbreaking attempts and filter out dangerous prompts that could lead to harmful or illegal behavior from the AI chatbot.

## Courses

Do your own research and due diligence before enrolling.

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

- **[Generative AI for Cybersecurity](https://codered.eccouncil.org/course/generative-ai-for-cybersecurity-course)** (3-Advanced, Above 5 hours)

  This course dives into Generative AI and LLMs in cybersecurity, offering an understanding of their architecture, technology, and security implications. With hands-on experience using open-source models for cyber defense, participants learn to identify and mitigate AI-related security risks. It requires knowledge of cybersecurity, AI/ML principles, and programming in Python. The course covers LLM architecture, technology stacks, security considerations, and practical applications, empowering learners to enhance their organization's cyber resilience.

- **[Generative AI for Security Professionals](https://www.pluralsight.com/paths/generative-ai-and-cybersecurity)** (1-Beginner, Under 5 hours)

  This learning path, comprised of 4 courses spanning 2 hours, delves into how Generative AI can revolutionize cybersecurity. It covers the integration of Generative AI in security operations, addressing data privacy, security risks, and how to harness Generative AI's potential effectively. The courses explore the balance between enhancing security measures and the inherent risks of Generative AI, offering insights into leveraging AI for both offensive and defensive cybersecurity operations.

- **[Generative AI in Cybersecurity](https://www.gsdcouncil.org/certified-generative-ai-in-cybersecurity)** (3-Advanced, Above 5 hours)

  The Generative AI in Cybersecurity Certification by GSDC is designed for cybersecurity professionals to master the use of Generative AI in detecting and mitigating cyber threats. It covers generative models, ethical considerations, and AI application skills, aiming to enhance digital defenses and provide a competitive edge in cybersecurity. The program requires programming knowledge, involves a 60-minute exam, and offers a deep dive into Generative AI fundamentals, cybersecurity basics, GANs, VAEs, and ethical considerations in AI.

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

## Communities

Join at your own risk. Lurk at your own risk. Interact at your own risk.

- **[AI security](https://www.linkedin.com/groups/8196854/)** (Individual, LinkedIn)

- **[AI Village](https://aivillage.org/)** (Community, Discord)

  A hacker community for AI security that runs the AI Village at DEF CON along with workshops, capture-the-flag events and red-team exercises through the year. It describes itself as bringing hackers, researchers, engineers and policymakers together through hands-on AI security education. Day-to-day conversation happens on its Discord.

- **[CSA AI Safety Working Group](https://cloudsecurityalliance.org/research/working-groups/ai-safety)** (Nonprofit, Working group)

  A Cloud Security Alliance research working group building best practices for AI, with an initial focus on generative AI. Anyone can join, and the time commitment ranges from reviewing a near-final publication to co-authoring new research. Output is published as free CSA papers.

- **[MLSecOps](https://mlsecops.slack.com/join/shared_invite/zt-24f8mmm45-Qc9qfZVxzBL4J5vcuLjaVw)** (Company, Slack)

- **[OWASP Gen AI Security Project](https://genai.owasp.org/contribute/)** (Nonprofit, Slack)

  The working community behind the OWASP Top 10 for LLM applications and the project's other generative AI security output. Discussion happens in the OWASP Slack workspace, in channels such as #project-top10-for-llm and #team-llm-discuss, with regular open meetings. OWASP membership is not required to take part.

## Links

Useful references that do not fit neatly anywhere else on the map.

- **[AI Incident Database](https://incidentdatabase.ai/)**

  The AI Incident Database is dedicated to indexing the collective history of harms or near harms realized in the real world by the deployment of artificial intelligence systems. Like similar databases in aviation and computer security, the AI Incident Database aims to learn from experience so we can prevent or mitigate bad outcomes.

- **[Cybersecurity Risks of AI-Generated Code](https://cset.georgetown.edu/publication/cybersecurity-risks-of-ai-generated-code/)**

  This issue brief explores the cybersecurity risks of AI-generated code, highlighting challenges posed by large language models used in software development. The report categorizes risks into three areas: insecure code generation, model vulnerabilities, and downstream impacts like feedback loops in AI training. Experimental findings show that nearly half of the evaluated code snippets from five prominent LLMs contained impactful bugs, emphasizing the importance of comprehensive security assessments. It also discusses the unequal risk distribution across organizations, the need for multi-stakeholder mitigation strategies, and enhancements in existing cybersecurity frameworks to address these novel challenges.

- **[NSA Artificial Intelligence Security Center](https://www.nsa.gov/AISC/)**

  The AISC will be a key part of NSA's cybersecurity mission, with the goal to defend the Nation's AI through Intel-Driven collaboration with industry, academia, the IC, and other government partners.

- **[OECD AI Incidents Monitor](https://oecd.ai/en/incidents)**

  The OECD AI Incidents Monitor (AIM) documents AI incidents to help policymakers, AI practitioners, and all stakeholders worldwide gain valuable insights into the incidents and hazards that concretise AI risks. Over time, AIM will help to show patterns and establish a collective understanding of AI incidents and their multifaceted nature and serve as an important tool for trustworthy AI.

- **[OWASP LLM Security Verification Standard](https://owasp.org/www-project-llm-verification-standard/)**

  The primary aim of the OWASP Large Language Model Security Verification Standard (LLMSVS) Project is to provide an open security standard for systems which leverage artificial intelligence and Large Language Models. The standard provides a basis for designing, building, and testing robust LLM backed applications, including architectural, model lifecycle, model training, model operation and integration, model storage and monitoring concerns.

- **[Policy Alignment on AI Transparency - Partnership on AI](https://partnershiponai.org/policy-alignment-on-ai-transparency/)**

  Partnership on AI’s Policy Alignment on AI Transparency conducts a comparative analysis of eight leading policy frameworks for foundation models, with a particular focus on documentation requirements, which are a critical lever for achieving transparency and safety.

## About this repository

The site is the source of truth. This README is generated by [`build_readme.py`](build_readme.py) from the site's `data/*.json` files, and a [monthly workflow](.github/workflows/rebuild.yml) rebuilds it, committing only when something changed. Do not edit README.md by hand: the next rebuild would overwrite your change.

To suggest an entry or a correction, [open an issue](https://github.com/sambucci/ai-security-ninja/issues) with a source. Accepted changes land on the site first and flow here at the next rebuild. An entry is amended or removed when a source shows it should be, never on a single failed link.

Kept by [Luca Sambucci](https://www.sambucci.com), founder of [Noctive Security](https://www.noctivesecurity.com). Curated through an agent, kept free of hype.

Text licensed under [CC BY 4.0](LICENSE); `build_readme.py` is MIT.
