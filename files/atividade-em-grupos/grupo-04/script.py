def validar_ip(ip):
    partes = ip.split('.')
    
    if len(partes) != 4:
        return False

    try:
        num1 = int(partes[0])
        nums = [int(parte) for parte in partes[1:]]
        
        if num1 < 1 or num1 > 255:
            return False
        for num in nums:
            if num < 0 or num > 255:
                return False
        return True
    except ValueError:
        return False
    

def processar_arquivos(arquivo_entrada, arquivo_ips_validos, arquivo_ips_invalidos):

    try:
        entrada = open(arquivo_entrada, 'r')
        validos = open(arquivo_ips_validos, 'w')
        invalidos = open(arquivo_ips_invalidos, 'w')

        for linha in entrada:
            ip = linha.strip()
            if validar_ip(ip):
                validos.write(ip + '\n')
            else:
                invalidos.write(ip + '\n')
    except OSError:
        print("ALgum arquivo não foi encontrado")
    finally:
        entrada.close()
        validos.close()
        invalidos.close()

arquivo_entrada = r'files/atividade-em-grupos/grupo-04/ips.txt'
arquivo_ips_validos = r'files/atividade-em-grupos/grupo-04/validos.txt'
arquivo_ips_invalidos = r'files/atividade-em-grupos/grupo-04/invalidos.txt'

processar_arquivos(arquivo_entrada, arquivo_ips_validos, arquivo_ips_invalidos)
