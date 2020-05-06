def div42by(dividBy):
    try:
        return 42/dividBy
    except:
        print("Error: Division by Zero!")
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
