import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import generate_site  # noqa: E402


class PortfolioGeneratorTests(unittest.TestCase):
    def test_loads_and_renders_portfolio_metadata(self):
        projects = generate_site.load_projects(Path(__file__).parents[1].joinpath("README.md").read_text())
        page = generate_site.render(projects)
        self.assertIn("USB FPGA development board", page)
        self.assertIn("https://github.com/4137314/usb-lab", page)
        self.assertIn('id="personal"', page)

    def test_rejects_non_https_links(self):
        readme = '''<!-- portfolio-projects:begin -->
```json
[{"title":"Example","category":"Personal","description":"Description","tags":["tag"],"source":"javascript:alert(1)"}]
```
<!-- portfolio-projects:end -->'''
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            generate_site.load_projects(readme)

    def test_rejects_unknown_category(self):
        readme = '''<!-- portfolio-projects:begin -->
```json
[{"title":"Example","category":"Other","description":"Description","tags":["tag"],"source":"https://example.com"}]
```
<!-- portfolio-projects:end -->'''
        with self.assertRaisesRegex(ValueError, "unsupported category"):
            generate_site.load_projects(readme)

    def test_updates_only_marked_site_region_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(__file__).parents[1] / "README.md"
            site = Path(directory) / "index.html"
            site.write_text(f"before\n{generate_site.BEGIN}\nold\n{generate_site.END}\nafter\n")
            generate_site.update_site(readme, site)
            first = site.read_text()
            generate_site.update_site(readme, site)
            self.assertEqual(first, site.read_text())
            self.assertTrue(first.startswith("before\n"))
            self.assertTrue(first.endswith("after\n"))
            self.assertNotIn("old", first)


if __name__ == "__main__":
    unittest.main()
