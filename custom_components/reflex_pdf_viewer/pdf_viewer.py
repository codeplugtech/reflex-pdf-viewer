import reflex as rx


class ReactPDF(rx.NoSSRComponent):
    library = "react-pdf@10.1.0"


def _load_success_signature(
    pdf_document_proxy: rx.vars.ObjectVar,
) -> tuple[rx.Var[dict]]:
    return (pdf_document_proxy["_pdfInfo"].to(dict),)


class Document(ReactPDF):
    tag = "Document"

    file: str
    on_load_success: rx.EventHandler[_load_success_signature]

    def add_custom_code(self) -> list[str]:
        return [
            """
        import { pdfjs } from 'react-pdf';

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  'pdfjs-dist/build/pdf.worker.min.mjs',
  import.meta.url,
).toString();"""
        ]

    def add_imports(self) -> rx.ImportDict:
        return {
            "": [
                "react-pdf/dist/Page/AnnotationLayer.css",
                "react-pdf/dist/Page/TextLayer.css",
            ],
        }


class Page(ReactPDF):
    tag = "Page"

    page_number: int