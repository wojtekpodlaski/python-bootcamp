class




def test_product():
    product = Product(1, 'Woda', 10.99)
    assert product.ID ==1
    assert product.nazwa == "Woda"
    assert product.cena ==10.99

