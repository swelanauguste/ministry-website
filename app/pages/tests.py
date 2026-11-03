from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_home_keeps_design_and_loads_local_libraries(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Stronger connections.")
        self.assertContains(response, "castries-harbour.jpg")
        self.assertContains(response, "vendor/alpine-3.14.9.min.js")
        self.assertContains(response, "vendor/htmx-2.0.11.min.js")
        self.assertContains(response, 'x-data="ministrySite"')
        self.assertContains(response, 'class="update-card"', count=3)

    def test_search_returns_fragment_for_htmx(self):
        response = self.client.get(reverse("search"), {"q": "DRIVER vehicle"}, HTTP_HX_REQUEST="true")
        self.assertContains(response, "Driver and vehicle services")
        self.assertNotContains(response, "<!doctype html>")
        self.assertNotContains(response, "Ports and connectivity")
        self.assertIn("HX-Request", response.headers["Vary"])

    def test_search_has_empty_state(self):
        for query in ("", "   ", "no-such-section"):
            with self.subTest(query=query):
                response = self.client.get(reverse("search"), {"q": query}, HTTP_HX_REQUEST="true")
                self.assertContains(response, "No matching sections")

    def test_search_without_htmx_renders_full_page_and_opens_panel(self):
        response = self.client.get(reverse("search"), {"q": "roads"})
        self.assertContains(response, "<!doctype html>")
        self.assertContains(response, "Roads, infrastructure and public works")
        self.assertContains(response, 'x-init="searchOpen = true"')

    def test_query_is_escaped_and_bounded(self):
        response = self.client.get(reverse("search"), {"q": '\"><script>alert(1)</script>'})
        self.assertNotContains(response, '<script>alert(1)</script>')
        self.assertContains(response, "&lt;script&gt;")
        response = self.client.get(reverse("search"), {"q": "a" * 500})
        self.assertEqual(len(response.context["query"]), 200)

    def test_update_filters_render_only_matching_cards(self):
        for category, count in (("all", 3), ("notice", 2), ("publication", 1)):
            with self.subTest(category=category):
                response = self.client.get(reverse("updates"), {"category": category}, HTTP_HX_REQUEST="true")
                self.assertContains(response, 'class="update-card"', count=count)
                self.assertNotContains(response, "<!doctype html>")
                self.assertContains(response, 'aria-current="true"', count=1)
                self.assertIn("HX-Request", response.headers["Vary"])

    def test_invalid_filter_falls_back_to_all(self):
        response = self.client.get(reverse("updates"), {"category": "invalid"}, HTTP_HX_REQUEST="true")
        self.assertEqual(response.context["category"], "all")
        self.assertContains(response, 'class="update-card"', count=3)

    def test_filter_without_htmx_returns_full_page(self):
        response = self.client.get(reverse("home"), {"category": "publication"})
        self.assertContains(response, "<!doctype html>")
        self.assertContains(response, 'class="update-card"', count=1)
        response = self.client.get(reverse("updates"), {"category": "notice"})
        self.assertContains(response, "<!doctype html>")
        self.assertContains(response, 'class="update-card"', count=2)

    def test_endpoints_are_read_only(self):
        for route in ("home", "search", "updates"):
            with self.subTest(route=route):
                self.assertEqual(self.client.post(reverse(route)).status_code, 405)
