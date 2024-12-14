import reflex as rx

class DashboardState(rx.State):
    action_result: str = ""

    def ping_action(self):
        self.action_result = "Ping results displayed here."

    def traceroute_action(self):
        self.action_result = "Traceroute results displayed here."

    def reboot_action(self):
        self.action_result = "Reboot initiated."

def network_dashboard():
    return rx.center(
        rx.vstack(
            rx.heading("Network Monitoring Dashboard", size="2"),
            rx.box(
                rx.vstack(
                    rx.text("192.168.1.1", font_size="lg", font_weight="bold"),
                    rx.text("Status: ", rx.text("Online", color="green", as_="span")),
                    rx.text("Uptime: 7 days, 3 hours"),
                    rx.text("Load: 0.75"),
                    rx.text("Last Updated: 2023-05-01 14:30:00"),
                    rx.text("Firewall Enabled: Yes"),
                    rx.hstack(
                        rx.button("Ping", on_click=DashboardState.ping_action, color_scheme="blue"),
                        rx.button("Trace Route", on_click=DashboardState.traceroute_action, color_scheme="green"),
                        rx.button("Reboot", on_click=DashboardState.reboot_action, color_scheme="yellow"),
                    ),
                    align="start",
                    spacing="4",
                    padding="4",
                    border_radius="10px",
                    border="1px solid lightgrey",
                ),
                shadow="lg",
                padding="10px",
                background_color="white",
                width="400px",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Action Results", font_size="lg", font_weight="bold"),
                    rx.text(DashboardState.action_result),
                    align="start",
                    spacing="3",
                ),
                shadow="lg",
                padding="10px",
                background_color="white",
                width="400px",
            ),
            rx.hstack(
                rx.text("10.0.0.1", padding="3", background_color="lightgrey", width="200px"),
                rx.text("172.16.0.1", padding="3", background_color="lightgrey", width="200px"),
                spacing="5"
            ),
            align="start",
            spacing="6",
        ),
        padding="8",
        background_color="#f7f7f7",
    )

def index() -> rx.Component:
    return rx.container(network_dashboard())

app = rx.App(state=DashboardState)
app.add_page(index)
# app.run()
