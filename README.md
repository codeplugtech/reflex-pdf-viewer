# Reflex PDF Viewer
A powerful and easy-to-use PDF viewer component for [Reflex](https://reflex.dev) applications. Built on top of react-pdf, it provides seamless PDF viewing capabilities with full control over navigation, zoom, and display options.


## 📦 Installation

```bash
pip install reflex-pdf-viewer
```

## 🚀 Quick Start

```python
import reflex as rx
from reflex_pdf_viewer import Document, Page

class State(rx.State):
    current_page: int = 1
    n_pages: int = 1

    @rx.event
    def load_success(self, info: dict):
        self.n_pages = info.get("numPages", 1)

def index():
    return rx.vstack(
        rx.heading("Reflex pdf preview", size="8"),
        Document.create(
            Page.create(page_number=State.current_page),
            file="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
            on_load_success=State.load_success,
        ),
    )

app = rx.App()
app.add_page(index)
```

Don't forget to add the frontend package to your `rxconfig.py`:

```python
import reflex as rx

config = rx.Config(
    app_name="your_app",
    frontend_packages=[
        "react-pdf@10.1.0",  # Required for PDF viewing
    ],
)
```

## 📝 Changelog

### v0.0.1 (2025-12-09)
- Initial release
- Basic PDF viewing functionality
- Page navigation support
- Zoom controls
- Error handling
- Loading states

### v0.0.2 (2025-11-01)
- Added loading prop to avoid failed to load pdf issue

## 🐛 Issues & Support

If you encounter any issues or have questions:

1. Check the [GitHub Issues](https://github.com/yourusername/reflex-pdf-viewer/issueshttps://github.com/reflex-dev/reflex/issues)
2. Join the [Reflex Discord](https://discord.gg/T5WSbC2YtQhttps://discord.com/invite/T5WSbC2YtQ) community
3. Create a new issue with detailed information


## 🙏 Acknowledgments

- Built with [Reflex](https://reflexhttps://github.com/reflex-dev/reflex) - The web framework for Python
- Powered by [react-pdf](https://github.com/wojtekmaj/react-pdfhttps://www.npmjs.com/package/react-pdf) - React PDF viewer component
- Uses [PDF.js](https://github.com/mozilla/pdf.jshttps://mozilla.github.io/pdf.js/) - JavaScript PDF rendering engine

---

**Made with ❤️ for the Reflex community**

*Star ⭐ this repo if you find it useful!*