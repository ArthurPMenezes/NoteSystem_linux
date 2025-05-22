def gerar_nota_peso():
    print("🧾 GERADOR DE NOTA (SOMA DE PESO)")
    data = input("Data (ex: 22/05/2025): ").strip()

    while True:
        peso_boi = input("Peso total do boi (kg, use ponto): ").strip()
        try:
            peso_boi_float = float(peso_boi)
            break
        except ValueError:
            print("⚠️ Valor inválido. Tente de novo.")

    cortes = []
    while True:
        corte = input("Corte (ENTER para finalizar): ").strip()
        if not corte:
            break
        peso = input(f"Peso de {corte} (kg, use ponto): ").strip()
        try:
            peso_float = float(peso)
            cortes.append((corte.upper(), peso_float))
        except ValueError:
            print("⚠️ Peso inválido. Tente de novo.")

    total_peso = sum(p for _, p in cortes)

    # Montar a nota
    linhas = [
        f"DATA: {data}",
        f"PESO TOTAL DO BOI: {peso_boi_float:.3f} kg\n",
        "    AV RACOES E FRIGORIFICO\n",
    ]

    for corte, peso in cortes:
        linhas.append(f"{corte.ljust(20, '.')} {peso:>6.3f} kg")
    linhas.append("")
    linhas.append(f"TOTAL".ljust(20, '.') + f" {total_peso:>6.3f} kg")
    linhas.append("\n\n")
    linhas.append("................................")

    nota_texto = "\n".join(linhas)

    print("\nPrévia da nota:")
    print("-" * 32)
    print(nota_texto)
    print("-" * 32)

    confirma = input("Imprimir? (s/n): ").strip().lower()
    if confirma == 's':
        with open("/dev/usb/lp0", "w") as imp:
            imp.write("\x1B\x40")  # reset
            imp.write(nota_texto)
            imp.write("\x1B\x64\x02")  # avanço de papel
        print("✅ Nota enviada para a impressora.")
    else:
        print("❌ Cancelado.")

if __name__ == "__main__":
    gerar_nota_peso()