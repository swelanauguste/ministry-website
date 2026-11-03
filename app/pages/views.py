from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.vary import vary_on_headers

from .content import SEARCH_SECTIONS, UPDATE_FILTERS, UPDATES


def homepage_context(request):
    category = request.GET.get("category", "all")
    if category not in dict(UPDATE_FILTERS):
        category = "all"
    query = request.GET.get("q", "").strip()[:200]
    terms = query.casefold().split()
    results = [
        {"title": title, "anchor": anchor}
        for title, anchor, keywords in SEARCH_SECTIONS
        if terms and all(term in f"{title} {keywords}".casefold() for term in terms)
    ]
    return {
        "category": category,
        "filters": UPDATE_FILTERS,
        "updates": [item for item in UPDATES if category == "all" or item["category"] == category],
        "query": query,
        "search_results": results,
        "search_submitted": "q" in request.GET,
    }


@require_GET
def home(request):
    return render(request, "home.html", homepage_context(request))


@require_GET
@vary_on_headers("HX-Request")
def search(request):
    template = "partials/search-results.html" if request.headers.get("HX-Request") == "true" else "home.html"
    return render(request, template, homepage_context(request))


@require_GET
@vary_on_headers("HX-Request")
def updates(request):
    template = "partials/updates.html" if request.headers.get("HX-Request") == "true" else "home.html"
    return render(request, template, homepage_context(request))
