import flet as ft

def main(page: ft.Page):
    page.title = "Network Monitoring Dashboard"
    page.padding = 20

    # Card for 192.168.1.1
    def create_device_card(ip_address, status, uptime, load, last_updated, firewall_enabled):
        return ft.ExpansionPanel(
            header=ft.Text(ip_address, style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row([
                            ft.Text(ip_address, weight="bold", size=18),
                        ]),
                        ft.Text(f"Status: {status}", color="green" if status == "Online" else "red"),
                        ft.Text(f"Uptime: {uptime}"),
                        ft.Text(f"Load: {load}"),
                        ft.Text(f"Last Updated: {last_updated}"),
                        ft.Text(f"Firewall Enabled: {firewall_enabled}"),
                        ft.Row(
                            [
                                ft.ElevatedButton("Ping", icon=ft.icons.POWER),
                                ft.ElevatedButton("Trace Route", icon=ft.icons.NEAR_ME),
                                ft.ElevatedButton("Reboot", icon=ft.icons.RESTART_ALT),
                            ]
                        ),
                    ],
                    spacing=10,
                ),
                padding=20,
            ),
            # margin=10,
        )

    # Action Results Pane
    action_results = ft.Container(
        content=ft.Column([
            ft.Text("Action Results", weight="bold", size=16),
            ft.Container(
                ft.Column([
                    ft.Text("Ping Result (192.168.1.1)"),
                    ft.Text("4 packets transmitted, 4 received, 0% packet loss"),
                    ft.Text("Round-trip min/avg/max = 1.2/2.3/3.4 ms"),
                ]),
                padding=10,
                # bgcolor=ft.colors.BLUE_GREY_50,
                border_radius=5,
            ),
            ft.Container(
                ft.Column([
                    ft.Text("Trace Route (192.168.1.1)"),
                    ft.Text("1. 192.168.1.1 (1.2 ms)"),
                    ft.Text("2. 10.0.0.1 (5.6 ms)"),
                    ft.Text("3. 172.16.0.1 (10.3 ms)"),
                ]),
                padding=10,
                # bgcolor=ft.colors.BLUE_GREY_50,
                border_radius=5,
            ),
        ],
            spacing=10,
        ),
        padding=20,
        margin=20,
        # bgcolor=ft.colors.WHITE,
        border_radius=5,
    )

    # Devices List
    devices_list = ft.ExpansionPanelList([
        create_device_card("192.168.1.1", "Online", "7 days, 3 hours", "0.75", "2023-05-01 14:30:00", "Yes"),
        create_device_card("10.0.0.1", "Online", "3 days, 5 hours", "0.65", "2023-05-01 14:30:00", "Yes"),
        create_device_card("172.16.0.1", "Offline", "0 days, 0 hours", "N/A", "2023-05-01 14:30:00", "No"),
    ])

    # Layout
    page.add(
        ft.Row([
            ft.Column([
                devices_list
            ], expand=True),
            action_results
        ])
    )

ft.app(target=main)
