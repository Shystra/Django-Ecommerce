def formata_preco (val):
    return f'R$ {val:.2f}'.replace ('.' , ',')


#TODO Soma a quantidade para cada item no carrinho.
def cart_total_qtd (carrinho):
    return sum([item ['quantidade'] for item in carrinho.values ()])


def cart_totals (carrinho):
    return sum (
        [
            #TODO Obtenha o preco_quantitativo_promocional se o preco_quantitativo_promocional estiver preenchido
            #TODO Ao contrario disso obtenha o preco_quantitativo para cada item no carrinho
            item.get ('preco_quantitativo_promocional')
            if item.get ('preco_quantitativo_promocional')
            else item.get ('preco_quantitativo')
            for item in carrinho.values ()
        ]
    )