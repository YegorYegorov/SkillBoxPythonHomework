lampa1 = store.get('12345')
lampa2 = lampa1[0]
lampa_q = lampa2.get('quantity')
lampa_p = lampa2.get('price')
lampa_sum = lampa_p * lampa_q
print('Лампа -', lampa_q, 'шт, стоимость', lampa_sum, 'руб')
