import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        # self.txt_name = None
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        # self.btn_hello = None
        self.btn_top_vendite = None
        self.btn_analizza_vendite = None
        self.txt_result = None
        # self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls

        """
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )
        """
        self.ddAnno = ft.Dropdown(label="anno", width=200, options=[ft.dropdown.Option(key="null", text="Nessun filtro")],
                                  on_change=self._controller.leggi_anno)
        self._controller.popola_ddAnno()
        self.ddBrand = ft.Dropdown(label="brand", width=200, options=[ft.dropdown.Option(key="null", text="Nessun filtro")],
                                   on_change=self._controller.leggi_brand)
        self._controller.popola_ddBrand()
        self.ddRetailer = ft.Dropdown(label="retailer", width=500, options=[ft.dropdown.Option(key=None,
                                                                                               text="Nessun filtro",
                                                                                               data=None,
                                                                                               on_click=self._controller.leggi_retailer)])
        self._controller.popola_ddRetailer()

        # button for the "hello" reply
        # self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.btn_top_vendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.get_top_vendite)
        self.btn_analizza_vendite = ft.ElevatedButton(text="Analizza vendite",
                                                      on_click=self._controller.get_analizza_vendite)

        row2 = ft.Row([self.btn_top_vendite, self.btn_analizza_vendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
