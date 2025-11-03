import reflex as rx
from typing import Any


class ReactPDF(rx.NoSSRComponent):
    library = "react-pdf@9.1.1"


def _load_success_signature(
        pdf_document_proxy: rx.vars.ObjectVar,
) -> tuple[rx.Var[dict]]:
    return (pdf_document_proxy["_pdfInfo"].to(dict),)


class Document(ReactPDF):
    tag = "Document"

    file: rx.Var[str]
    loading: rx.Var[Any] = "Loading PDF..."
    error: rx.Var[Any] = "Failed to load PDF"

    on_load_success: rx.EventHandler[_load_success_signature]
    on_load_error: rx.EventHandler[lambda error: [error]]

    def add_custom_code(self) -> list[str]:
        return [
            """
import { pdfjs } from 'react-pdf';

pdfjs.GlobalWorkerOptions.workerSrc = `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;
"""
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

    page_number: rx.Var[int]
    width: rx.Var[int]
    height: rx.Var[int]
    scale: rx.Var[float] = 1.0

    render_text_layer: rx.Var[bool] = True
    render_annotation_layer: rx.Var[bool] = True