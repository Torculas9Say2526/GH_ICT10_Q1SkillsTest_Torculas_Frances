from pyscript import document, display 


def create_order(e):
    matcha_ichigo = document.getElementById("item1")
    dark_matcha = document.getElementById("item2")
    cold_strawberry_yuzu = document.getElementById("item3")
    mint_choco_mochi = document.getElementById("item4")
    white_caramel_frappucino = document.getElementById("item5")

    subtotal = float(matcha_ichigo.value) * float(matcha_ichigo.checked) + float(dark_matcha.value) * float(dark_matcha.checked) + float(cold_strawberry_yuzu.value) * float(cold_strawberry_yuzu.checked) + float(mint_choco_mochi.value) * float(mint_choco_mochi.checked) + float(white_caramel_frappucino.value) * float(white_caramel_frappucino.checked)
    VAT = subtotal * 0.12
    total = subtotal + VAT

    display(f"Your subtotal is: ₱{subtotal: .2f}", target="show")
    display(f"Your VAT is: ₱{VAT: .2f}", target="show")
    display(f"Your total is: ₱{total: .2f}", target="show")