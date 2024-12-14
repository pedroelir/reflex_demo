"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def create_heading(tag, font_size, line_height, text):
    """Create a heading with custom styling."""
    return rx.heading(
        text,
        font_weight="700",
        margin_bottom="1rem",
        font_size=font_size,
        line_height=line_height,
        as_=tag,
    )


def create_bold_span(text):
    """Create a span element with bold text."""
    return rx.text.span(text, font_weight="500")


def create_chevron_down_icon():
    """Create a chevron-down icon with specific dimensions."""
    return rx.icon(
        tag="chevron-down",
        height="1.25rem",
        width="1.25rem",
    )


def create_expandable_button(button_text):
    """Create an expandable button with custom styling and a chevron-down icon."""
    return rx.el.button(
        create_bold_span(text=button_text),
        create_chevron_down_icon(),
        display="flex",
        _focus={"outline-style": "none"},
        _hover={"background-color": "#0A0A0B"},
        align_items="center",
        justify_content="space-between",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        text_align="left",
        width="100%",
    )


def create_strong_text(text):
    """Create a strong (bold) text element."""
    return rx.text.strong(text)


def create_colored_span(color, text):
    """Create a span element with colored text."""
    return rx.text.span(text, color=color)


def create_status_text(status_color, status_text):
    """Create a status text with a label and colored status."""
    return rx.text(
        create_strong_text(text="Status:"),
        create_colored_span(
            color=status_color, text=status_text
        ),
    )


def create_labeled_text(label, value):
    """Create a text element with a bold label and a value."""
    return rx.text(create_strong_text(text=label), value)


def create_colored_button(
    hover_style, background_color, button_text
):
    """Create a colored button with hover effect and custom text."""
    return rx.el.button(
        button_text,
        background_color=background_color,
        _hover=hover_style,
        margin_right="0.5rem",
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        border_radius="0.25rem",
        color="#ffffff",
    )


def create_block_button():
    """Create a red 'Block' button with hover effect."""
    return rx.el.button(
        "Block",
        background_color="#EF4444",
        _hover={"background-color": "#DC2626"},
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.25rem",
        padding_bottom="0.25rem",
        border_radius="0.25rem",
        color="#ffffff",
    )


def create_action_buttons():
    """Create a set of action buttons including Ping, Trace, and Block."""
    return rx.box(
        create_colored_button(
            hover_style={"background-color": "#2563EB"},
            background_color="#3B82F6",
            button_text="Ping",
        ),
        create_colored_button(
            hover_style={"background-color": "#059669"},
            background_color="#10B981",
            button_text="Trace",
        ),
        create_block_button(),
        margin_top="0.5rem",
    )


def create_ip_details_box(
    status_color, status_text, last_seen, hostname
):
    """Create a box containing IP details including status, last seen, and hostname."""
    return rx.box(
        create_status_text(
            status_color=status_color,
            status_text=status_text,
        ),
        create_labeled_text(
            label="Last Seen:", value=last_seen
        ),
        create_labeled_text(
            label="Hostname:", value=hostname
        ),
        create_action_buttons(),
        # background_color="#F9FAFB",
        # display="none",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    )


def create_ip_details():
    return rx.box(
        create_status_text(
            status_color="#059669", status_text="Active"
        ),
        create_labeled_text(
            label="Last Seen:",
            value=" 2023-04-15 14:30:22",
        ),
        create_labeled_text(
            label="Hostname:", value=" router.local"
        ),
        create_action_buttons(),
        # background_color="#F9FAFB",
        padding_left="1rem",
        padding_right="1rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
    ),


def create_ip_entry():
    """Create an IP address entry with expandable details for 192.168.1.1."""
    return rx.box(
        create_expandable_button(button_text="192.168.1.1"),
        create_ip_details(),
        # rx.box(
        #     create_status_text(
        #         status_color="#059669", status_text="Active"
        #     ),
        #     create_labeled_text(
        #         label="Last Seen:",
        #         value=" 2023-04-15 14:30:22",
        #     ),
        #     create_labeled_text(
        #         label="Hostname:", value=" router.local"
        #     ),
        #     create_action_buttons(),
        #     # background_color="#F9FAFB",
        #     padding_left="1rem",
        #     padding_right="1rem",
        #     padding_top="0.5rem",
        #     padding_bottom="0.5rem",
        # ),
        border_bottom_width="1px",
    )


def create_ip_list():
    """Create a list of IP addresses with expandable details."""
    return rx.box(
        create_ip_entry(),
        rx.box(
            create_expandable_button(
                button_text="10.0.0.1"
            ),
            create_ip_details_box(
                status_color="#D97706",
                status_text="Inactive",
                last_seen=" 2023-04-14 09:15:47",
                hostname=" server1.local",
            ),
            border_bottom_width="1px",
        ),
        rx.box(
            create_expandable_button(
                button_text="172.16.0.1"
            ),
            create_ip_details_box(
                status_color="#059669",
                status_text="Active",
                last_seen=" 2023-04-15 15:45:10",
                hostname=" workstation5.local",
            ),
            border_bottom_width="1px",
        ),
        # background_color="#ffffff",
        overflow="hidden",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )

def create_accordion_ip_list():
    return rx.accordion.root(
        rx.accordion.item(
            header="Is it accessible?",
            content=create_ip_details(),
            value="item_1",
        ),
        rx.accordion.item(
            header="Is it unstyled?",
            content=create_ip_details_box(
                status_color="#D97706",
                status_text="Inactive",
                last_seen=" 2023-04-14 09:15:47",
                hostname=" server1.local",
            ),
            value="item_2",
        ),
        rx.accordion.item(
            header="Is it finished?",
            content="It's still in beta, but it's ready to use in production.",
            value="item_3",
        ),
        collapsible=True,
        )


def create_action_results_section():
    """Create a section to display action results."""
    return rx.box(
        create_heading(
            tag="h2",
            font_size="1.25rem",
            line_height="1.75rem",
            text="Action Results",
        ),
        rx.box(
            rx.text(
                "Select an action to see results here.",
                color="#4B5563",
            ),
            background_color="#ffffff",
            padding="1rem",
            border_radius="0.5rem",
            box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        ),
        width="33.333333%",
    )


def create_main_content():
    """Create the main content layout including IP list and action results."""
    return rx.flex(
        rx.box(
            create_heading(
                tag="h1",
                font_size="1.5rem",
                line_height="2rem",
                text="IP Address Management",
            ),
            create_accordion_ip_list(),
            create_ip_list(),
            padding_right="1rem",
            width="66.666667%",
        ),
        create_action_results_section(),
        width="100%",
        style=rx.breakpoints(
            {
                "640px": {"max-width": "640px"},
                "768px": {"max-width": "768px"},
                "1024px": {"max-width": "1024px"},
                "1280px": {"max-width": "1280px"},
                "1536px": {"max-width": "1536px"},
            }
        ),
        display="flex",
        margin_left="auto",
        margin_right="auto",
        padding="1rem",
    )


def index():
    """Create the main IP address management page with styling and content."""
    return rx.fragment(
        rx.script(src="https://cdn.tailwindcss.com"),
        rx.el.style(
            """
        @font-face {
            font-family: 'LucideIcons';
            src: url(https://unpkg.com/lucide-static@latest/font/Lucide.ttf) format('truetype');
        }
    """
        ),
        rx.box(
            create_main_content(),
            # background_color="#F3F4F6",
            font_family='system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
        ),
    )


app = rx.App()
app.add_page(index)
