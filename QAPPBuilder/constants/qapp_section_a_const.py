# NOTE: This will also house constants for the Qapp model
#       as well as shared constants across sections.
QAPP_TITLE_HEADER = 'U.S. Environmental Protection Agency ' + \
    'Office of Research and Development'
QAPP_STR = 'Quality Assurance Project Plan (QAPP)'

QA_CATEGORY_A = 'A'
QA_CATEGORY_B = 'B'
QA_CATEGORY_OPTIONS = (
    (QA_CATEGORY_A, QA_CATEGORY_A),
    (QA_CATEGORY_B, QA_CATEGORY_B),
)

INTRAMURALLY = 'Intramurally'
EXTRAMURALLY = 'Extramurally'
INTRA_EXTRA_CHOICES = (
    (INTRAMURALLY, INTRAMURALLY),
    (EXTRAMURALLY, EXTRAMURALLY),
)

INTRAMURAL_TEXT = 'Period of Applicability for intramural QAPPs starts on ' + \
    'the date of QAPP approval and ends five years after QAPP approval ' + \
    'date or until a new version of the QAPP is approved, whichever is sooner.'

EXTRAMURAL_TEXT = 'Period of Applicability for extramural QAPPs starts on ' + \
    'the date of QAPP approval and ends on the last day of the POP or ' + \
    'until a new version of the QAPP is approved, whichever is sooner, and ' + \
    'not to exceed 5 years.'

CCTE = 'Center for Computational Toxicology & Exposure'
CEMM = 'Center for Environmental Measurement and Modeling'
CESER = 'Center for Environmental Solutions & Emergency Response'
CPHEA = 'Center for Public Health and Environmental Assessments'
ORM = 'Office of Resource Management'
OSAPE = 'Office of Science Advisor, Policy & Engagement'

ORD_CENTER_OPTIONS = (
    (CCTE, CCTE), (CEMM, CEMM), (CESER, CESER),
    (CPHEA, CPHEA), (ORM, ORM), (OSAPE, OSAPE)
)

CURRENT_FY = 2025
QUARTERS = ['Q1', 'Q2', 'Q3', 'Q4']

FY_QUARTERS = [
    f'FY{CURRENT_FY-1} {QUARTERS[3]}',  # FY24 Q4
    f'FY{CURRENT_FY} {QUARTERS[0]}',    # FY25 Q1
    f'FY{CURRENT_FY} {QUARTERS[1]}',    # FY25 Q2
    f'FY{CURRENT_FY} {QUARTERS[2]}',    # FY25 Q3
    f'FY{CURRENT_FY} {QUARTERS[3]}',    # FY25 Q4
    f'FY{CURRENT_FY+1} {QUARTERS[0]}',  # FY26 Q1
    f'FY{CURRENT_FY+1} {QUARTERS[1]}',  # FY26 Q2
    f'FY{CURRENT_FY+1} {QUARTERS[2]}',  # FY26 Q3
]

PROJ_ROLES_RESPONSIBILITIES = {
    'QA Manager': [
        'Provides QA training/review on the ORD QA Program.',
        'Assists the ORD TL in ensuring that quality requirements are identified for the project.',  # noqa: E501
        'Reviews and approves QAPP.',
        'Reviews and approves ORD sub-products and products developed under the project QAPP.',  # noqa: E501
        'Reports quality related issues to the TL\'s supervisor and organization\'s senior manager.'  # noqa: E501
    ],
    'Branch Chief': [
        'Consults with TL and QAM on QA category designation.',
        'Reviews and approves QAPP.',
        'Communicates regularly with project TL to ensure that QA requirements are met.',  # noqa: E501
        'Evaluates and seeks to provide the necessary resources to accomplish the work described in the QAPP.',  # noqa: E501
        'Ensures that no EIO begins until the QA documentation is approved.'
    ],
    'Division Director': [
        'Provides the necessary resources (personnel, funding, materials, supplies, and time) to accomplish the work described in the project QAPP.',  # noqa: E501
        'Ensures the roles and responsibilities of division personnel meet project specific and organizational specific requirements as specified in QAPPs and the ORD QMP'  # noqa: E501
    ],
    'Technical Lead': [
        'Maintains and distributes the official, approved copy of this QAPP to project EIO participants.',  # noqa: E501
        'Reviews project QAPP annually for consistency with the current EIO of the project and updates the QAPP to match the current EIO of the project as necessary.',  # noqa: E501
        'Notifies their QAM in writing of any quality related issue or deviation from QA documentation.',  # noqa: E501
    ]
}

# Create a copy of the dictionary without the "Division Director" role
# This is for distribution defaults, which are almost the same as above...
DISTRIBUTION_LIST_DEFAULT_ROLES = {
    key: value for key, value
    in PROJ_ROLES_RESPONSIBILITIES.items()
    if key != 'Division Director'
}

SECTION_A = {
    'a': {'header': 'A: Project Management and Information/Data Quality Objectives'},  # noqa: E501
    'a1': {
        'header': 'A1: Title Page',
        'labels': {
            'qapp': 'QAPP',
            'ord_center': 'ORD Center',
            'division': 'Division',
            'branch': 'Branch',
            'title': 'Title',
            'ord_national_program': 'ORD National Program',
            'version_date': 'Version Date',
            'proj_qapp_id': 'Project QAPP ID (QA Track ID)',
            'qa_category': 'QA Category',
            'intra_or_extra': 'QAPP Developed Intra-or-Extramurally',
            'vehicle_num': 'Vehicle #',
            'non_epa_org': 'Name of Non-EPA Organization',
            'period_performance': 'Period of Performance (POP)',
            'accessibility': 'QAPP Accessibility'
        }
    },
    'a2': {
        'header': 'A2: Approval Page',
        'labels': {
            'ord_technical_lead': 'ORD Technical Lead (TL)',
            'ord_tl_supervisor': 'ORD Technical Lead\'s Supervisor',
            'ord_qa_manager': 'ORD QA Manager',
            'extramural_technical_manager': 'Extramural Technical Manager',
            'extramural_qa_manager': 'Extramural QA Manager'
        }
    },
    'a3': {
        'header': 'A3: Table of Contents, Document Format, and Document Control'
    },
    'a4': {
        'header': 'A4: Project Purpose, Problem Definition, and Background',
        'boilerplate': 'Environmental information operations (EIO) conducted under this Quality Assurance Project Plan (QAPP) will adhere to the requirements specified in the Office of Research and Development (ORD) Quality Management Plan (QMP). ',  # noqa: E501
        'labels': {
            'project_background': 'A4.1: Project Background',
            'project_purpose': 'A4.2: Project Purpose and Problem Definition'
        }
    },
    'a5': {
        'header': 'A5: Project Task Description',
        'boilerplate': 'The Table below lists expected tasks and products for this project in relation to their anticipated start and projected end dates by Fiscal Year (FY).',  # noqa: E501
        'labels': {
            'tasks_summary': 'Tasks Summary',
            'start_fy': 'Starting Fiscal Year (FY)',
            'start_q': 'Starting Quarter'
        }
    },
    'a6': {
        'header': 'A6: Information/Data Quality Objectives and Performance/Acceptance Criteria',  # noqa: E501
        'labels': {
            'information': 'A6: Information/Data Quality Objectives and Performance/Acceptance Criteria'  # noqa: E501
        }
    },
    'a7': {
        'header': 'A7: Distribution List',
        'boilerplate': 'The EPA Technical Lead (TL) is responsible for maintaining a copy of the original approved QAPP and all approved subsequent revisions of the QAPP within their project file. The Technical Lead (TL) is responsible for the distribution of the most current signed approved version of the QAPP to participants as indicated in Table 2 below.'  # noqa: E501
    },
    'a8': {
        'header': 'A8: Project Organization',
        'boilerplate': 'The roles and responsibilities of individuals involved in performing research activities and developing products within this project are identified in the below Table.'  # noqa: E501
    },
    'a9': {
        'header': 'A9: Project Quality Assurance Manager Independence',
        'boilerplate': 'ORD QA Managers are independent from all EIO for any project for which they serve as Project QA Manager for, as indicated in the ORD QMP and Table 3 within Section A8 of this QAPP. \nFigure 1 in Section A10, shows the independence of ORD Project QA Manager from the project participants and EIO within this project.'  # noqa: E501
    },
    'a10': {
        'header': 'A10: Project Organization Chart and Communications',
        'boilerplate': 'Figure 1 organization chart provides a visual representation of the working relationships and lines of communication among all project participants identified in Table 3. Any issues identified by an individual within the project will notify the TL. The TL will notify their QA Manager in writing of any quality related issue or deviation from QA Documentation. The QA Manager has the authority to access and discuss quality related issues with their organization\'s senior manager.'  # noqa: E501
    },
    'a11': {
        'header': 'A11: Personnel Training/Certification',
        'labels': {
            'information': 'A11: Personnel Training/Certification'
        }
    },
    'a12': {
        'header': 'A12: Documents and Records',
        'boilerplate': 'Research activities must be documented according to the requirements of ORD QA Policies titled Scientific Recordkeeping: Paper, Scientific Recordkeeping: Electronic, and Quality Assurance/Quality Control Practices for ORD Laboratory and Field-Based Research, as well as requirements defined in this QA Project Plan.\n'  # noqa: E501
        'The ORD QA Policies require the use of research notebooks and the management of research records, both paper and electronic, such that project research data generation may continue even if a researcher or an analyst participating in the project leaves the project staff.\n'  # noqa: E501
        'Detailed information regarding project file location and managing of data can be found in section B7.\n'  # noqa: E501
        'Table 4 provides a list of documents and records that will be generated for this project, the parties responsible for generating and updating those records, storage locations, and file types. The ORD technical lead will be responsible for maintaining a copy of all file records in accordance with the EPA records schedule identified in Table 5.'  # noqa: E501
    }
}

TABLE_5_BOILERPLATE = {
    'col_headers': [
        'EPA Records No. and Series Title', 'Brief Description',
        'Final Disposition', 'QA Category'
    ],
    'qa_category_a': [
        '1035(a): Historically significant environmental programs and project records',  # noqa: E501
        'Applied and directed scientific research project files for projects conducted by EPA personnel in the Office of Research and Development (ORD) laboratories that directly support rulemaking, enforcement, regulatory, or policy decisions, research of high programmatic relevance, and research of significant national interest (e.g., technology transfer projects which may be critical to the award of a patent or other important commercial or legal decision), consisting of research plans, research methodology, questionnaires, quality assurance project plans, raw data, laboratory notebooks, correspondence, reports, peer reviews, quality assurance assessments, and related records.',  # noqa: E501
        'Permanent', 'Cat A'
    ],
    'qa_category_b': [
        '1035(b): Long-term environmental program and project records',
        'Includes records that are not required for documenting the history of the program or project, but which have operational value to EPA throughout the life of the program or project.',  # noqa: E501
        '20 Years', 'Cat B'
    ]
}
