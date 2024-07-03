import operator

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno_selezionato = None
        self.brand_selezionato = None
        self.retailer_selezionato = None

    def leggi_anno(self, e):
        # self.anno_selezionato = self._view.ddAnno.value
        if self._view.ddAnno.value == "null":
            self.anno_selezionato = None
        else:
            self.anno_selezionato = self._view.ddAnno.value

    def leggi_brand(self, e):
        # self.brand_selezionato = self._view.ddBrand.value
        if self._view.ddBrand.value == "null":
            self.brand_selezionato = None
        else:
            self.brand_selezionato = self._view.ddBrand.value

    def leggi_retailer(self, e):
        # self.retailer_selezionato = self._view.ddRetailer.value
        # print(self.retailer_selezionato)
        #print("e.control.data")
        #print(e.control.data)
        if e.control.data is None: # se è None, cioè nessun filtro
            self.retailer_selezionato = None
        else:
            self.retailer_selezionato = e.control.data.retailer_code # è un oggetto retailer
        #print("retailer selezionato")
        #print(self.retailer_selezionato)

    def popola_ddAnno(self):
        anni = self._model.get_anni()
        for anno in anni:
            self._view.ddAnno.options.append(ft.dropdown.Option(anno))

    def popola_ddBrand(self):
        brands = self._model.get_brands()
        for brand in brands:
            self._view.ddBrand.options.append(ft.dropdown.Option(brand[0]))

    def popola_ddRetailer(self):
        retailers = self._model.get_retailers()
        #print(retailers)
        for retailer in retailers:
            #print(retailer)
            self._view.ddRetailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                    text=retailer.retailer_name,
                                                                    data=retailer, on_click=self.leggi_retailer))

    def get_top_vendite(self, e):
        #print(self.anno_selezionato)
        #print(self.brand_selezionato)
        #print(self.retailer_selezionato)
        vendite = self._model.get_top_vendite(self.anno_selezionato, self.brand_selezionato, self.retailer_selezionato)
        #print("ciao")
        #print(vendite)
        vendite.sort(key=operator.attrgetter("ricavo"), reverse=True)
        #print(vendite)
        #print(len(vendite))

        self._view.txt_result.controls.clear()

        if 0 < len(vendite) <= 5:
            for vendita in vendite:
                self._view.txt_result.controls.append(ft.Text(vendita.__str__()))
        elif len(vendite) > 5:
            for i in range(5):
                self._view.txt_result.controls.append(ft.Text(vendite[i].__str__()))
        else: # se è uguale a 0
            self._view.txt_result.controls.append(ft.Text("Non sono state trovate vendite."))

        self._view.update_page()

    def get_analizza_vendite(self, e):
        vendite = self._model.get_top_vendite(self.anno_selezionato, self.brand_selezionato, self.retailer_selezionato)
        statistiche = self._model.get_statistiche(self.anno_selezionato, self.brand_selezionato, self.retailer_selezionato)

        self._view.txt_result.controls.clear()

        totale_ricavi = 0
        for vendita in vendite:
            totale_ricavi += vendita.ricavo

        # il numero di vendite è la lunghezza della lista di vendite

        self._view.txt_result.controls.extend([ft.Text("Statistiche vendite:"),
                                               ft.Text(f"Giro d'affari: {totale_ricavi}"),
                                               ft.Text(f"Numero vendite: {len(vendite)}"),
                                               ft.Text(f"Numero retailers coinvolti: {statistiche[0]}"),
                                               ft.Text(f"Numero prodotti coinvolti: {statistiche[1]}")])

        self._view.update_page()

"""
    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
"""

