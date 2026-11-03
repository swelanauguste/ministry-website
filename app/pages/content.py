"""Curated homepage content, shared by full-page and HTMX responses."""

SEARCH_SECTIONS = (
    ("About the ministry", "about", "about infrastructure ministry communities"),
    ("Roads, infrastructure and public works", "our-work", "road infrastructure works technical"),
    ("Ports and connectivity", "our-work", "port sea ship airport slaspa"),
    ("Driver and vehicle services", "services", "transport driving licence license permit vehicle"),
    ("Electrical certification and materials testing", "services", "electrical certification construction materials testing services"),
    ("Projects and programmes", "projects", "millennium highway west coast reconstruction projects"),
    ("News and public notices", "updates", "news notices tenders procurement announcements"),
    ("Publications and policy documents", "publications", "publications policies plans documents resources"),
    ("Contact the ministry", "contact", "contact address union castries help directory"),
)

UPDATES = (
    {
        "category": "notice", "label": "NOTICE ARCHIVE",
        "title": "Hewanorra International Airport: request for proposals",
        "url": "https://infrastructure.govt.lc/news/slaspa--request-for-proposals",
        "description": "SLASPA’s published notice for the completion of the air traffic control tower.",
        "date_label": "21 January 2025",
    },
    {
        "category": "publication", "label": "PUBLICATION",
        "title": "Plans, policies and project documents",
        "url": "https://infrastructure.govt.lc/publications",
        "description": "Browse ministry publications, including stakeholder engagement plans and policy resources.",
        "date_label": "Ministry resources",
    },
    {
        "category": "notice", "label": "PUBLIC NOTICES",
        "title": "Stay connected to ministry announcements",
        "url": "https://infrastructure.govt.lc/notices",
        "description": "Find official notices, procurement opportunities and information for the public.",
        "date_label": "Official notice board",
    },
)

UPDATE_FILTERS = (("all", "All updates"), ("notice", "Notices"), ("publication", "Publications"))
