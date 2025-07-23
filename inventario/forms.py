from django import forms
from .models import Producto, MovimientoStock
from .services import crear_producto, registrar_movimiento


class ProductoForm(forms.ModelForm):
    stock_inicial = forms.IntegerField(min_value=0, required=False, initial=0)

    class Meta:
        model = Producto
        fields = ("sku", "nombre", "categoria", "stock_minimo", "activo")

    def save(self, commit=True, usuario=None):
        data = self.cleaned_data
        return crear_producto(
            sku=data["sku"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            stock_inicial=data.get("stock_inicial", 0),
            stock_minimo=data["stock_minimo"],
            usuario=usuario,
        )


class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ("producto", "tipo", "cantidad", "referencia")

    def save(self, commit=True, usuario=None):
        data = self.cleaned_data
        return registrar_movimiento(
            producto=data["producto"],
            tipo=data["tipo"],
            cantidad=data["cantidad"],
            referencia=data.get("referencia", ""),
            usuario=usuario,
        )
