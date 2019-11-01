# Questão 03
O IPERF é uma ferramenta que é muito utilizada para realizar a avaliação de desempenho de redes. Ela permite que você crie conexões TCP, modificando os parâmetros desejados das configurações que serão usadas pelo protocolo, bem como também possibilita o envido de dados através de UDP. Execute a ferramenta com as opções indicadas abaixo, coletando os resultados de cada um deles e discutindo as diferenças observadas no desempenho dos testes de acordo com essas modificações.

Servidor: `iperf -s`
Cliente: `iperf -c 127.0.0.1`

### Usando flag -w

Valor da flag | Interval | Transfer | Bandwith        | Window size
--------------|----------|----------|-----------------|-------------
none          | 0-10 sec | 50.1 GB  | 41.6 Gbits/sec  | 2.5 MB
1             | 0-10 sec | 15.8 MB  | 13.1 Mbits/sec  | 4.5 KB
2000          | 0-10 sec | 16.1 MB  | 13.5 Mbits/sec  | 4.5 KB
10000         | 0-10 sec | 18.5 MB  | 15.4 Mbits/sec  | 19.5 KB
50000         | 0-10 sec | 13.7 GB  | 11.7 Gbits/sec  | 97.7 KB
100000        | 0-10 sec | 39.6 GB  | 34.0 Gbits/sec  | 195 KB

Podemos ver que quando chamamos, no cliente, `iperf -c 127.0.0.1` a janela do TCP é a default (2.5MB), dessa forma há uma transferência de 50.1 GB pois a janela é grande. 

Quando usamos a flag -w 1 (janela com 1 byte), o iperf determina que a janela será 4.5KB, um valor arredondado para cima, e o valor transferido diminui pois a janela diminuiu de 2.5MB para 4.5KB. O mesmo acontece para a flag -w 2000 pois o iperf também arredondou para 4.5KB

O mesmo ocorre para os outros valores de flag. Um valor é requisitado, mas o iperf utiliza um diferente (geralmente arredondado bastante para cima). Quanto maior a janela usada, maior a largura de banda e consequentemente o valor final transferido (Transfer). 

### Usando flag -M

Valor da flag | Interval | Transfer | Bandwith        | MSS
--------------|----------|----------|-----------------|------
none          | 0-10 sec | 50.1 GB  | 41.6 Gbits/sec  | default
100           | 0-10 sec | 38.1 GB  | 32.8 Gbits/sec  | 536
250           | 0-10 sec | 37.6 GB  | 32.3 Gbits/sec  | 536
500           | 0-10 sec | 37.4 GB  | 32.1 Gbits/sec  | 536
1000          | 0-10 sec | 37.2 GB  | 30.0 Gbits/sec  | 536
1500          | 0-10 sec | 38.7 GB  | 33.2 Gbits/sec  | 536

Aqui apesar das tentativas de determinar o MSS, o iperf o colocou em 536 o que parece ser um tipo de valor padrão. Devido ao MSS não ter sido alterado, não houve diferença muito significante na largura de banda.

### Usando a flag P
```bash
$ iperf -c 127.0.0.1 -P 1

TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 34904 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  32.0 GBytes  27.5 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -P 2
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[  5] local 127.0.0.1 port 34916 connected with 127.0.0.1 port 5001
[  3] local 127.0.0.1 port 34914 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  5]  0.0-10.0 sec  19.3 GBytes  16.6 Gbits/sec
[  3]  0.0-10.0 sec  19.9 GBytes  17.1 Gbits/sec
[SUM]  0.0-10.0 sec  39.2 GBytes  33.6 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -P 4

------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[ 13] local 127.0.0.1 port 34930 connected with 127.0.0.1 port 5001
[  3] local 127.0.0.1 port 34924 connected with 127.0.0.1 port 5001
[  5] local 127.0.0.1 port 34926 connected with 127.0.0.1 port 5001
[ 14] local 127.0.0.1 port 34928 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[ 13]  0.0-10.0 sec  10.7 GBytes  9.18 Gbits/sec
[  3]  0.0-10.0 sec  11.7 GBytes  10.0 Gbits/sec
[  5]  0.0-10.0 sec  10.6 GBytes  9.13 Gbits/sec
[ 14]  0.0-10.0 sec  11.3 GBytes  9.69 Gbits/sec
[SUM]  0.0-10.0 sec  44.3 GBytes  38.0 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -P 8

------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[ 20] local 127.0.0.1 port 34964 connected with 127.0.0.1 port 5001
[ 14] local 127.0.0.1 port 34956 connected with 127.0.0.1 port 5001
[  3] local 127.0.0.1 port 34950 connected with 127.0.0.1 port 5001
[  5] local 127.0.0.1 port 34952 connected with 127.0.0.1 port 5001
[ 19] local 127.0.0.1 port 34960 connected with 127.0.0.1 port 5001
[ 21] local 127.0.0.1 port 34962 connected with 127.0.0.1 port 5001
[ 18] local 127.0.0.1 port 34958 connected with 127.0.0.1 port 5001
[ 13] local 127.0.0.1 port 34954 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[ 20]  0.0-10.0 sec  4.83 GBytes  4.14 Gbits/sec
[ 14]  0.0-10.0 sec  6.46 GBytes  5.54 Gbits/sec
[  3]  0.0-10.0 sec  5.10 GBytes  4.38 Gbits/sec
[  5]  0.0-10.0 sec  5.48 GBytes  4.71 Gbits/sec
[ 19]  0.0-10.0 sec  5.65 GBytes  4.85 Gbits/sec
[ 21]  0.0-10.0 sec  4.98 GBytes  4.27 Gbits/sec
[ 18]  0.0-10.0 sec  5.96 GBytes  5.11 Gbits/sec
[ 13]  0.0-10.0 sec  4.87 GBytes  4.18 Gbits/sec
[SUM]  0.0-10.0 sec  43.3 GBytes  37.2 Gbits/sec
```

Aqui houve uma separação da transferência em **P** partições, onde P é o número especificado na flag P. O desempenho final é semelhante a execução do iperf sem nenhuma flag, mas o recurso largura de banda é dividido de forma a cada uma das P partições ter 1/P da largura de banda.

No final, a soma da quantidade transferida e também a largura de banda é semelhante à execução `iperf -c 127.0.0.1`