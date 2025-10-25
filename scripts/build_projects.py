from __future__ import annotations

from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent

PROJECTS = [
    {
        "id": 1,
        "slug": "01-pandemic-pulse",
        "title": "Pandemic Pulse — Digital Biosurveillance",
        "subtitle": "Digital exhaust early warning platform detecting bio-threats weeks before official alerts.",
        "hero_image": "1.1.pandemic-pulse-dashboard.png",
        "hero_alt": "Dashboards from the Pandemic Pulse biosurveillance platform",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Built a national biosurveillance platform fusing social, search, and news data.",
                    "Designed to surface weak outbreak signals weeks before official alerts.",
                    "Delivered intuitive analyst dashboards for NBIC, DHS, and local partners.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Conventional surveillance lagged on novel threats and ambiguous digital clues.",
                    "Teams faced noisy, fragmented feeds scattered across disparate sources.",
                    "Agencies needed credible early warnings without overwhelming analysts.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Streaming pipelines fused Twitter, Google Trends, and HealthMap feeds.",
                    "Tiered NLP triaged signals by pathogen priority, source trust, and location.",
                    "Interactive maps and timelines framed alerts with actionable context.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Retrospective tests flagged Boston bombing and Hepatitis A anomalies early.",
                    "Won DHS Hidden Signals Challenge, shaping national preparedness plans.",
                    "Methods seeded later COVID-19 partnerships with Meta and Google.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as principal architect, coordinating DHS, NBIC, and academic teams.",
                    "Built AWS pipelines with Python NLP, anomaly detection, and geolocation.",
                    "Led dashboard UX to speed analyst review and response playbooks.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "1.2.pandemic-pulse-system-architecture.png",
                "type": "image",
                "alt": "Pandemic Pulse system architecture diagram",
                "caption": "System architecture showing multi-engine streaming pipeline.",
            }
        ],
        "card": {
            "description": "Unified digital exhaust to detect novel outbreaks weeks earlier.",
            "role": "Role: Principal investigator & systems architect",
            "focus": "Focus: Weak-signal detection, NLP pipelines, real-time dashboards",
        },
    },
    {
        "id": 2,
        "slug": "02-ml-allergy",
        "title": "ML-Allergy — Food Allergy Risk Stratification",
        "subtitle": "Composite biomarker decision support predicting oral food challenge outcomes for pediatric patients.",
        "hero_image": "2.1.Allergy-AI-system-architecture.png",
        "hero_alt": "ML-Allergy system architecture diagram",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Developed ML-Allergy decision support to stratify pediatric food allergy risk.",
                    "Combined biomarkers, histories, and machine learning scores for clinic visits.",
                    "Embedded outputs within Boston Children’s allergy workflows.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Single tests left families stuck in diagnostic gray zones for years.",
                    "Inconclusive results triggered unnecessary avoidance or risky challenges.",
                    "Clinicians required interpretable predictions aligned with existing EHR data.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Curated composite features across IgE, SPT, history, and demographics.",
                    "Trained regularized classifiers on retrospective oral challenge outcomes.",
                    "Delivered clear risk tiers and guidance inside clinic decision reports.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Improved triage for patients needing supervised challenges versus observation.",
                    "Enabled earlier reintroduction for confidently low-risk children.",
                    "Provided blueprint for expanding ML biomarker panels to new allergens.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led collaboration with hospital allergy clinics and informatics partners.",
                    "Applied Python, scikit-learn, and careful feature engineering for transparency.",
                    "Designed clinician-friendly reports with uncertainty cues and next steps.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Composite biomarker ML panel predicting oral food challenge outcomes.",
            "role": "Role: Clinical data scientist",
            "focus": "Focus: EHR integration, model interpretability, clinician workflows",
        },
    },
    {
        "id": 3,
        "slug": "03-pediatric-vision-ai",
        "title": "Pediatric Vision AI — Early Screening",
        "subtitle": "Computer vision and analytics delivering rapid pediatric vision screening in primary care settings.",
        "hero_image": "3.1.Vision-ninja-gaze-and-optotypes.png",
        "hero_alt": "Prototype interface illustrating pediatric gaze tracking",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Created computer vision workflows for rapid pediatric vision screening.",
                    "Partnered with ophthalmology teams to align hardware, analytics, and workflow.",
                    "Planned path from prototype to clinic-ready screening toolkit.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Traditional screenings miss amblyopia because tools are slow or subjective.",
                    "Primary care sites lack specialized equipment or trained vision technicians.",
                    "Capture quality varies with lighting, movement, and young patient behavior.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Engineered gaze tracking and optotype detection using embedded cameras.",
                    "Standardized capture protocols with simple calibration for non-specialist staff.",
                    "Combined on-device guidance with cloud analytics for reliable scoring.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Cut screening time while improving early amblyopia detection confidence.",
                    "Enabled deployment beyond specialty clinics, expanding access to early screening.",
                    "Aligned stakeholders on regulatory, reimbursement, and commercialization milestones.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led product strategy across clinicians, engineers, and data scientists.",
                    "Applied Python computer vision, embedded firmware integration, and UX testing.",
                    "Authored validation plans linking algorithm metrics to clinical endpoints.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Computer vision screening tool for pediatric amblyopia detection.",
            "role": "Role: Product & analytics lead",
            "focus": "Focus: Computer vision, embedded hardware, clinical validation",
        },
    },
    {
        "id": 4,
        "slug": "04-project-apollo-icu-hypoxemia",
        "title": "ICU Hypoxemia Prediction — Project Apollo",
        "subtitle": "Bedside machine learning forecasts hypoxemia events minutes ahead for ICU clinicians.",
        "hero_image": "4.1.icu-hypoxemia-alert-console.png",
        "hero_alt": "ICU hypoxemia prediction console highlighting rising risk",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Co-led Project Apollo to forecast ICU hypoxemia minutes before onset.",
                    "Merged streaming vitals, labs, and clinician notes into risk scores.",
                    "Delivered bedside displays with prioritized alerts and playbooks.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Hypoxemia escalates quickly, leaving clinicians minimal reaction time.",
                    "Existing monitors triggered alarms without actionable prediction or triage.",
                    "Critical care teams demanded interpretable insights to trust automation.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Built time-series models on high-frequency ventilator and waveform data.",
                    "Integrated clinician feedback to tune thresholds and suppress noisy alerts.",
                    "Designed bedside UI with escalation cues, tasks, and documentation hooks.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Enabled earlier interventions that reduced severe desaturation incidents.",
                    "Standardized response workflows across respiratory therapists and physicians.",
                    "Established governance patterns for deploying ML at the bedside.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as principal product owner bridging analytics and ICU leadership.",
                    "Used Python, Spark, and streaming feature pipelines for real-time inference.",
                    "Led change management, training, and monitoring for safe adoption.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Delivered a bedside platform forecasting critical oxygen drops minutes in advance.",
            "role": "Role: Principal product owner",
            "focus": "Focus: Time-series forecasting, clinician-in-the-loop design",
        },
    },
    {
        "id": 5,
        "slug": "05-maternal-infant-integration",
        "title": "Maternal-Infant Health Data Integration",
        "subtitle": "Linked maternal and infant datasets to close service gaps across public health and social care.",
        "hero_image": "5.1.mother-infant-diad-infant-clinical-data-elements-mapping-USCDI.png",
        "hero_alt": "Maternal-infant clinical data elements mapped to USCDI",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Unified maternal and infant data across clinical, public health, and social systems.",
                    "Built linked dashboards for program managers and frontline navigators.",
                    "Drove policy alignment for statewide maternal-infant service coordination.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Critical maternal-infant data were siloed across hospitals, Medicaid, and social programs.",
                    "Slow data sharing hindered timely interventions for high-risk dyads.",
                    "Leaders lacked unified views to target support and funding.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Designed interoperable data models mapping clinical, claims, and social determinants.",
                    "Stood up secure pipelines with governance and consent guardrails.",
                    "Developed dashboards highlighting care gaps, eligibility, and referrals.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Improved identification of high-risk dyads needing intensive follow-up.",
                    "Informed statewide policy updates on perinatal data-sharing agreements.",
                    "Enabled partners to evaluate programs with near real-time metrics.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as program director aligning agencies and hospital systems.",
                    "Applied SQL, Python, and governance frameworks for multi-source integration.",
                    "Facilitated design sprints translating analytics into actionable workflows.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "5.2.mother-infant-diad-infant-supportive-data-elements-mapping-USCDI.pdf",
                "type": "pdf",
                "alt": "Supportive maternal-infant data mapped to USCDI",
                "caption": "Supportive data elements aligned to national interoperability standards.",
            },
            {
                "src": "5.3.mother-infant-diad-synthetic-data-table.png",
                "type": "image",
                "alt": "Synthetic maternal-infant record sample",
                "caption": "Synthetic dyad record illustrating linked clinical and social features.",
            },
            {
                "src": "5.4.mother-infant-diad-dashboard-prototype.png",
                "type": "image",
                "alt": "Maternal-infant data integration dashboard",
                "caption": "Prototype dashboard highlighting care coordination opportunities.",
            },
        ],
        "card": {
            "description": "Connected siloed health, social, and public data to support maternal-infant care.",
            "role": "Role: Program director",
            "focus": "Focus: Interoperability, community health analytics, policy impact",
        },
    },
    {
        "id": 6,
        "slug": "06-global-covid-impact-monitoring",
        "title": "Global COVID-19 Impact Monitoring",
        "subtitle": "Scaled the Facebook UMD-CTIS survey to deliver daily global COVID-19 situational awareness.",
        "hero_image": "6.1.covid-CTIS-banchmarking.png",
        "hero_alt": "Global benchmarking of Facebook UMD-CTIS survey signals",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Led global expansion of the Facebook UMD-CTIS COVID-19 survey program.",
                    "Delivered daily dashboards benchmarking symptoms, behaviors, and policy metrics.",
                    "Partnered with academia and governments for actionable insights.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Official reporting lagged across countries, obscuring emerging hotspots.",
                    "Inconsistent data quality complicated cross-country comparisons.",
                    "Leaders needed privacy-conscious ways to leverage social survey data.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Scaled sampling, weighting, and translation for billions of daily impressions.",
                    "Built analytics comparing survey signals against public health benchmarks.",
                    "Implemented stringent privacy and quality controls for partners and respondents.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Provided near real-time metrics adopted by WHO and national agencies.",
                    "Validated survey indicators against case data to prove policy relevance.",
                    "Guided resource allocation and messaging campaigns through shared dashboards.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as global survey co-lead with Meta and university partners.",
                    "Applied Python, R, and Bayesian weighting for rapid global analytics.",
                    "Coordinated localization, QA, and stakeholder briefings across continents.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "6.2.covid-CTIS-ML-model-features.png",
                "type": "image",
                "alt": "Features informing COVID-19 survey models",
                "caption": "Feature pipeline supporting predictive models and data quality checks.",
            }
        ],
        "card": {
            "description": "Scaled the 114-country Facebook UMD-CTIS survey for daily COVID-19 intelligence.",
            "role": "Role: Global survey program co-lead",
            "focus": "Focus: Participatory epidemiology, real-time analytics",
        },
    },
    {
        "id": 7,
        "slug": "07-bangkok-vaccine-insights",
        "title": "Bangkok Vaccine Hesitancy Insights",
        "subtitle": "Delivered weekly vaccine sentiment intelligence for Bangkok’s third COVID-19 wave.",
        "hero_image": "7.1.CITS-Thiland-premedical-conditon.png",
        "hero_alt": "Bangkok vaccine concerns segmented by pre-existing conditions",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Produced vaccine sentiment intelligence for Bangkok leadership.",
                    "Blended survey data with digital conversation monitoring.",
                    "Delivered weekly briefs guiding messaging and outreach.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Hesitancy surged amid third-wave misinformation and limited supply.",
                    "Officials lacked timely insight into community concerns and motivators.",
                    "Needed to identify trusted messengers for targeted outreach.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Fielded rapid-turn surveys capturing risk factors and motivators.",
                    "Analyzed digital chatter to surface prevalent questions and rumors.",
                    "Segmented populations to tailor messaging by concern and trust source.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Guided campaigns addressing safety fears and chronic condition worries.",
                    "Identified trusted local messengers for vaccine outreach.",
                    "Directed resources toward high-hesitancy districts and groups.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led analytics collaboration with Bangkok Metropolitan Administration.",
                    "Applied Python NLP, survey weighting, and geospatial segmentation.",
                    "Produced executive dashboards and weekly narrative briefs.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "7.2.CITS-Thiland-trusted-source-of-info.png",
                "type": "image",
                "alt": "Trusted vaccine information sources in Bangkok",
                "caption": "Trusted messengers shaped outreach prioritization by district.",
            }
        ],
        "card": {
            "description": "Provided weekly intelligence on COVID-19 vaccine sentiment for Bangkok’s third wave.",
            "role": "Role: Lead data scientist",
            "focus": "Focus: Urban health analytics, behavior change",
        },
    },
    {
        "id": 8,
        "slug": "08-federated-npi-behavior",
        "title": "Federated NPI Behavior Study",
        "subtitle": "Privacy-preserving analytics measuring masking and distancing behaviors across the United States.",
        "hero_image": "8.1.Accute-Respiratory-Infection-Google-Health-Study-Launch.png",
        "hero_alt": "Google Health federated NPI study launch graphic",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Partnered with Google Health on a federated study of NPI behaviors.",
                    "Tracked masking and distancing alongside vaccination milestones nationwide.",
                    "Delivered privacy-preserving analytics across participating health systems.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Behavioral data was fragmented and sensitive across institutions.",
                    "Needed to monitor NPIs without centralizing identifiable information.",
                    "Stakeholders required trusted analytics to guide reopening decisions.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Implemented federated querying with differential privacy safeguards.",
                    "Linked mobility, survey, and vaccination data to contextualize behaviors.",
                    "Built dashboards summarizing adherence trends and intervention impact.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Provided a national view of NPI adoption at regional scales.",
                    "Informed policymakers on timing for easing or reinforcing measures.",
                    "Demonstrated scalable privacy-preserving analytics for future collaborations.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as epidemiology and analytics lead across partner institutions.",
                    "Applied TensorFlow Federated, Python, and secure aggregation pipelines.",
                    "Led privacy reviews, stakeholder reporting, and interpretation sessions.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "8.2.federated-analytics-and-differential-privacy-preserved-data-collection.png",
                "type": "image",
                "alt": "Federated analytics and differential privacy workflow",
                "caption": "Federated pipeline balancing utility with strong privacy protections.",
            },
            {
                "src": "8.3.participant-engaguement-in-mobility-based-NPI-intervention.png",
                "type": "image",
                "alt": "Participant engagement in NPI interventions",
                "caption": "Engagement metrics informed outreach strategies over the study period.",
            },
        ],
        "card": {
            "description": "Partnered with Google Health to deploy a privacy-preserving NPI behavior cohort.",
            "role": "Role: Epidemiology & analytics lead",
            "focus": "Focus: Federated analysis, differential privacy",
        },
    },
    {
        "id": 9,
        "slug": "09-covid-trial-equity",
        "title": "COVID-19 Trial Leadership Equity",
        "subtitle": "Benchmarked gender representation across US COVID-19 clinical trial leadership teams.",
        "hero_image": "9.1.clinical-trial-leadership-gender-by-disease.png",
        "hero_alt": "Gender representation across COVID-19 clinical trial leadership",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Audited thousands of US COVID-19 trial leadership rosters.",
                    "Benchmarked gender representation against other disease areas.",
                    "Linked leadership diversity with participant representation concerns.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Rapid trial launches lacked oversight on leadership equity.",
                    "Historic gender gaps risked repeating in urgent COVID-19 research.",
                    "Needed transparent metrics to hold institutions accountable.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Curated national trial registry, publication, and investigator datasets.",
                    "Used NLP to identify leadership roles and infer gender representation.",
                    "Built dashboards and briefs comparing specialties and sponsors.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Highlighted underrepresentation of women relative to other disease areas.",
                    "Prompted discussions with NIH and academic partners on inclusion goals.",
                    "Provided methodology for monitoring equity in future clinical studies.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as principal investigator guiding analytic design and narrative.",
                    "Applied Python NLP, entity resolution, and statistical benchmarking.",
                    "Engaged policy stakeholders to translate findings into actions.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "9.2.clinical-trial-leadership-study-selection.png",
                "type": "image",
                "alt": "Study selection workflow for clinical trial leadership analysis",
                "caption": "Study selection pipeline ensured comprehensive, comparable trial coverage.",
            }
        ],
        "card": {
            "description": "Audited gender representation across thousands of US COVID-19 trials.",
            "role": "Role: Principal investigator",
            "focus": "Focus: Clinical data mining, equity analytics",
        },
    },
    {
        "id": 10,
        "slug": "10-variant-vaccine-effectiveness",
        "title": "Variant-Responsive Vaccine Effectiveness",
        "subtitle": "Rapid survey-based pipeline tracking vaccine effectiveness shifts across global variants.",
        "hero_image": "10.1.covid-vaccine-effectiveness-against-mild-vs-severe-illness.png",
        "hero_alt": "Vaccine effectiveness against mild versus severe illness",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Built survey-based models to estimate vaccine effectiveness as variants emerged.",
                    "Leveraged global Facebook survey data and case trajectories.",
                    "Delivered country dashboards for low- and middle-income partners.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Effectiveness data lagged in many regions during Delta and Omicron waves.",
                    "Clinical studies were scarce in low-resource settings.",
                    "Decision-makers needed quick signals on waning protection.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Modeled self-reported symptoms and vaccination status to infer effectiveness.",
                    "Used Bayesian updating to track shifts as new variants spread.",
                    "Automated reporting with rigorous quality checks across dozens of countries.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Flagged early declines prompting booster planning in partner nations.",
                    "Supported WHO and NGOs with insights for LMIC policy decisions.",
                    "Showcased survey-based VE monitoring for future variant surveillance.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as study architect coordinating Meta, academia, and global partners.",
                    "Applied Python, Stan, and reproducible pipelines for rapid iteration.",
                    "Led validation comparing outputs with available clinical benchmarks.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "10.2.covid-vaccine-effectiveness-change-from-delta-to-omnicron.png",
                "type": "image",
                "alt": "Change in vaccine effectiveness from Delta to Omicron",
                "caption": "Variant comparison chart informed timing of booster recommendations.",
            }
        ],
        "card": {
            "description": "Built a rapid estimation pipeline using global survey data to quantify vaccine performance shifts.",
            "role": "Role: Study architect",
            "focus": "Focus: Survey-based VE modeling, global health",
        },
    },
    {
        "id": 11,
        "slug": "11-dns-command-control-detection",
        "title": "Cybersecurity — DNS Command-and-Control Detection",
        "subtitle": "Real-time DNS analytics pipeline detecting covert malware command-and-control traffic.",
        "hero_image": "11.1.Cybersecurity.Detect-and-control-channel-in-DNS-Logs.image.png",
        "hero_alt": "Architecture for DNS command-and-control detection",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Designed streaming DNS analytics to surface covert C2 communications.",
                    "Built microservices pipeline enriching logs with threat intelligence context.",
                    "Delivered alerting dashboards for security operations teams.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Attackers hide command channels inside ordinary DNS traffic.",
                    "Massive DNS volume overwhelms manual triage and review.",
                    "Slow detection leaves malicious domains active for weeks.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Built Kafka-backed ingestion with GeoIP and WHOIS enrichment.",
                    "Applied short- and long-window anomaly detection for fast and stealthy tunnels.",
                    "Integrated threat intel feeds and automated multi-channel alert routing.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Cut attacker dwell time by triggering near real-time DNS alerts.",
                    "Improved detection accuracy across bursty and low-and-slow behaviors.",
                    "Shared new indicators with the broader security community.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led architecture spanning data engineering and security operations.",
                    "Used Python, Kafka, Elastic, and containerized microservices.",
                    "Coordinated SOC workflows, knowledge base updates, and dashboard UX.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "11.1.Cybersecurity.Detect-and-control-channel-in-DNS-Logs.image.pdf",
                "type": "pdf",
                "alt": "Detailed DNS C2 detection system design",
                "caption": "Detailed system blueprint shared with security operations teams.",
            }
        ],
        "card": {
            "description": "Built streaming DNS analytics to detect covert malware command channels.",
            "role": "Role: Lead security analytics architect",
            "focus": "Focus: Streaming detection, threat intelligence, SOC enablement",
        },
    },
    {
        "id": 12,
        "slug": "12-foodborne-twitter-surveillance",
        "title": "Foodborne-1 — Twitter Surveillance",
        "subtitle": "Twitter-driven foodborne illness surveillance boosting citizen reporting and inspections.",
        "hero_image": "12.1.foodborne-illness-tweet-detailed.png",
        "hero_alt": "Tweet flagged by the HealthMap foodborne dashboard",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Built the HealthMap foodborne dashboard to monitor illness tweets.",
                    "Automated classification to flag likely food poisoning incidents.",
                    "Linked social signals to official reporting workflows.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Foodborne illness is widely underreported through traditional channels.",
                    "Manual reporting is cumbersome, delaying inspections and interventions.",
                    "Health departments lacked timely intelligence on emerging outbreaks.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Streamed tweets with geolocation inference and symptom keyword filters.",
                    "Trained SVM models to highlight credible illness reports.",
                    "Sent rapid response links prompting citizens to file official complaints.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Boosted official reports from communities that rarely called hotlines.",
                    "Accelerated targeted inspections uncovering serious violations sooner.",
                    "Established a blueprint for digital public health engagement.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led solution design with city health departments and HealthMap engineers.",
                    "Applied Python NLP, geocoding, and dashboard development.",
                    "Coordinated inspector training and response protocols.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "12.2.foodborne-illness-surveillance-using-twitter.png",
                "type": "image",
                "alt": "Foodborne illness surveillance dashboard",
                "caption": "Dashboard view guiding inspectors to likely outbreak clusters.",
            }
        ],
        "card": {
            "description": "Created a Twitter-monitoring dashboard that converts tweets into actionable food safety reports.",
            "role": "Role: Public health data scientist",
            "focus": "Focus: Digital epidemiology, rapid response workflows",
        },
    },
    {
        "id": 13,
        "slug": "13-foodborne-yelp-disparities",
        "title": "Foodborne-2 — Reporting Disparities via Yelp",
        "subtitle": "Yelp review mining revealed inequities in foodborne illness reporting across communities.",
        "hero_image": "13.1.correlation-between-count-of-yelp-sick-reports-and-variables.png",
        "hero_alt": "Correlation between Yelp illness reports and community indicators",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Analyzed Yelp reviews to uncover disparities in food poisoning reporting.",
                    "Connected digital complaints with demographic and socioeconomic indicators.",
                    "Equipped public health agencies with insights on underreporting communities.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Official complaint data skewed toward certain demographics.",
                    "Underreporting obscured hotspots in vulnerable neighborhoods.",
                    "Needed to quantify digital reporting gaps to target outreach.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Processed 1.5 million Yelp reviews with NLP to flag illness narratives.",
                    "Linked findings with census, climate, and inspection datasets.",
                    "Modeled reporting disparities across neighborhoods and sociodemographics.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Revealed communities underrepresented in official complaint systems.",
                    "Informed equity-focused outreach and education strategies.",
                    "Extended digital surveillance beyond social media into consumer reviews.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led analytical design with epidemiologists and city partners.",
                    "Applied Python NLP, statistical modeling, and data integration.",
                    "Delivered equity dashboards and policy briefings.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Mined Yelp reviews to expose who reports foodborne illness—and who gets overlooked.",
            "role": "Role: Lead data scientist",
            "focus": "Focus: Health equity analytics, natural language processing",
        },
    },
    {
        "id": 14,
        "slug": "14-global-mobility-mapping",
        "title": "Mapping Global Human Mobility",
        "subtitle": "Analyzed anonymized Google location data to reveal worldwide movement patterns and disparities.",
        "hero_image": "14.1.global-human-mobility-map.png",
        "hero_alt": "Global map of human mobility patterns",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Mapped global human mobility with anonymized Google Location data.",
                    "Characterized travel patterns across income levels and regions.",
                    "Released an open dataset for researchers and policymakers.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Global mobility data was historically sparse and inconsistent.",
                    "Difficult to compare movement across countries with limited records.",
                    "Needed privacy-preserving methods for sensitive location data.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Processed billions of pings into trips using a standardized S2 grid.",
                    "Applied differential privacy thresholds before publishing flows.",
                    "Modeled travel typologies and scaling laws across contexts.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Produced the first comprehensive mobility map covering 2.9 billion people.",
                    "Revealed stark disparities in travel distance across income levels.",
                    "Enabled epidemic modeling and infrastructure planning worldwide.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Collaborated with Google researchers and academic epidemiologists.",
                    "Used Python, R, and cloud pipelines for large-scale geospatial analysis.",
                    "Led interpretation and publication of insights for cross-sector partners.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Mapped global variation in human mobility using anonymized Google location history.",
            "role": "Role: Data science co-author",
            "focus": "Focus: Geospatial analytics, privacy engineering",
        },
    },
    {
        "id": 15,
        "slug": "15-gun-violence-platform",
        "title": "Gun Violence Surveillance Platform",
        "subtitle": "Real-time public platform integrating news, social, and search data on US gun violence.",
        "hero_image": "15.1.gunviolence-map-dashboard-views.png",
        "hero_alt": "Gun violence map dashboard views",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Developed a public gun violence surveillance platform aggregating multi-source data.",
                    "Combined Twitter, news, and search insights for situational awareness.",
                    "Delivered interactive maps and analytics for communities and policymakers.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Official gun violence data is delayed and fragmented.",
                    "Communities lacked accessible, real-time incident intelligence.",
                    "Policy evaluation required timely evidence between official reports.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Built ingestion pipelines from Twitter, Google News, and search trends.",
                    "Applied ML to classify tweets and articles into actionable categories.",
                    "Geocoded content to dashboards with contextual state-level metrics.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Collected hundreds of thousands of signals monthly for public awareness.",
                    "Increased engagement through gunviolencemap.org and national showcases.",
                    "Informed policy discussions at venues such as SXSW and media briefings.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led cross-functional team delivering analytics and visualization.",
                    "Used Python NLP, geocoding, and web development frameworks.",
                    "Integrated human review with automated pipelines for quality control.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "15.2.gunviolence-map-visual-analytics.png",
                "type": "image",
                "alt": "Gun violence visual analytics dashboard",
                "caption": "Topic and sentiment analytics powering public storytelling.",
            }
        ],
        "card": {
            "description": "Built a real-time platform that fuses digital exhaust to track US gun violence.",
            "role": "Role: Program architect",
            "focus": "Focus: Social data integration, ML classification, civic tech",
        },
    },
    {
        "id": 16,
        "slug": "16-demining-analytics-dashboard",
        "title": "Humanitarian Demining Analytics Dashboard",
        "subtitle": "Geospatial analytics system prioritizing landmine clearance using multi-sensor intelligence.",
        "hero_image": "16.1.Demining-dashboard-sys-design-location-focused-with-KPI.png",
        "hero_alt": "Demining dashboard system design",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Designed modular geospatial analytics for humanitarian demining operations.",
                    "Integrated multi-sensor detection data into actionable dashboards.",
                    "Equipped mission planners with prioritization and workflow tools.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Landmine clearance is slow, dangerous, and data fragmented.",
                    "Teams lacked unified views of sensor outputs and mission KPIs.",
                    "Resource constraints demanded precise prioritization of search areas.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Ingested multi-sensor detections and intelligence into layered maps.",
                    "Built KPI-driven dashboards scoring locations and tracking workflows.",
                    "Deployed modular microservices enabling rapid updates and scaling.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Improved prioritization of high-risk zones for clearance teams.",
                    "Enabled commanders to monitor progress and adjust tactics quickly.",
                    "Provided a replicable framework for humanitarian technology missions.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as product strategist aligning NGOs, defense, and tech partners.",
                    "Used Python, GIS tooling, and microservice design patterns.",
                    "Facilitated field feedback loops refining analytics and user experience.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Designed a modular geospatial system that guides humanitarian demining priorities.",
            "role": "Role: Product strategist",
            "focus": "Focus: Geospatial analytics, humanitarian tech, decision support",
        },
    },
    {
        "id": 17,
        "slug": "17-masl-isr-supervision",
        "title": "MAS-1 — MOTL-based ISR Supervision",
        "subtitle": "Multi-agent teaming strategies that dynamically reassign ISR roles using MOTL principles.",
        "hero_image": "17.1.Multi-agent-system-MOTL-based-ISR-Supervision.png",
        "hero_alt": "Multi-agent ISR supervision concept",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Developed MOTL-based multi-agent supervision for ISR mission coordination.",
                    "Automated dynamic role assignment among unmanned assets.",
                    "Enabled adaptive teaming with minimal operator load.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "ISR missions must balance coverage, persistence, and scarce assets.",
                    "Static tasking fails when conditions change mid-mission.",
                    "Operators cannot micromanage every asset in contested environments.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Applied MOTL for agent role allocation under competing objectives.",
                    "Implemented negotiation and partner selection to swap tasks on the fly.",
                    "Built simulation framework to evaluate strategies across scenarios.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Improved mission coverage and resilience under asset attrition.",
                    "Reduced operator interventions while maintaining ISR objectives.",
                    "Informed future multi-agent control architectures for defense partners.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led analytics bridging autonomy research with operational requirements.",
                    "Used multi-agent simulations, reinforcement learning, and optimization.",
                    "Collaborated with defense labs to validate algorithms and concepts.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "17.2.ISR-agent-role-exchange-partner-selection.png",
                "type": "image",
                "alt": "Agent role exchange and partner selection workflow",
                "caption": "Role exchange workflow illustrates adaptive task redistribution.",
            }
        ],
        "card": {
            "description": "Applied MOTL to coordinate ISR agents that swap roles as missions evolve.",
            "role": "Role: Autonomy research lead",
            "focus": "Focus: Multi-agent systems, reinforcement learning, defense ISR",
        },
    },
    {
        "id": 18,
        "slug": "18-masl-control-paradigm",
        "title": "MAS-2 — MOTL Control Paradigm",
        "subtitle": "Expanded MOTL paradigm for resilient multi-agent control across complex missions.",
        "hero_image": "18.1.John-Boyds-Control-loop.png",
        "hero_alt": "Control loop inspired by Boyd's OODA framework",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Extended the MOTL paradigm to broader control system design.",
                    "Created framework for coordinating multi-agent teams in complex environments.",
                    "Demonstrated approach across surveillance and decision-support scenarios.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Traditional control paradigms struggled with distributed, adaptive missions.",
                    "Needed to unify proactive planning with reactive agent behaviors.",
                    "Operators required transparent oversight of autonomous teams.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Defined MOTL stages linking sensing, learning, and tasking loops.",
                    "Implemented modular architecture aligning human command with autonomy.",
                    "Built simulations to stress-test responsiveness and adaptability.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Provided doctrine for integrating autonomy into command-and-control.",
                    "Improved agility of distributed teams under uncertain conditions.",
                    "Influenced design of future multi-agent mission management tools.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led conceptual framework and experimentation across partner labs.",
                    "Applied systems engineering, game theory, and multi-agent simulation.",
                    "Produced playbooks translating research into operational guidance.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Defined a resilient MOTL control paradigm for coordinating autonomous mission teams.",
            "role": "Role: Systems research lead",
            "focus": "Focus: Autonomy doctrine, control theory, mission design",
        },
    },
    {
        "id": 19,
        "slug": "19-patient-experience-longitudinal",
        "title": "Patient Experience — US Longitudinal Study",
        "subtitle": "Four-year analysis of patient experience trends across US states using surveys and digital signals.",
        "hero_image": "19.1.patient-experience-across-US-states-four-year-logitudinal-study.png",
        "hero_alt": "Longitudinal patient experience trends across US states",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Led a four-year longitudinal study on patient experience across states.",
                    "Integrated surveys, social media, and census data sources.",
                    "Delivered state scorecards for health system leaders.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Patient experience metrics vary widely by geography and demographics.",
                    "Traditional surveys alone miss evolving sentiment trends.",
                    "Policymakers need consistent benchmarks for equity improvements.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Combined CAHPS-style measures with large-scale social listening.",
                    "Applied hierarchical models to adjust for demographics and access.",
                    "Built interactive reports comparing states and tracking change.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Surfaced persistent gaps in experience across regions and populations.",
                    "Informed state strategies to improve patient-centered care.",
                    "Provided evidence for targeted quality improvement initiatives.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Served as principal analyst coordinating multi-year collaboration.",
                    "Used R, Python, and hierarchical modeling for longitudinal insights.",
                    "Partnered with health systems to translate results into action.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "19.1.patient-experience-across-US-states-four-year-logitudinal-study.pdf",
                "type": "pdf",
                "alt": "Detailed patient experience longitudinal report",
                "caption": "Full longitudinal report accessible within partner portals.",
            },
            {
                "src": "19.2.patient-experience-on-twitter-vs-census-all-states.png",
                "type": "image",
                "alt": "Patient experience sentiment versus census demographics",
                "caption": "Comparison of Twitter sentiment and demographic baselines by state.",
            },
        ],
        "card": {
            "description": "Measured four years of patient experience trends and equity gaps across every state.",
            "role": "Role: Principal analyst",
            "focus": "Focus: Experience analytics, longitudinal modeling, health equity",
        },
    },
    {
        "id": 20,
        "slug": "20-patient-experience-twitter",
        "title": "Patient Experience — Hospital Twitter Signals",
        "subtitle": "Twitter-based assessment of hospital experience across the United States.",
        "hero_image": "20.1.patient-experience-across-US-Hospitals.png",
        "hero_alt": "Patient experience sentiment across US hospitals",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Analyzed patient tweets to evaluate hospital experience nationwide.",
                    "Correlated social sentiment with clinical quality metrics.",
                    "Produced hospital-level dashboards for administrators.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Hospitals lacked real-time feedback beyond periodic surveys.",
                    "Needed to understand experience differences across facilities.",
                    "Large social data requires careful curation for healthcare context.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Collected and filtered hospital-related tweets with custom classifiers.",
                    "Linked sentiment with CMS quality metrics and geography.",
                    "Built dashboards ranking hospitals and highlighting opportunities.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Exposed experience gaps across hospital systems and regions.",
                    "Enabled quality teams to monitor perception trends in near real time.",
                    "Demonstrated scalable fusion of digital and clinical metrics.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led analytics bridge between marketing, quality, and data science.",
                    "Applied NLP, sentiment modeling, and visualization platforms.",
                    "Established governance for ethical social media use in healthcare.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Mapped hospital patient experience by mining and contextualizing social media feedback.",
            "role": "Role: Experience analytics lead",
            "focus": "Focus: Social listening, healthcare quality, data visualization",
        },
    },
    {
        "id": 21,
        "slug": "21-patient-experience-equity",
        "title": "Patient Experience — Racial Equity Signals",
        "subtitle": "Measured racial disparities in patient experience sentiment using responsibly inferred demographics.",
        "hero_image": "21.1.patient-experience-user-race-correlation-with-census-last-name-across-all-states.png",
        "hero_alt": "Correlation between patient sentiment and inferred race across states",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Analyzed patient sentiment by inferred race to uncover disparities.",
                    "Combined Twitter data with census-based race inference.",
                    "Delivered insights on equity gaps in patient experience.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Racial disparities often hide within aggregate experience metrics.",
                    "Digital data rarely includes explicit demographic tagging.",
                    "Needed ethical methods for inferring identity while protecting privacy.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Used surname and geolocation proxies to estimate racial distributions.",
                    "Aligned sentiment models with validated demographic benchmarks.",
                    "Built dashboards highlighting gaps and improvement opportunities.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Quantified inequities in patient experience across racial groups nationwide.",
                    "Guided health systems toward targeted outreach and service redesign.",
                    "Advanced ethical analytics practices for demographic inference.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led research bridging data science, DEI experts, and ethicists.",
                    "Applied NLP, Bayesian inference, and fairness assessments.",
                    "Delivered equity reports with actionable recommendations.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Exposed racial disparities in patient experience by fusing sentiment and demographic inference.",
            "role": "Role: Health equity analytics lead",
            "focus": "Focus: Fairness analytics, patient experience, responsible AI",
        },
    },
    {
        "id": 22,
        "slug": "22-smoking-structured-resistance",
        "title": "Social Contagion 1 — Structured Resistance Model",
        "subtitle": "Structured resistance model explaining the stubborn decline of smoking prevalence.",
        "hero_image": "22.1.Smoking-behavior-structured-resistance-model.png",
        "hero_alt": "Structured resistance model for smoking contagion",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Introduced a structured resistance model for smoking contagion.",
                    "Explained persistent smoking despite decades of intervention.",
                    "Used multi-level states to capture addiction dynamics.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Traditional SIS models predicted rapid smoking decline unlike reality.",
                    "Addiction alters susceptibility yet was absent from prior models.",
                    "Policy planning needed accurate long-term behavior forecasts.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Extended SIS with multiple susceptible and infected tiers.",
                    "Modeled relapse dynamics with escalating resistance thresholds.",
                    "Simulated longitudinal data to validate slow decline patterns.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Demonstrated backward bifurcation requiring stronger interventions.",
                    "Provided insights guiding long-term anti-smoking strategies.",
                    "Informed later projects on targeted intervention design.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led modeling collaboration with social epidemiologists and mathematicians.",
                    "Applied differential equations, simulation, and network analysis.",
                    "Shared findings through conferences and policy workshops.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "22.2.overview-of-network-centric-intervenstions-for-controlling-smoking-epidemic.png",
                "type": "image",
                "alt": "Network-centric interventions for smoking control",
                "caption": "Intervention playbook derived from structured resistance modeling.",
            }
        ],
        "card": {
            "description": "Modeled smoking as a structured contagion to explain why prevalence declines so slowly.",
            "role": "Role: Lead modeler",
            "focus": "Focus: Behavioral epidemiology, nonlinear dynamics",
        },
    },
    {
        "id": 23,
        "slug": "23-smoking-online-exposure",
        "title": "Social Contagion 2 — Online Exposure",
        "subtitle": "Quantified teen exposure to smoking content on Twitter using supervised modeling.",
        "hero_image": "23.1.social-media-supervised-ML-model-building-workflow.png",
        "hero_alt": "Workflow for supervised ML smoking exposure study",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Measured teen exposure to smoking content on Twitter.",
                    "Built supervised models to classify pro-tobacco messaging.",
                    "Estimated vulnerable audiences for public health partners.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Underage users encounter tobacco content without strict age controls.",
                    "Exposure levels were unknown, hindering intervention design.",
                    "Needed scalable methods to spot youth following pro-smoking accounts.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Collected smoking-related tweets and follower networks at scale.",
                    "Used supervised ML to classify promotional and advocacy content.",
                    "Estimated exposure frequencies and hotspots for regulators.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Revealed substantial teen exposure to pro-smoking messaging online.",
                    "Supported advocacy for stronger platform age controls.",
                    "Guided targeted health education and outreach campaigns.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led social media data collection and modeling efforts.",
                    "Applied supervised ML, network analysis, and exposure estimation.",
                    "Collaborated with public health partners on responsible reporting.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "23.2.smoking-related-tweet-exposure-estimation-for-underage-users.png",
                "type": "image",
                "alt": "Exposure estimation for underage users",
                "caption": "Exposure estimation highlighted reach of pro-smoking tweets to teens.",
            }
        ],
        "card": {
            "description": "Quantified how underage audiences encounter smoking promotion across Twitter networks.",
            "role": "Role: Social data scientist",
            "focus": "Focus: Exposure modeling, network analytics, youth prevention",
        },
    },
    {
        "id": 24,
        "slug": "24-ecig-exposure-hotspots",
        "title": "Social Contagion 3 — E-cig Exposure Hotspots",
        "subtitle": "Mapped e-cigarette social media exposure hotspots to guide youth prevention.",
        "hero_image": "24.1.e-cig-socialmedia-exposure-westcoast-hotspots.png",
        "hero_alt": "E-cig social media exposure hotspots map",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Analyzed e-cigarette social media exposure across US regions.",
                    "Identified hotspots of youth-targeted content.",
                    "Equipped public health teams with prevention insights.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Rapid e-cig marketing reached youth via digital channels.",
                    "Public health lacked a geographic view of exposure intensity.",
                    "Needed to pinpoint communities for targeted interventions.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Collected e-cig posts and geolocated them to counties nationwide.",
                    "Measured content themes, sentiment, and influencer reach.",
                    "Visualized hotspots to inform outreach planning.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Highlighted regional exposure surges, including West Coast clusters.",
                    "Supported agencies in prioritizing prevention campaigns and resources.",
                    "Strengthened regulatory discussions on digital advertising oversight.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led data pipeline and geospatial analysis with tobacco control experts.",
                    "Applied NLP, sentiment analysis, and mapping platforms.",
                    "Coordinated findings with youth prevention coalitions.",
                ],
            },
        ],
        "gallery": [],
        "card": {
            "description": "Mapped where e-cigarette messaging concentrates so prevention teams can respond quickly.",
            "role": "Role: Lead exposure analyst",
            "focus": "Focus: Geospatial social analytics, youth tobacco prevention",
        },
    },
    {
        "id": 25,
        "slug": "25-contagion-edge-blocking",
        "title": "Social Contagion 4 — Edge Blocking",
        "subtitle": "Efficient edge-removal strategies to contain harmful social contagions.",
        "hero_image": "25.1.an-efficient-algorithm-for-edge-removal-based-social-contagion-blocking.png",
        "hero_alt": "Edge removal algorithm performance comparison",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Developed efficient edge-removal algorithms to block social contagions.",
                    "Balanced proactive planning with minimal network disruption.",
                    "Outperformed previous structural approaches in simulations.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Stopping harmful contagions requires removing minimal connections.",
                    "Existing methods were computationally heavy or ineffective on complex networks.",
                    "Decision-makers need actionable interventions under resource limits.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Designed heuristics leveraging network structure and influence scores.",
                    "Optimized edge selection to minimize contagion reach.",
                    "Tested across synthetic and real networks for robustness.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Achieved better containment with fewer interventions than baselines.",
                    "Provided practical guidance for policymakers on contagion blocking.",
                    "Complemented node-focused strategies with edge-centric toolkits.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led algorithm design and evaluation with academic collaborators.",
                    "Used graph optimization, simulations, and complexity analysis.",
                    "Translated findings into policy-focused playbooks.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "25.2.our-approach-for-blocking-social-contagion-vs-pervious-studies.png",
                "type": "image",
                "alt": "Edge blocking approach versus prior studies",
                "caption": "Comparison chart illustrating gains over prior edge-blocking methods.",
            }
        ],
        "card": {
            "description": "Engineered edge-removal strategies that stop contagion spread with minimal disruption.",
            "role": "Role: Network science lead",
            "focus": "Focus: Graph optimization, resilience planning",
        },
    },
    {
        "id": 26,
        "slug": "26-contagion-community-blocking",
        "title": "Social Contagion 5 — Community Blocking",
        "subtitle": "Hybrid community-based strategy to contain complex social contagions.",
        "hero_image": "26.1.community-based-social-contagion-blocking-illustration.png",
        "hero_alt": "Community-based social contagion blocking illustration",
        "sections": [
            {
                "heading": "At a glance",
                "bullets": [
                    "Developed community-based strategy to block complex contagions.",
                    "Targeted boundary nodes bridging communities.",
                    "Blended structural analysis with reactive simulations.",
                ],
            },
            {
                "heading": "Problem",
                "bullets": [
                    "Complex contagions require multiple confirmations, resisting simple interventions.",
                    "Purely structural or purely reactive methods underperformed alone.",
                    "Needed efficient approaches leveraging community structure.",
                ],
            },
            {
                "heading": "Solution",
                "bullets": [
                    "Detected communities and identified inter-community chokepoints.",
                    "Simulated threshold contagions to prioritize boundary nodes.",
                    "Applied hybrid selection balancing speed and effectiveness.",
                ],
            },
            {
                "heading": "Impact",
                "bullets": [
                    "Contained complex contagions more effectively than prior methods.",
                    "Reduced interventions while maintaining protection across networks.",
                    "Inspired integrated approaches for social contagion preparedness.",
                ],
            },
            {
                "heading": "Role & toolkit",
                "bullets": [
                    "Led algorithm design combining graph clustering and simulations.",
                    "Used community detection, threshold models, and optimization.",
                    "Shared results through workshops and follow-on research.",
                ],
            },
        ],
        "gallery": [
            {
                "src": "26.2.a-heuristic-for-community-based-social-contagion-blocking.png",
                "type": "image",
                "alt": "Heuristic for community-based blocking",
                "caption": "Hybrid heuristic balancing structural speed with dynamic accuracy.",
            }
        ],
        "card": {
            "description": "Combined community detection and simulations to halt complex contagions efficiently.",
            "role": "Role: Network intervention researcher",
            "focus": "Focus: Community analytics, hybrid algorithms",
        },
    },
]

CARD_ORDER = sorted(PROJECTS, key=lambda p: p["id"])


def escape(text: str) -> str:
    return html.escape(text, quote=True)


def build_section(section: dict) -> str:
    heading = escape(section["heading"])
    bullet_html = "\n".join(
        f"              <li>{escape(bullet)}</li>" for bullet in section.get("bullets", [])
    )
    return (
        "          <section class=\"project-section\">\n"
        f"            <h2>{heading}</h2>\n"
        "            <ul>\n"
        f"{bullet_html}\n"
        "            </ul>\n"
        "          </section>"
    )


def build_gallery(project: dict) -> str:
    items = []
    for asset in project.get("gallery", []):
        src = escape(asset["src"])
        caption = escape(asset.get("caption", ""))
        if asset.get("type") == "pdf":
            alt = escape(asset.get("alt", ""))
            items.append(
                "            <figure class=\"project-gallery__item project-gallery__item--pdf\">\n"
                f"              <object data=\"{src}\" type=\"application/pdf\" aria-label=\"{alt}\"></object>\n"
                f"              <figcaption>{caption}</figcaption>\n"
                "            </figure>"
            )
        else:
            alt = escape(asset.get("alt", ""))
            items.append(
                "            <figure class=\"project-gallery__item\">\n"
                f"              <img src=\"{src}\" alt=\"{alt}\" />\n"
                f"              <figcaption>{caption}</figcaption>\n"
                "            </figure>"
            )
    if not items:
        return ""
    return (
        "          <section class=\"project-section project-section--gallery\">\n"
        "            <h2>Visual highlights</h2>\n"
        "            <div class=\"project-gallery\">\n"
        + "\n".join(items)
        + "\n            </div>\n          </section>"
    )


def build_project_page(project: dict) -> str:
    sections_html = "\n".join(build_section(section) for section in project["sections"])
    gallery_html = build_gallery(project)
    if gallery_html:
        sections_html += "\n" + gallery_html

    hero_image = escape(project["hero_image"])
    hero_alt = escape(project["hero_alt"])
    title = escape(project["title"])
    subtitle = escape(project["subtitle"])

    return (
        "<!DOCTYPE html>\n"
        '<html lang="en" class="theme-light">\n'
        "<head>\n"
        '  <meta charset="UTF-8" />\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        f"  <title>{title}</title>\n"
        '  <link rel="stylesheet" href="../assets/css/al-folio.css" />\n'
        '  <link rel="stylesheet" href="../assets/css/custom.css" />\n'
        "</head>\n"
        '<body class="page">\n'
        '  <div class="page__inner">\n'
        '    <header class="project-hero">\n'
        '      <div class="wrapper project-hero__inner">\n'
        '        <a class="back-link" href="../index.html">&larr; Back to portfolio</a>\n'
        f"        <h1 class=\"project-hero__title\">{title}</h1>\n"
        f"        <p class=\"project-hero__subtitle\">{subtitle}</p>\n"
        "      </div>\n"
        "    </header>\n"
        "\n"
        '    <main class="wrapper project-body">\n'
        '      <div class="project-body__grid">\n'
        '        <figure class="project-body__media project-body__media--hero">\n'
        f'          <img src="{hero_image}" alt="{hero_alt}" />\n'
        "        </figure>\n"
        '        <div class="project-body__content">\n'
        f"{sections_html}\n"
        "        </div>\n"
        "      </div>\n"
        "    </main>\n"
        "\n"
        '    <footer class="wrapper project-footer">\n'
        '      <a class="btn btn--ghost" href="../index.html">Back to portfolio</a>\n'
        "    </footer>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


def build_project_card(project: dict) -> str:
    slug = project["slug"]
    href = f"{slug}/index.html"
    image = escape(project["hero_image"])
    alt = escape(project["hero_alt"])
    title = escape(project["title"])
    description = escape(project["card"]["description"])
    role = escape(project["card"]["role"])
    focus = escape(project["card"]["focus"])

    return (
        "        <article class=\"project-card\">\n"
        f"          <a class=\"project-card__link\" href=\"{href}\">\n"
        '            <figure class="project-card__figure">\n'
        f'              <img src="{slug}/{image}" alt="{alt}" />\n'
        "            </figure>\n"
        '            <div class="project-card__content">\n'
        f"              <h3 class=\"project-card__title\">{title}</h3>\n"
        f"              <p class=\"project-card__description\">{description}</p>\n"
        "              <ul class=\"project-card__meta\">\n"
        f"                <li>{role}</li>\n"
        f"                <li>{focus}</li>\n"
        "              </ul>\n"
        "            </div>\n"
        "          </a>\n"
        "        </article>"
    )


def build_index() -> str:
    hero = (
        "<!DOCTYPE html>\n"
        '<html lang="en" class="theme-light">\n'
        "<head>\n"
        '  <meta charset="UTF-8" />\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        '  <title>Gaurav Tuli | Portfolio</title>\n'
        '  <link rel="stylesheet" href="assets/css/al-folio.css" />\n'
        '  <link rel="stylesheet" href="assets/css/custom.css" />\n'
        "</head>\n"
        '<body class="page">\n'
        '  <div class="page__inner">\n'
        '    <header class="landing-header">\n'
        '      <div class="wrapper hero">\n'
        '        <span class="hero__eyebrow">Gaurav Tuli, PhD</span>\n'
        '        <h1 class="hero__title">Translating public health and healthcare data into actionable intelligence.</h1>\n'
        '        <p class="hero__subtitle">\n'
        '          Clinician-data scientist building surveillance platforms, predictive models, and decision support tools that help\n'
        '          health systems and government agencies respond faster and smarter.\n'
        '        </p>\n'
        '        <div class="hero__actions">\n'
        '          <a class="btn btn--primary" href="#projects">Explore signature projects</a>\n'
        '          <a class="btn btn--ghost" href="mailto:gtuli.ml@gmail.com">Let’s collaborate</a>\n'
        '        </div>\n'
        '      </div>\n'
        '    </header>\n'
        "\n"
        '    <main id="projects" class="wrapper landing-main">\n'
        '      <section class="section-intro">\n'
        '        <h2 class="section-title">Featured initiatives</h2>\n'
        '        <p class="section-subtitle">\n'
        '          Each project pairs rigorous analytics with compassionate healthcare delivery—spanning biosurveillance, precision\n'
        '          diagnostics, and clinical decision support.\n'
        '        </p>\n'
        '      </section>\n'
        "\n"
        '      <div class="project-grid">\n'
    )

    cards_html = "\n".join(build_project_card(project) for project in CARD_ORDER)

    footer = (
        "      </div>\n"
        "    </main>\n"
        "\n"
        '    <section class="wrapper landing-secondary">\n'
        '      <div class="callout">\n'
        '        <h2 class="callout__title">Beyond the portfolio</h2>\n'
        '        <p class="callout__description">\n'
        '          Gaurav collaborates with federal agencies, health systems, and startups to advance equitable care. Whether it is\n'
        '          architecting national-scale biosurveillance or deploying AI safely at the bedside, each engagement blends systems\n'
        '          thinking with compassionate leadership.\n'
        '        </p>\n'
        '        <a class="btn btn--primary" href="mailto:gtuli.ml@gmail.com">Start a conversation</a>\n'
        '      </div>\n'
        '    </section>\n'
        "\n"
        '    <footer class="wrapper site-footer">\n'
        '      <p class="site-footer__text">&copy; <span id="year"></span> Gaurav Tuli. Built with the al-folio design system.</p>\n'
        '    </footer>\n'
        '  </div>\n'
        '  <script>\n'
        "    document.getElementById('year').textContent = new Date().getFullYear();\n"
        '  </script>\n'
        '</body>\n'
        '</html>\n'
    )

    return hero + cards_html + "\n" + footer


def main() -> None:
    for project in PROJECTS:
        project_dir = ROOT / project["slug"]
        project_dir.mkdir(parents=True, exist_ok=True)
        (project_dir / "index.html").write_text(build_project_page(project), encoding="utf-8")

    (ROOT / "index.html").write_text(build_index(), encoding="utf-8")


if __name__ == "__main__":
    main()
