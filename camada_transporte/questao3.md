# Questão 03
O IPERF é uma ferramenta que é muito utilizada para realizar a avaliação de desempenho de redes. Ela permite que você crie conexões TCP, modificando os parâmetros desejados das configurações que serão usadas pelo protocolo, bem como também possibilita o envido de dados através de UDP. Execute a ferramenta com as opções indicadas abaixo, coletando os resultados de cada um deles e discutindo as diferenças observadas no desempenho dos testes de acordo com essas modificações.

Servidor: `iperf -s`
Cliente: `iperf -c 127.0.0.1`

### Modificando a janela (flag w)

```bash
$ iperf -c 127.0.0.1

------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37734 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  44.2 GBytes  38.0 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -w 1

WARNING: TCP window size set to 1 bytes. A small window size
will give poor performance. See the Iperf documentation.
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 4.50 KByte (WARNING: requested 1.00 Byte)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37746 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  16.2 MBytes  13.6 Mbits/sec
``` 

```bash
$ iperf -c 127.0.0.1 -w 2000

WARNING: TCP window size set to 2000 bytes. A small window size
will give poor performance. See the Iperf documentation.
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 4.50 KByte (WARNING: requested 1.95 KByte)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37748 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.1 sec  16.6 MBytes  13.9 Mbits/sec
```

```bash
$ iperf -c 127.0.0.1 -w 10000

------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 19.5 KByte (WARNING: requested 9.77 KByte)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37750 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  17.0 MBytes  14.2 Mbits/sec
```

```bash
$ iperf -c 127.0.0.1 -w 50000
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 97.7 KByte (WARNING: requested 48.8 KByte)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37752 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  15.5 GBytes  13.3 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -w 100000

------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size:  195 KByte (WARNING: requested 97.7 KByte)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37756 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  53.5 GBytes  46.0 Gbits/sec
```

Ao adicionar a flag w à uma chamada do iperf, ele realiza uma **tentativa** de fixar a janela no valor passado como argumento. Podemos ver isso mais claramente quando usamos o valor 1 e 2000, ambos valores abaixo do permitido pelo iperf, que a ferramenta determina que se valores muito baixos forem escolhidos, um valor padrão será usado que nesse no caso foi 4.5 KB.

Podemos ver que quando chamamos, no cliente, `iperf -c 127.0.0.1` a janela do TCP é a default (2.5MB), dessa forma há uma transferência de aproximadamente 44 GB pois a janela é grande. 

Quando usamos a flag -w 1 (buffer de 1 byte), o iperf determina que a janela será 4.5KB, como explicado anteriormente. O valor transferido diminui pois a janela diminuiu de 2.5MB para 4.5KB. O mesmo acontece para a flag -w 2000 pois o iperf também determinou a janela para 4.5 KB.

Algo parecido ocorre para os outros valores de flag. Um valor é requisitado, mas o iperf utiliza um diferente (geralmente maior). 

**Conclusão** :tada:
Quanto maior a janela usada, maior a largura de banda e consequentemente o valor final transferido (Transfer). 

### Modificando o MSS (flag M)

```bash
$ iperf -c 127.0.0.1
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 2.50 MByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37862 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  44.9 GBytes  38.6 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -M 100
WARNING: attempt to set TCP maximum segment size to 100, but got 536
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 25.0 KByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37864 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  48.8 GBytes  41.9 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -M 250
WARNING: attempt to set TCP maximum segment size to 250, but got 536
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 25.0 KByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37866 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  48.7 GBytes  41.8 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -M 500
WARNING: attempt to set TCP maximum segment size to 500, but got 536
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 45.0 KByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37868 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  45.3 GBytes  38.9 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -M 1000
WARNING: attempt to set TCP maximum segment size to 1000, but got 536
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 45.0 KByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37872 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  47.2 GBytes  40.5 Gbits/sec
```

```bash
$ iperf -c 127.0.0.1 -M 1500
WARNING: attempt to set TCP maximum segment size to 1500, but got 536
------------------------------------------------------------
Client connecting to 127.0.0.1, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 127.0.0.1 port 37874 connected with 127.0.0.1 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  49.4 GBytes  42.4 Gbits/sec
```

**Conclusão** :tada:
Aqui apesar das tentativas de determinar o MSS, o iperf o colocou em 536 o que parece ser um tipo de valor padrão. Devido ao MSS não ter sido alterado, não houve diferença muito significante na largura de banda.

### Modificando o número de  (flag P)
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

**Conclusão** :tada:
O dado transferido é dividido e enviado paralelamente em **n** partes, onde **n** é o argumento usado na flag -P

Tanto a largura de banda quanto o valor transferido de cada *thread* usada para enviar o dado é uma fração dos valores utilizados em um envio não-paralelo. Para notar isso, basta comparar qualquer uma exceção que usou a flag P com a execução sem a flag P e notar as semelhanças.

No final, o valor transferido somado é semelhante à execução `iperf -c 127.0.0.1`, pois o que ocorreu foi apenas o envio do mesmo dado só que fragmentado de forma a ser enviado em um número determinado de fluxos paralelos.