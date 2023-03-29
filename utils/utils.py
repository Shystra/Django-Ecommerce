def formata_preco (val):
    return f'R$ {val:.2f}'.replace ('.' , ',')


#TODO Soma a quantidade para cada item no carrinho.
def cart_total_qtd (carrinho):
    return sum([item ['quantidade'] for item in carrinho.values ()])
