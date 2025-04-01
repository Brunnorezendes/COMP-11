function [m, b] = identificarCruiseControl(f, t, v)
% [m, b] = identificaCruiseControl(f, t, v) utiliza identificacao de
% sistemas para determinar parametros da planta do cruise control. Assume
% que foi realizado um experimento com forca constante f com o carro
% comecando em repouso. Nesse experimento, a velocidade do carro foi
% medida nos tempos t (t eh um vetor) e os resultados foram armazenados no
% vetor v. As saidas da funcao sao os parametros da planta: a massa m e o
% fator de amortecimento b.

e = exp(1);
% Implementar identificacao do cruise control
n = length(t);
vinf = max(v);
b = f/vinf;
dist = vinf;
for i=1:n
    if dist>abs(0.632*vinf-v(i))
        dist = abs(0.632*vinf-v(i));
        tau = t(i);
    end
end
m = b*tau;
end