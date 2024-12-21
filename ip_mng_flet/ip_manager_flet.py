import flet as ft
import random

def main(page: ft.Page):
    page.title = "Network Monitoring Dashboard"
    page.padding = 20

    def mock_ping():
        return random.choice([True, False])

    action_results_content = ft.Column([], spacing=10)

    def log_action_result(ip_address, action, result):
        action_results_content.controls.append(
            ft.Container(
                ft.Column([
                    ft.Text(f"{action} Result ({ip_address})"),
                    ft.Text(result),
                ]),
                padding=10,
                border_radius=5,
            )
        )
        action_results_content.update()

    def create_device_card(ip_address, status, uptime, load, last_updated, firewall_enabled):
        status_text = ft.Text(f"Status: {status}", color="green" if status == "Online" else "red")

        def on_ping_click(e):
            if mock_ping():
                status_text.value = "Status: Online"
                status_text.color = "green"
                result = "Ping successful"
            else:
                status_text.value = "Status: Offline"
                status_text.color = "red"
                result = "Ping failed"
            status_text.update()
            log_action_result(ip_address, "Ping", result)

        return ft.ExpansionTile(
            title=ft.Text(ip_address, style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            controls=[
                ft.Row([status_text]),
                ft.Row([ft.Text(f"Uptime: {uptime}")]),
                ft.Row([ft.Text(f"Load: {load}")]),
                ft.Row([ft.Text(f"Last Updated: {last_updated}")]),
                ft.Row([ft.Text(f"Firewall Enabled: {firewall_enabled}")]),
                ft.Row([
                    ft.ElevatedButton("Ping", icon=ft.icons.POWER, on_click=on_ping_click),
                    ft.ElevatedButton("Trace Route", icon=ft.icons.NEAR_ME),
                    ft.ElevatedButton("Reboot", icon=ft.icons.RESTART_ALT),
                ]),
            ],
        )

    action_results = ft.Container(
        content=ft.Column([
            ft.Text("Action Results", weight="bold", size=16),
            action_results_content,
        ], spacing=10),
        padding=20,
        margin=20,
        border_radius=5,
    )

    page.add(
        ft.Row([
            ft.Column([
                create_device_card("192.168.1.1", "Online", "7 days, 3 hours", "0.75", "2023-05-01 14:30:00", "Yes"),
                create_device_card("10.0.0.1", "Online", "3 days, 5 hours", "0.65", "2023-05-01 14:30:00", "Yes"),
                create_device_card("172.16.0.1", "Offline", "0 days, 0 hours", "N/A", "2023-05-01 14:30:00", "No"),
            ], expand=True),
            action_results
        ])
    )

ft.app(target=main)