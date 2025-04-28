try:
    raise Exception(100)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e)

    print('Valor sugerido', e.args[0])