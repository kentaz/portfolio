"""Generate a one-page resume PDF for Kenneth Tafadzwa Zendera."""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepInFrame,
)


def build_resume(path: str) -> None:
    doc = SimpleDocTemplate(
        path,
        pagesize=LETTER,
        leftMargin=0.7 * inch,
        rightMargin=0.7 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Kenneth Tafadzwa Zendera — Resume",
        author="Kenneth Tafadzwa Zendera",
    )

    navy = HexColor("#0B1929")
    cyan = HexColor("#00A3C4")
    muted = HexColor("#5A7A9A")
    body = HexColor("#1A3050")

    name_style = ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=22,
        textColor=navy, leading=26, spaceAfter=2,
    )
    role_style = ParagraphStyle(
        "role", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=cyan, leading=13, spaceAfter=8,
    )
    meta_style = ParagraphStyle(
        "meta", fontName="Helvetica", fontSize=9,
        textColor=muted, leading=11,
    )
    section_style = ParagraphStyle(
        "section", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=navy, leading=13, spaceBefore=10, spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=9,
        textColor=body, leading=12,
    )
    bullet_style = ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=9,
        textColor=body, leading=12, leftIndent=10,
        bulletIndent=0,
    )

    flow = []

    # Header
    flow.append(Paragraph("Kenneth Tafadzwa Zendera", name_style))
    flow.append(Paragraph(
        "Cloud &amp; AI Governance Engineer &middot; ISO 42001/27001/27701 Lead Auditor &middot; Builder of ComplyAgent",
        role_style,
    ))
    flow.append(Paragraph(
        "Cape Town, South Africa &middot; UTC+2 &middot; kentaz23@hotmail.com &middot; github.com/kentaz &middot; linkedin.com/in/kenneth-tafadzwa-z-57954467",
        meta_style,
    ))

    # Summary
    flow.append(Paragraph("Summary", section_style))
    flow.append(Paragraph(
        "Six years across SOC engineering, cloud automation, and solutions architecture. "
        "Design, secure, and govern AWS infrastructure at the organisation level — landing zones, multi-account Terraform, security baselines. "
        "On the AI side: implement governance programmes aligned to the EU AI Act, NIST AI RMF, and ISO 42001, and build the tooling that proves compliance — currently shipping ComplyAgent, an open-source platform for EU AI Act audit-ready evidence collection.",
        body_style,
    ))

    # What I'm offering now
    flow.append(Paragraph("Available for", section_style))
    flow.append(Paragraph("• EU AI Act readiness assessments &amp; control mapping for SaaS companies deploying AI in the EU", bullet_style))
    flow.append(Paragraph("• Fractional CISO engagements (3–6 months) for Series A–C startups", bullet_style))
    flow.append(Paragraph("• Cloud security architecture — AWS multi-account design, Terraform modules, baseline implementation", bullet_style))
    flow.append(Paragraph("• AI governance programme design — ISO 42001 implementation, NIST AI RMF alignment, vendor risk assessment", bullet_style))

    # Selected projects
    flow.append(Paragraph("Selected projects", section_style))
    projects = [
        ("complyagent (github.com/kentaz/complyagent)",
         "EU AI Act audit-ready evidence collection for AI agent deployments — signed audit trails, OPA policy evaluation, PDF reports"),
        ("ai-governance-toolkit (github.com/kentaz/ai-governance-toolkit)",
         "Practitioner templates for EU AI Act risk classification, ISO 42001 audit, NIST AI RMF, incident response, vendor assessment"),
        ("terraform-aws-security-baseline",
         "Reusable module enabling Security Hub, GuardDuty, Config, CloudTrail+KMS, IAM Access Analyzer — ISO 27001 aligned"),
        ("terraform-aws-bedrock-governance",
         "Private VPC-endpointed Bedrock with Guardrails and CloudWatch monitoring — resources annotated to ISO 42001 controls"),
        ("aws-cwagent-deployer",
         "Self-healing CloudWatch Agent deployment via SSM State Manager with ASG-dimensioned alarms"),
        ("aws-cost-auditor",
         "Read-only cross-account cost reporting with MoM variance flagging and EC2 rightsizing — CloudShell-native"),
    ]
    project_rows = [[Paragraph(f"<b>{name}</b>", body_style),
                     Paragraph(desc, body_style)] for name, desc in projects]
    project_table = Table(
        project_rows,
        colWidths=[2.4 * inch, 4.6 * inch],
        hAlign="LEFT",
    )
    project_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
    ]))
    flow.append(project_table)

    # Experience
    flow.append(Paragraph("Experience", section_style))
    flow.append(Paragraph(
        "<b>Cloud &amp; AI Governance Engineer — MSP delivery</b> (current)",
        body_style,
    ))
    flow.append(Paragraph(
        "Run cloud and AI governance delivery across two AWS Organizations. "
        "Design multi-account landing zones, author production Terraform, lead ISO 27001 / 42001 control implementation, "
        "and build the cross-account automation (Bash + Python) that keeps it all running.",
        bullet_style,
    ))
    flow.append(Paragraph(
        "<b>Solutions Architect &amp; Cloud Security Engineer — earlier roles</b>",
        body_style,
    ))
    flow.append(Paragraph(
        "Designed and secured AWS workloads across SaaS and enterprise clients. "
        "Led migrations: GCP → AWS, RDS Blue/Green, IAM → IAM Identity Center, S3 + CloudFront OAC cutovers. "
        "Built incident response runbooks, CloudWatch alarm frameworks, and cost auditing tooling.",
        bullet_style,
    ))

    # Certifications
    flow.append(Paragraph("Certifications", section_style))
    certs = [
        "AWS Solutions Architect — Professional (2025)",
        "AWS Security — Specialty (2024)",
        "AWS Solutions Architect — Associate (2023)",
        "AWS SysOps Administrator — Associate (2023)",
        "OCI 2025 Multicloud Architect Professional (2025)",
        "ISC2 Certified in Cybersecurity (2024)",
        "ISO/IEC 42001:2023 Lead Auditor — Mastermind (2025)",
        "ISO/IEC 27001:2022 Lead Auditor — Mastermind (2025)",
        "ISO/IEC 27701:2025 Lead Auditor — Mastermind (2026)",
        "Fellow of Management Systems Auditing (2026)",
    ]
    cert_data = [[Paragraph(f"• {c}", bullet_style) for c in certs[i:i + 2]] for i in range(0, len(certs), 2)]
    cert_table = Table(cert_data, colWidths=[3.5 * inch, 3.5 * inch], hAlign="LEFT")
    cert_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
    ]))
    flow.append(cert_table)

    # Tech stack
    flow.append(Paragraph("Tech stack", section_style))
    stack = Paragraph(
        "<b>Cloud:</b> AWS (Control Tower, Organizations, IAM Identity Center, EC2, ECS, EKS, RDS, Lambda, CloudFront, Bedrock, VPC, Security Hub, GuardDuty, Config, CloudWatch), Azure, Oracle Cloud "
        "&nbsp; <b>IaC &amp; CI/CD:</b> Terraform, CloudFormation, GitLab CI, GitHub Actions, TFSec, Checkov "
        "&nbsp; <b>Automation:</b> Bash, Python, AWS CLI, SSM "
        "&nbsp; <b>Containers:</b> Docker, Kubernetes (EKS) "
        "&nbsp; <b>Governance:</b> EU AI Act, NIST AI RMF, ISO 42001, ISO 27001, ISO 27701, CIS Benchmarks",
        body_style,
    )
    flow.append(stack)

    # Education
    flow.append(Paragraph("Education", section_style))
    flow.append(Paragraph(
        "Bachelor of Technology, International Marketing — Chinhoyi University of Technology, Zimbabwe",
        body_style,
    ))

    # Wrap everything in a frame so it fits on one page; shrink if needed
    frame_content = KeepInFrame(
        maxWidth=7.1 * inch,
        maxHeight=10.0 * inch,
        content=flow,
        mode="shrink",
    )

    doc.build([frame_content])


if __name__ == "__main__":
    out = "/Users/kentaz/Documents/portfolio-site/Kenneth-Zendera-Resume.pdf"
    build_resume(out)
    print(f"Wrote {out}")