"""
Open Vantage ISMS – Policy Document Generator
Generates 6 core ISO 27001 policy documents as markdown files
"""
 
import os, sys
from datetime import date
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.ov_context import COMPANY, ISMS_SCOPE
 
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'policies')
os.makedirs(OUTPUT_DIR, exist_ok=True)
 
TODAY = date.today().strftime("%d %B %Y")
VERSION = "v1.0"
STATUS = "DRAFT – Pending CEO Approval"
 
 
def _header(title, doc_id, purpose):
    return [
        f"# {title}",
        f"## {COMPANY['name']}",
        "",
        "| Field | Detail |",
        "|---|---|",
        f"| **Document ID** | {doc_id} |",
        f"| **Version** | {VERSION} |",
        f"| **Status** | {STATUS} |",
        f"| **Date** | {TODAY} |",
        f"| **Owner** | {COMPANY['document_owner']} |",
        f"| **Approved By** | {COMPANY['approved_by']} |",
        f"| **Review Cycle** | {COMPANY['review_cycle']} |",
        f"| **Classification** | INTERNAL – CONFIDENTIAL |",
        "",
        "---", "",
        "## 1. Purpose",
        "",
        purpose,
        "",
        "---", "",
    ]
 
 
# ── POLICY 1: Information Security Policy ────────────────────────────────────
def generate_information_security_policy():
    L = _header(
        "Information Security Policy",
        "OV-POL-001",
        (
            "This policy establishes Open Vantage's commitment to protecting the confidentiality, "
            "integrity and availability of all information assets — including client intellectual "
            "property, source code, personal information and business data — in support of ISO/IEC "
            "27001:2022 certification and compliance with POPIA, GDPR and UK GDPR."
        )
    )
    L += [
        "## 2. Scope",
        "",
        ISMS_SCOPE["scope_statement"],
        "",
        "---", "",
        "## 3. Policy Statement",
        "",
        f"{COMPANY['name']} is committed to:",
        "",
        "- Protecting all information assets from unauthorised access, disclosure, modification, destruction or interference",
        "- Ensuring the confidentiality of client intellectual property, source code and personal information",
        "- Maintaining the integrity of software development outputs and client deliverables",
        "- Ensuring the availability of systems and services to meet client contractual obligations",
        "- Complying with all applicable legal, regulatory and contractual requirements including POPIA, GDPR and UK GDPR",
        "- Continuously improving the Information Security Management System (ISMS)",
        "- Embedding information security into all software development projects from inception",
        "",
        "---", "",
        "## 4. Information Security Objectives",
        "",
        "| Objective | Measure | Target |",
        "|---|---|---|",
        "| Achieve ISO 27001:2022 certification | Certification audit outcome | Q4 2025 |",
        "| Zero critical unpatched vulnerabilities | Vulnerability scan results | <30 days patch cycle |",
        "| 100% staff security awareness training | Training completion rate | 100% annually |",
        "| Incident response readiness | Tabletop exercise completion | Bi-annual |",
        "| POPIA compliance | Information Regulator audit findings | Zero major findings |",
        "| Supplier security | Vendor risk assessments completed | 100% of critical vendors |",
        "",
        "---", "",
        "## 5. Roles and Responsibilities",
        "",
        "| Role | Responsibility |",
        "|---|---|",
        "| **CEO** | Approves ISMS policy; provides visible leadership commitment |",
        "| **CISO** | Owns the ISMS; responsible for implementation and maintenance |",
        "| **Information Officer** | POPIA compliance; liaises with Information Regulator |",
        "| **All Staff & Contractors** | Comply with all security policies; report security events |",
        "| **Project Leads** | Embed security requirements in all client projects |",
        "| **HR** | Ensures security obligations in employment contracts and onboarding |",
        "",
        "---", "",
        "## 6. Compliance",
        "",
        "All Open Vantage employees, contractors and augmented talent must comply with this policy. "
        "Non-compliance may result in disciplinary action up to and including termination of employment "
        "or contract. Breaches involving client data may also trigger legal and regulatory consequences "
        "under POPIA, GDPR or applicable client contracts.",
        "",
        "---", "",
        "## 7. Related Documents",
        "",
        "- OV-POL-002 Acceptable Use Policy",
        "- OV-POL-003 Access Control Policy",
        "- OV-POL-004 Incident Response Policy",
        "- OV-POL-005 Remote Working Policy",
        "- OV-POL-006 Data Classification Policy",
        "- OV-SOA-001 Statement of Applicability",
        "",
        "---", "",
        "## 8. Review and Approval",
        "",
        "This policy is reviewed annually or following any significant change to the business, "
        "technology landscape or regulatory environment. The CISO is responsible for initiating "
        "reviews and obtaining CEO approval for updates.",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['hq_address']} | {COMPANY['website']}*",
    ]
    path = os.path.join(OUTPUT_DIR, 'OV-POL-001-Information-Security-Policy.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-POL-001 Information Security Policy → {path}")
    return path
 
 
# ── POLICY 2: Acceptable Use Policy ──────────────────────────────────────────
def generate_acceptable_use_policy():
    L = _header(
        "Acceptable Use Policy",
        "OV-POL-002",
        (
            "This policy defines the acceptable use of Open Vantage information systems, "
            "devices, networks and data by all employees, contractors and augmented talent, "
            "to protect OV and client information assets from misuse or compromise."
        )
    )
    L += [
        "## 2. Scope",
        "",
        "This policy applies to all employees, contractors, augmented talent and any other "
        "persons granted access to Open Vantage systems, devices or data.",
        "",
        "---", "",
        "## 3. Acceptable Use",
        "",
        "### 3.1 Permitted Activities",
        "- Use of OV systems for legitimate business purposes related to your role",
        "- Access to client systems only for approved project work",
        "- Use of approved collaboration tools (Slack, Microsoft Teams, GitHub/GitLab)",
        "- Remote working via OV-approved VPN",
        "- Storage of work files in OV-approved cloud storage only",
        "",
        "### 3.2 Prohibited Activities",
        "- Accessing client data beyond your project assignment",
        "- Storing client source code or data on personal devices or unapproved storage",
        "- Sharing OV or client credentials with any other person",
        "- Installing unlicensed or unapproved software on OV devices",
        "- Using OV systems for personal financial gain or illegal activities",
        "- Connecting to public Wi-Fi without using the OV VPN",
        "- Disabling security software (antivirus, EDR, MDM) on OV devices",
        "- Removing OV equipment from its approved location without authorisation",
        "",
        "---", "",
        "## 4. Device Usage",
        "",
        "| Requirement | Detail |",
        "|---|---|",
        "| **Screen lock** | Auto-lock after 5 minutes of inactivity |",
        "| **Encryption** | Full disk encryption enabled on all laptops |",
        "| **MFA** | Multi-factor authentication required for all OV systems |",
        "| **Updates** | Security updates installed within 14 days of release |",
        "| **VPN** | Required when working outside OV office on sensitive work |",
        "| **USB** | Removable media use requires CISO approval |",
        "",
        "---", "",
        "## 5. Internet and Email Usage",
        "",
        "- Business email must be used for all client and official communications",
        "- Client data must never be sent via personal email accounts",
        "- Suspicious emails must be reported to the CISO immediately",
        "- Clicking links or downloading attachments from unknown sources is prohibited",
        "",
        "---", "",
        "## 6. Consequences of Non-Compliance",
        "",
        "Violations of this policy may result in disciplinary action including warnings, "
        "suspension or termination. Violations involving client data may result in legal "
        "action and notification to relevant regulators under POPIA or GDPR.",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | Related: OV-POL-001*",
    ]
    path = os.path.join(OUTPUT_DIR, 'OV-POL-002-Acceptable-Use-Policy.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-POL-002 Acceptable Use Policy → {path}")
    return path
 
 
# ── POLICY 3: Access Control Policy ──────────────────────────────────────────
def generate_access_control_policy():
    L = _header(
        "Access Control Policy",
        "OV-POL-003",
        (
            "This policy establishes Open Vantage's approach to managing access to information "
            "systems, client environments, source code repositories and data, based on the "
            "principles of least privilege, need-to-know and separation of duties."
        )
    )
    L += [
        "## 2. Access Control Principles",
        "",
        "| Principle | Description |",
        "|---|---|",
        "| **Least Privilege** | Users receive only the minimum access required for their role |",
        "| **Need-to-Know** | Access to client data is restricted to relevant project team members only |",
        "| **Separation of Duties** | No single person can approve and execute sensitive changes |",
        "| **Default Deny** | Access is denied by default unless explicitly granted |",
        "| **Regular Review** | All access rights are reviewed quarterly |",
        "",
        "---", "",
        "## 3. Access Management Process",
        "",
        "### 3.1 Provisioning",
        "1. Line manager submits access request to CISO",
        "2. CISO approves based on role and project assignment",
        "3. IT provisions access within 1 business day",
        "4. User receives access confirmation and acknowledges AUP",
        "",
        "### 3.2 Access Reviews",
        "- **Quarterly** — all user access rights reviewed by CISO",
        "- **On role change** — access updated within 24 hours",
        "- **On departure** — all access revoked within 4 hours of termination",
        "",
        "### 3.3 Privileged Access",
        "- Admin and privileged accounts require separate approval from CEO or CISO",
        "- Privileged accounts must use MFA at all times",
        "- Privileged access sessions must be logged and monitored",
        "- Shared admin credentials are prohibited",
        "",
        "---", "",
        "## 4. Authentication Requirements",
        "",
        "| System Type | MFA Required | Password Minimum |",
        "|---|---|---|",
        "| Client systems | ✅ Yes | 14 characters |",
        "| Cloud environments (AWS/Azure/GCP) | ✅ Yes | 14 characters |",
        "| Source code repositories (GitHub/GitLab) | ✅ Yes | 12 characters |",
        "| OV internal systems | ✅ Yes | 12 characters |",
        "| VPN | ✅ Yes | 14 characters |",
        "",
        "---", "",
        "## 5. Remote Access",
        "",
        "- All remote access to OV and client systems must use the approved VPN",
        "- MFA is mandatory for all remote access",
        "- Remote sessions must be terminated when not in use",
        "- Public Wi-Fi must never be used without VPN",
        "",
        "---", "",
        "## 6. Third-Party and Contractor Access",
        "",
        "- Contractors and augmented talent receive access only for their assigned project",
        "- Third-party access is time-limited and reviewed monthly",
        "- All contractor access is revoked immediately on contract termination",
        "- Vendors accessing OV or client systems must sign the OV Supplier Security Agreement",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | Related: OV-POL-001, OV-POL-002*",
    ]
    path = os.path.join(OUTPUT_DIR, 'OV-POL-003-Access-Control-Policy.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-POL-003 Access Control Policy → {path}")
    return path
 
 
# ── POLICY 4: Incident Response Policy ───────────────────────────────────────
def generate_incident_response_policy():
    L = _header(
        "Incident Response Policy",
        "OV-POL-004",
        (
            "This policy defines Open Vantage's approach to detecting, reporting, assessing, "
            "responding to and learning from information security incidents, in compliance with "
            "ISO 27001:2022 Annex A.5.24 and POPIA Section 22 breach notification requirements."
        )
    )
    L += [
        "## 2. Incident Classification",
        "",
        "| Severity | Description | Examples | Response Time |",
        "|---|---|---|---|",
        "| 🔴 **P1 Critical** | Confirmed breach of client or personal data | Ransomware, data exfiltration, account takeover | 1 hour |",
        "| 🟠 **P2 High** | Significant security event with potential data impact | Malware infection, suspicious admin activity | 4 hours |",
        "| 🟡 **P3 Medium** | Security event with limited impact | Phishing attempt, policy violation | 24 hours |",
        "| 🟢 **P4 Low** | Minor security event with no data impact | Lost device (no sensitive data), minor AUP breach | 72 hours |",
        "",
        "---", "",
        "## 3. Incident Response Process",
        "",
        "### Phase 1 — Detect & Report",
        "- Any staff member detecting a security event must report it immediately to the CISO",
        "- Report via: security@openvantage.co.za or direct call to CISO",
        "- Do NOT attempt to investigate or remediate without CISO authorisation",
        "",
        "### Phase 2 — Assess & Contain",
        "- CISO assesses severity within the applicable response time",
        "- Containment actions taken to limit damage (isolate systems, revoke access)",
        "- Evidence preserved for forensic investigation",
        "",
        "### Phase 3 — Investigate & Eradicate",
        "- Root cause investigation conducted",
        "- Affected systems cleaned and restored from clean backups",
        "- Vulnerabilities exploited during the incident remediated",
        "",
        "### Phase 4 — Notify",
        "",
        "| Notification | Trigger | Deadline |",
        "|---|---|---|",
        "| **Information Regulator (POPIA S.22)** | Personal information breach | As soon as reasonably possible |",
        "| **Netherlands AP (GDPR Art.33)** | Personal data breach (Netherlands office) | 72 hours |",
        "| **UK ICO (UK GDPR)** | Personal data breach (UK office) | 72 hours |",
        "| **Affected clients** | Breach of client data or systems | Within 24 hours of confirmation |",
        "| **Affected data subjects** | High-risk breach of personal data | Without undue delay |",
        "",
        "### Phase 5 — Recover & Learn",
        "- Systems restored to normal operation",
        "- Post-incident review conducted within 5 business days",
        "- Lessons learned documented and fed into ISMS improvement",
        "",
        "---", "",
        "## 4. POPIA Section 22 Breach Notification",
        "",
        "Open Vantage must notify the Information Regulator of South Africa when personal "
        "information has been accessed or acquired by an unauthorised person. Notification "
        "must include: nature of the breach, personal information involved, likely consequences, "
        "measures taken or proposed, and contact details of the Information Officer.",
        "",
        "**Information Regulator contact:** inforeg@justice.gov.za | 010 023 5207",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | Related: OV-POL-001, OV-SOA-001*",
    ]
    path = os.path.join(OUTPUT_DIR, 'OV-POL-004-Incident-Response-Policy.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-POL-004 Incident Response Policy → {path}")
    return path
 
 
# ── POLICY 5: Remote Working Policy ──────────────────────────────────────────
def generate_remote_working_policy():
    L = _header(
        "Remote Working Policy",
        "OV-POL-005",
        (
            "This policy governs the secure use of remote working arrangements by Open Vantage "
            "employees, contractors and augmented talent, ensuring that information security "
            "controls are maintained outside the office environment."
        )
    )
    L += [
        "## 2. Scope",
        "",
        "This policy applies to all Open Vantage personnel working remotely, including from "
        "home, client sites, co-working spaces or any location outside the Sandton WeWork office.",
        "",
        "---", "",
        "## 3. Remote Working Requirements",
        "",
        "### 3.1 Device Requirements",
        "- Only OV-issued or OV-approved devices may be used for work",
        "- Devices must have full disk encryption enabled",
        "- Devices must have OV-approved antivirus/EDR software installed",
        "- Auto-lock must be configured (maximum 5 minutes)",
        "- Personal devices must not be used to store or process client data",
        "",
        "### 3.2 Network Requirements",
        "- VPN must be used when accessing OV or client systems remotely",
        "- Public Wi-Fi must not be used without VPN",
        "- Home routers must use WPA2 or WPA3 encryption",
        "- Personal mobile hotspots are acceptable for temporary connectivity",
        "",
        "### 3.3 Physical Security",
        "- Screens must not be visible to unauthorised persons",
        "- Sensitive conversations must not be held in public places",
        "- Devices must not be left unattended in public or vehicles",
        "- Clear desk policy applies in shared spaces",
        "",
        "---", "",
        "## 4. Cross-Border Working",
        "",
        "Open Vantage operates across South Africa, the Netherlands and the United Kingdom. "
        "Staff working across borders must be aware that:",
        "",
        "- POPIA applies to all processing of South African personal information",
        "- GDPR applies when processing EU/Netherlands personal data",
        "- UK GDPR applies when processing UK personal data",
        "- Cross-border data transfers must comply with applicable transfer mechanisms",
        "- Any data transfers outside the SADC region must be approved by the Information Officer",
        "",
        "---", "",
        "## 5. Incident Reporting",
        "",
        "Remote workers must report security incidents immediately regardless of location. "
        "Lost or stolen devices must be reported to the CISO within 1 hour of discovery. "
        "The CISO will initiate remote wipe procedures for lost or stolen OV devices.",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | Related: OV-POL-001, OV-POL-002, OV-POL-003*",
    ]
    path = os.path.join(OUTPUT_DIR, 'OV-POL-005-Remote-Working-Policy.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-POL-005 Remote Working Policy → {path}")
    return path
 
 
# ── POLICY 6: Data Classification Policy ─────────────────────────────────────
def generate_data_classification_policy():
    L = _header(
        "Data Classification Policy",
        "OV-POL-006",
        (
            "This policy defines Open Vantage's framework for classifying information assets "
            "according to their sensitivity and value, ensuring appropriate protection controls "
            "are applied consistently across all information handling activities."
        )
    )
    L += [
        "## 2. Classification Levels",
        "",
        "| Level | Label | Description | Examples |",
        "|---|---|---|---|",
        "| 1 | 🔴 **CONFIDENTIAL** | Highest sensitivity — serious harm if disclosed | Client source code, personal data (POPIA/GDPR), financial data, security credentials |",
        "| 2 | 🟠 **RESTRICTED** | Sensitive — could cause harm if disclosed | Client project plans, internal financial reports, employee records, NDA-covered information |",
        "| 3 | 🟡 **INTERNAL** | For internal use only | Internal policies, meeting notes, general business communications |",
        "| 4 | 🟢 **PUBLIC** | Approved for public release | Website content, published case studies, press releases |",
        "",
        "---", "",
        "## 3. Handling Requirements",
        "",
        "| Requirement | CONFIDENTIAL | RESTRICTED | INTERNAL | PUBLIC |",
        "|---|---|---|---|---|",
        "| Encryption at rest | ✅ Required | ✅ Required | ⚠️ Recommended | ❌ Not required |",
        "| Encryption in transit | ✅ Required | ✅ Required | ✅ Required | ❌ Not required |",
        "| Access control | Strict need-to-know | Role-based | All staff | Unrestricted |",
        "| MFA required | ✅ Yes | ✅ Yes | ⚠️ Recommended | ❌ No |",
        "| Printing | Prohibited | Restricted | Allowed | Allowed |",
        "| Email (external) | Encrypted only | Encrypted only | Allowed | Allowed |",
        "| Cloud storage | OV-approved only | OV-approved only | OV-approved only | Any |",
        "| Disposal | Secure wipe/shred | Secure wipe/shred | Standard delete | Standard delete |",
        "",
        "---", "",
        "## 4. Personal Information (POPIA/GDPR)",
        "",
        "All personal information — regardless of other classification — must be treated as "
        "minimum CONFIDENTIAL and handled in compliance with POPIA (South Africa), GDPR "
        "(Netherlands) and UK GDPR (United Kingdom). This includes:",
        "",
        "- Employee personal information",
        "- Client contact details",
        "- End-user personal data in OV-built products",
        "- Contractor identity documents",
        "",
        "---", "",
        "## 5. Client Intellectual Property",
        "",
        "All client source code, architecture documents, business requirements and project "
        "deliverables are classified as CONFIDENTIAL by default, regardless of any other "
        "labelling. Client IP must only be stored in OV-approved and client-approved systems.",
        "",
        "---", "",
        f"*{COMPANY['name']} | {COMPANY['website']} | Related: OV-POL-001, OV-SOA-001*",
    ]
    path = os.path.join(OUTPUT_DIR, 'OV-POL-006-Data-Classification-Policy.md')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print(f"  ✅ OV-POL-006 Data Classification Policy → {path}")
    return path
 
 
def generate_all_policies():
    print("\n📄 Generating ISMS Policy Documents...")
    paths = []
    paths.append(generate_information_security_policy())
    paths.append(generate_acceptable_use_policy())
    paths.append(generate_access_control_policy())
    paths.append(generate_incident_response_policy())
    paths.append(generate_remote_working_policy())
    paths.append(generate_data_classification_policy())
    print(f"  ✅ {len(paths)} policy documents generated")
    return paths
 
 
if __name__ == "__main__":
    generate_all_policies()
 