saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite
saldo >= saque or saque <= limite
not saque > limite
conta_especial = True
saldo >= saque or (not conta_especial and saque <= limite)