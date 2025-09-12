import reflex as rx
from reflex_pdf_viewer import Document, Page


class State(rx.State):
    n_pages: int = 1
    current_page: int = 1

    @rx.event
    def load_success(self, info: dict):
        print(info)
        self.n_pages = info.get("numPages", 1)
        self.current_page = 1

    @rx.event
    def prev_page(self):
        self.current_page = max(1, self.current_page - 1)

    @rx.event
    def next_page(self):
        self.current_page = min(self.n_pages, self.current_page + 1)


def page_control():
    return rx.hstack(
        rx.button(
            "<", on_click=State.prev_page, is_disabled=State.current_page <= 1
        ),
        rx.text(f"{State.current_page} / {State.n_pages}"),
        rx.button(
            ">",
            on_click=State.next_page,
            is_disabled=State.current_page >= State.n_pages,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Pdf preview", size="9"),
            rx.vstack(
                page_control(),
                Document.create(
                    Page.create(
                        page_number=State.current_page,
                    ),
                    file="/pkpadmin,+1008-4741-1-CE (1).pdf",
                    on_load_success=State.load_success,
                ),
                page_control(),
                align="center",
            ),
        ),
    )


app = rx.App()
app.add_page(index)