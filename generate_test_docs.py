"""Generate synthetic Saudi enterprise test documents for Wathiqa demo."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
)
from reportlab.lib import colors

styles = getSampleStyleSheet()
TITLE = ParagraphStyle("T", parent=styles["Title"], fontSize=22, spaceAfter=20,
                       textColor=colors.HexColor("#006C35"))
H1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=15, spaceAfter=12,
                    textColor=colors.HexColor("#006C35"))
H2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12, spaceAfter=8)
BODY = ParagraphStyle("B", parent=styles["BodyText"], fontSize=10.5,
                      alignment=TA_JUSTIFY, spaceAfter=8, leading=15)
SMALL = ParagraphStyle("S", parent=styles["BodyText"], fontSize=9,
                       alignment=TA_CENTER, textColor=colors.grey)


def p(text, style=BODY):
    return Paragraph(text, style)


def filler(topic, n=4):
    """Return n paragraphs of realistic legal filler text."""
    templates = [
        f"Each Party shall comply with all applicable laws and regulations of the Kingdom of Saudi Arabia in connection with {topic}, including but not limited to any circulars, rules, or directives issued by the relevant regulatory authorities from time to time.",
        f"Any breach of the obligations set out in this section concerning {topic} shall entitle the non-breaching Party to seek appropriate remedies, including but not limited to specific performance, injunctive relief, and recovery of direct losses.",
        f"The obligations relating to {topic} shall survive the termination or expiration of this Agreement to the extent necessary to give full effect to their intent and purpose.",
        f"Nothing in this section shall be construed to limit or exclude any rights or remedies available to either Party under the laws of the Kingdom of Saudi Arabia concerning {topic}.",
        f"Both Parties acknowledge that the matters described in this section relating to {topic} are material to the performance of this Agreement and shall be carried out with due care, skill, and diligence.",
        f"All communications, notices, and documentation in connection with {topic} shall be made in writing in both Arabic and English, and the English version shall prevail in case of any inconsistency.",
    ]
    out = []
    for i in range(n):
        out.append(p(templates[i % len(templates)]))
    return out


def build_agreement(path):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    s = []

    # Cover page
    s.append(Spacer(1, 4*cm))
    s.append(p("SERVICE AGREEMENT", TITLE))
    s.append(Spacer(1, 1*cm))
    s.append(p("Between", H2))
    s.append(p("Al-Riyadh Trading Company (CR 1010123456)", BODY))
    s.append(p("And", H2))
    s.append(p("NEOM Contractors LLC (CR 4030987654)", BODY))
    s.append(Spacer(1, 2*cm))
    s.append(p("Contract Number: SA-2026-0042", BODY))
    s.append(p("Effective Date: 01/01/2026", BODY))
    s.append(p("Expiration Date: 31/12/2027", BODY))
    s.append(p("Total Contract Value: SAR 4,250,000", BODY))
    s.append(Spacer(1, 3*cm))
    s.append(p("CONFIDENTIAL — For internal use only", SMALL))
    s.append(PageBreak())

    # Parties
    s.append(p("1. Parties", H1))
    s.append(p("This Service Agreement (the &quot;Agreement&quot;) is entered into as of 01/01/2026 (the &quot;Effective Date&quot;) by and between:", BODY))
    s.append(p("<b>Al-Riyadh Trading Company</b>, a company incorporated under the laws of the Kingdom of Saudi Arabia with Commercial Registration number 1010123456, having its registered office at King Fahd Road, Riyadh, and represented by Mr. Abdullah Al-Qahtani, National ID 1023456789, contact number +966512345678, email contracts@alriyadh-trading.sa (the &quot;Client&quot;).", BODY))
    s.append(p("<b>NEOM Contractors LLC</b>, a company incorporated under the laws of the Kingdom of Saudi Arabia with Commercial Registration number 4030987654, having its registered office at NEOM Business District, Tabuk Province, represented by Ms. Fatima Al-Zahrani, National ID 2019876543, contact number +966555987654, email info@neom-contractors.sa (the &quot;Contractor&quot;).", BODY))
    s.append(p("The Client and the Contractor are hereinafter referred to individually as a &quot;Party&quot; and collectively as the &quot;Parties&quot;.", BODY))
    s.append(PageBreak())

    # Recitals
    s.append(p("2. Recitals", H1))
    for para in filler("the background and purpose of this Agreement", 5):
        s.append(para)
    s.append(PageBreak())

    # Definitions
    s.append(p("3. Definitions and Interpretation", H1))
    s.append(p("In this Agreement, unless the context otherwise requires, the following terms shall have the meanings set out below:", BODY))
    defs = [
        ("&quot;Business Day&quot;", "means any day other than a Friday, Saturday, or public holiday in the Kingdom of Saudi Arabia."),
        ("&quot;Confidential Information&quot;", "means all non-public information disclosed by one Party to the other, whether orally, in writing, or in any other form."),
        ("&quot;Deliverables&quot;", "means all reports, documents, software, and other materials to be provided by the Contractor under this Agreement."),
        ("&quot;Force Majeure&quot;", "means any event beyond the reasonable control of a Party, including but not limited to acts of God, war, pandemics, or government actions."),
        ("&quot;Governing Law&quot;", "means the laws of the Kingdom of Saudi Arabia as applied by its competent courts."),
        ("&quot;Intellectual Property Rights&quot;", "means all patents, copyrights, trade secrets, trademarks, and other proprietary rights of any kind."),
        ("&quot;Services&quot;", "means the services described in Section 5 and Appendix A to this Agreement."),
        ("&quot;Term&quot;", "means the period commencing on the Effective Date and ending on the Expiration Date, subject to renewal or termination."),
    ]
    for term, definition in defs:
        s.append(p(f"<b>{term}</b> {definition}", BODY))
    for para in filler("interpretation of defined terms", 3):
        s.append(para)
    s.append(PageBreak())

    # Scope of services
    s.append(p("4. Scope of Services", H1))
    s.append(p("The Contractor shall provide the following services (the &quot;Services&quot;) to the Client:", BODY))
    for para in filler("the scope, manner, and standards of the Services", 8):
        s.append(para)
    s.append(PageBreak())

    # Term
    s.append(p("5. Term and Renewal", H1))
    s.append(p("This Agreement shall commence on the Effective Date (01/01/2026) and shall remain in full force and effect until the Expiration Date (31/12/2027), unless terminated earlier in accordance with Section 12.", BODY))
    s.append(p("The Agreement may be renewed for additional one-year periods by mutual written consent of the Parties, provided that either Party gives at least <b>ninety (90) days</b> written notice prior to the Expiration Date.", BODY))
    for para in filler("renewal, extension, and term-related matters", 5):
        s.append(para)
    s.append(PageBreak())

    # Fees
    s.append(p("6. Fees and Payment", H1))
    s.append(p("The Client shall pay the Contractor a total contract value of <b>SAR 4,250,000</b> (Four Million Two Hundred Fifty Thousand Saudi Riyals) inclusive of all applicable taxes and fees, unless otherwise stated.", BODY))
    s.append(p("Payment shall be made in quarterly installments of SAR 1,062,500 each, due within thirty (30) days of receipt of a valid invoice.", BODY))
    s.append(p("All payments shall be made by bank transfer to the following account:", BODY))
    s.append(p("Account Name: NEOM Contractors LLC<br/>IBAN: <b>SA0380000000608010167519</b><br/>Bank: Saudi National Bank<br/>SWIFT: NCBKSAJEXXX", BODY))
    for para in filler("payment terms, invoicing, and currency matters", 4):
        s.append(para)
    s.append(PageBreak())

    # Confidentiality
    s.append(p("7. Confidentiality", H1))
    for para in filler("confidentiality obligations and exceptions", 7):
        s.append(para)
    s.append(PageBreak())

    # Data protection
    s.append(p("8. Data Protection and Privacy", H1))
    s.append(p("Both Parties shall comply with the Personal Data Protection Law (PDPL) of the Kingdom of Saudi Arabia and any regulations issued by the Saudi Data and Artificial Intelligence Authority (SDAIA).", BODY))
    s.append(p("Personal data collected under this Agreement shall be processed lawfully, stored securely, and retained only as long as necessary for the purposes for which it was collected.", BODY))
    for para in filler("data protection, privacy, and information security", 5):
        s.append(para)
    s.append(PageBreak())

    # IP
    s.append(p("9. Intellectual Property", H1))
    for para in filler("intellectual property ownership and licensing", 6):
        s.append(para)
    s.append(PageBreak())

    # Warranties
    s.append(p("10. Representations and Warranties", H1))
    for para in filler("representations, warranties, and covenants", 6):
        s.append(para)
    s.append(PageBreak())

    # Liability
    s.append(p("11. Limitation of Liability", H1))
    for para in filler("limitation of liability and indemnification", 6):
        s.append(para)
    s.append(PageBreak())

    # Termination
    s.append(p("12. Termination", H1))
    s.append(p("Either Party may terminate this Agreement for material breach upon <b>thirty (30) days</b> written notice, provided the breach remains uncured at the end of such period.", BODY))
    s.append(p("Either Party may terminate this Agreement for convenience upon <b>ninety (90) days</b> prior written notice to the other Party.", BODY))
    for para in filler("termination rights, effects, and consequences", 6):
        s.append(para)
    s.append(PageBreak())

    # Dispute resolution
    s.append(p("13. Governing Law and Dispute Resolution", H1))
    s.append(p("This Agreement shall be governed by and construed in accordance with the laws of the Kingdom of Saudi Arabia.", BODY))
    s.append(p("Any dispute arising out of or in connection with this Agreement shall first be resolved through good-faith negotiations. If unresolved within sixty (60) days, the dispute shall be referred to the competent courts of Riyadh.", BODY))
    for para in filler("dispute resolution and jurisdiction", 4):
        s.append(para)
    s.append(PageBreak())

    # General
    s.append(p("14. General Provisions", H1))
    for para in filler("general contractual provisions including notices, assignment, and severability", 8):
        s.append(para)
    s.append(PageBreak())

    # Signatures
    s.append(p("15. Signatures", H1))
    s.append(p("IN WITNESS WHEREOF, the Parties have executed this Agreement as of the Effective Date.", BODY))
    s.append(Spacer(1, 1.5*cm))
    s.append(p("<b>For Al-Riyadh Trading Company</b><br/>Mr. Abdullah Al-Qahtani<br/>National ID: 1023456789<br/>Signature: ___________________<br/>Date: 01/01/2026", BODY))
    s.append(Spacer(1, 1.5*cm))
    s.append(p("<b>For NEOM Contractors LLC</b><br/>Ms. Fatima Al-Zahrani<br/>National ID: 2019876543<br/>Signature: ___________________<br/>Date: 01/01/2026", BODY))
    s.append(PageBreak())

    # Arabic summary
    s.append(p("ملخص عربي (Arabic Summary)", H1))
    s.append(p("هذا الاتفاق مبرم بين شركة الرياض التجارية وشركة نيوم للمقاولات. تبلغ القيمة الإجمالية للعقد أربعة ملايين ومئتان وخمسون ألف ريال سعودي. تبدأ مدة الاتفاق في 01/01/2026 وتنتهي في 31/12/2027.", BODY))
    s.append(p("رقم الآيبان للدفع: SA0380000000608010167519", BODY))
    s.append(p("رقم الجوال للتواصل: +966512345678", BODY))
    s.append(p("البريد الإلكتروني: contracts@alriyadh-trading.sa", BODY))
    s.append(Spacer(1, 1*cm))
    s.append(p("End of Document", SMALL))

    doc.build(s)
    print(f"Generated: {path}")


def build_pdpl_policy(path):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    s = []
    s.append(Spacer(1, 3*cm))
    s.append(p("DATA PROTECTION POLICY", TITLE))
    s.append(Spacer(1, 0.5*cm))
    s.append(p("Saudi National Bank — Internal Policy Document", H2))
    s.append(p("Version 3.2 · Effective 01/01/2026", BODY))
    s.append(p("Reference: SNB-PDPL-2026-003", BODY))
    s.append(p("Data Protection Officer: Khalid Al-Otaibi, National ID 1056789012, email dpo@snb-pdpl.sa, phone +966503456789", BODY))
    s.append(PageBreak())

    sections = [
        ("1. Purpose and Scope", "This policy sets out the principles, obligations, and procedures that Saudi National Bank (the &quot;Bank&quot;) follows to comply with the Personal Data Protection Law (PDPL) of the Kingdom of Saudi Arabia and the directives of the Saudi Data and Artificial Intelligence Authority (SDAIA).", 5),
        ("2. Definitions", "Terms such as &quot;Personal Data&quot;, &quot;Sensitive Data&quot;, &quot;Data Subject&quot;, &quot;Processing&quot;, and &quot;Controller&quot; shall have the meanings assigned to them under the PDPL and its Implementing Regulations.", 5),
        ("3. Lawful Basis for Processing", "The Bank shall process personal data only where a lawful basis exists, including consent, contractual necessity, legal obligation, vital interests, public interest, or legitimate interests, in accordance with Article 4 of the PDPL.", 7),
        ("4. Data Subject Rights", "Data subjects have the right to be informed, to access their personal data, to request correction, to request destruction, and to withdraw consent, subject to applicable legal restrictions.", 7),
        ("5. Data Retention", "Personal data shall be retained only for as long as necessary to fulfil the purpose for which it was collected, or as required by applicable laws, after which it shall be securely destroyed.", 6),
        ("6. Cross-Border Transfers", "Personal data shall not be transferred outside the Kingdom of Saudi Arabia unless the requirements of Article 29 of the PDPL are met, including an adequate level of protection or the existence of appropriate safeguards.", 6),
        ("7. Data Security", "The Bank shall implement appropriate technical and organisational measures, including encryption, access controls, and regular audits, to protect personal data against unauthorised access, alteration, or disclosure.", 7),
        ("8. Breach Notification", "Any personal data breach shall be reported to SDAIA within seventy-two (72) hours of becoming aware of the breach, and affected data subjects shall be notified where the breach poses a high risk to their rights.", 6),
        ("9. Roles and Responsibilities", "The Data Protection Officer (DPO) shall oversee compliance with this policy, act as the point of contact with SDAIA, and provide guidance to all departments on data protection matters.", 6),
        ("10. Training and Awareness", "All employees who process personal data shall complete mandatory annual training on PDPL compliance and data protection best practices.", 5),
        ("11. Audit and Review", "This policy shall be reviewed at least annually and audited by the internal audit function to ensure continued effectiveness and alignment with regulatory requirements.", 5),
        ("12. Sanctions", "Non-compliance with this policy may result in disciplinary action, up to and including termination of employment, and may also give rise to civil or criminal liability under the PDPL.", 5),
    ]
    for title, intro, n in sections:
        s.append(p(title, H1))
        s.append(p(intro, BODY))
        for para in filler(title.lower(), n):
            s.append(para)
        s.append(PageBreak())

    s.append(p("Arabic Section / القسم العربي", H1))
    s.append(p("تلتزم المؤسسة بأحكام نظام حماية البيانات الشخصية في المملكة العربية السعودية الصادر بموجب المرسوم الملكي رقم م/19. يجب معالجة البيانات الشخصية بشكل قانوني وشفاف ولأغراض محددة ومشروعة فقط.", BODY))
    s.append(p("للاستفسار، يُرجى التواصل مع مسؤول حماية البيانات عبر البريد الإلكتروني dpo@snb-pdpl.sa أو الهاتف +966503456789.", BODY))

    doc.build(s)
    print(f"Generated: {path}")


if __name__ == "__main__":
    import os
    os.makedirs("data", exist_ok=True)
    build_agreement("data/saudi_service_agreement.pdf")
    build_pdpl_policy("data/saudi_pdpl_policy.pdf")
    print("\nDone. Files saved in the data/ folder.")